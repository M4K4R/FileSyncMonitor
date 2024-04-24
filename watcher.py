import os
import subprocess
import time
import keyboard
import psutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Specify the folder path to monitor
folder_path = "./"

# Command to use for synchronization
sync_command = "sync.cmd"

# Variable to track if Visual Studio Code is running
vscode_running = False

# Define a class to handle file system changes
class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Check if the event is for a file modification
        if not event.is_directory and event.event_type == 'modified':
            # Check if Visual Studio Code is running and Ctrl+S is pressed
            if vscode_running and keyboard.is_pressed('ctrl+s'):
                # Execute the synchronization command
                subprocess.call(sync_command, shell=True)
                print("Change detected. Sync command executed.")

# Function to check if Visual Studio Code is running
def check_vscode():
    global vscode_running
    vscode_running = any("Code.exe" in p.name() for p in psutil.process_iter())

# Main function to start monitoring file changes
def main():
    # Create an instance of the file change handler
    file_change_handler = FileChangeHandler()
    # Create an observer to monitor the folder for changes
    observer = Observer()
    observer.schedule(file_change_handler, path=folder_path, recursive=True)
    observer.start()

    try:
        # Continuously check if Visual Studio Code is running
        check_vscode()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Stop the observer if Ctrl+C is pressed
        observer.stop()
    # Wait for the observer to join the main thread
    observer.join()

# Entry point of the script
if __name__ == "__main__":
    main()
