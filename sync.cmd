@echo off
REM This batch script uses the robocopy command to copy files from a source directory to a destination directory.
REM Source directory: . (current directory)
REM Destination directory: C:\test\test
REM /MIR: Mirrors the source directory to the destination directory, deleting files in the destination that are not present in the source.
REM /XD ".git": Excludes the directory named .git from being copied.
REM /XF "sync.cmd": Excludes the file named sync.cmd from being copied.
robocopy . "C:\test\test" /MIR /XD ".git" /XF "sync.cmd"
