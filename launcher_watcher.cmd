@echo off
REM This batch script installs required Python packages and runs the watcher script.

REM Displaying a message indicating that requirements installation is starting.
echo Installing requirements...
REM Installing required Python packages listed in requirements.txt file using pip.
pip install -r requirements.txt

REM Displaying a message indicating that the watcher script is starting.
echo Running watcher script...
REM Running the watcher.py script to monitor file system events.
python watcher.py

REM Displaying a message indicating that the process is completed.
echo Process completed.
REM Pausing the script to keep the command prompt window open.
pause
