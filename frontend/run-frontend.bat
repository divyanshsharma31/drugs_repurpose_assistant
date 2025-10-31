@echo off
setlocal enableextensions enabledelayedexpansion
cd /d "%~dp0"

where node >nul 2>nul
if errorlevel 1 (
  echo Node.js is not in PATH. Please install Node.js 18+ and retry.
  pause
  exit /b 1
)

if not exist node_modules (
  echo Installing frontend dependencies...
  npm install || goto :npmfail
)

echo Starting Vite dev server...
npm run dev
exit /b 0

:npmfail
echo Failed to install frontend dependencies. Check your internet connection or proxy.
pause
exit /b 1
