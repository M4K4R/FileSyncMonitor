# File Watcher and Synchronizer

This Python script monitors changes in a specified folder and executes a synchronization command when a file is saved in Visual Studio Code.

## Setup

1. Clone this repository to your local machine.
2. Navigate to the project directory.

### Requirements

- Python 3.x
- `pip` (Python package manager)

### Installation

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. Customize the `folder_path` variable in `watcher.py` to specify the folder you want to monitor.
2. Customize the `sync_command` variable in `watcher.py` to specify the synchronization command you want to execute.
3. Run the `launcher_watcher.cmd` script to start the watcher.

## Notes

- This script assumes that Visual Studio Code is installed on your system and running as `Code.exe`.
- The synchronization command (`sync.cmd`) is a placeholder. You should customize it according to your synchronization requirements.
- Press `Ctrl + S` in Visual Studio Code to trigger the synchronization command when saving a file.

## Contributions

Contributions are welcome! While the script is primarily tailored for personal use to streamline tasks, there might be bugs or areas for improvement. Feel free to contribute by opening an issue or submitting a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
