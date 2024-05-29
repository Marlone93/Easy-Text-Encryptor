@echo off
chcp 65001 > nul
:menu
echo Choose 1 or 2:
echo 1. Run's Text to Number
echo 2. Run's Number to Text 
set /p choice="Type 1 or 2: "
if "%choice%"=="1" (
    python Text-to-Num.py
) else if "%choice%"=="2" (
    python Num-to-Text.py
) else (
    echo Invalid!
)
pause
cls
goto menu