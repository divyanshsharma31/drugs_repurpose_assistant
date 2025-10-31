@echo off
setlocal enableextensions enabledelayedexpansion
cd /d "%~dp0"

where python >nul 2>nul
if errorlevel 1 (
  echo Python is not in PATH. Please install Python 3.9+ and retry.
  pause
  exit /b 1
)

if not exist .venv (
  echo Creating virtual environment...
  python -m venv .venv
)

call .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt || goto :pipfail

python main.py
exit /b 0

:pipfail
echo Failed to install Python dependencies. Check your internet connection or proxy.
pause
exit /b 1
