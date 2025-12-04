@echo off
REM 編譯所有 Jack 專案

jack2vm.exe ..\jack\Seven
jack2vm.exe ..\jack\Square
jack2vm.exe ..\jack\Average
REM jack2vm.exe ..\jack\Pong
jack2vm.exe ..\jack\ConvertToBin
jack2vm.exe ..\jack\ComplexArrays

pause
