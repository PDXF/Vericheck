@echo off
REM Batch file to open VeriCheck - Advanced CLI Validator

REM Navigate to the directory where this batch file is located
cd d %~dp0

REM Run VeriCheck Python script
python vericheck.py

REM Pause to keep the command prompt open after execution
pause
