@echo off
setlocal

:: Correctly assign path
set "BLENDER_DIR=C:\Program Files\Blender Foundation\Blender 4.4"
set "BLENDER_PY=%BLENDER_DIR%\4.4\python\bin\python.exe"

:: Check if Blender Python exists
if exist "%BLENDER_PY%" (
    echo Found Blender Python at %BLENDER_PY%
) else (
    echo Blender Python not found at %BLENDER_PY%
    echo Please update BLENDER_DIR in the script.
    endlocal
    echo Press any key to exit . . .
    pause >nul
    exit /b 1
)

:: Proceed with build or other commands
"%BLENDER_PY%" -m ensurepip
"%BLENDER_PY%" -m pip install --upgrade pip build
"%BLENDER_PY%" -m build %*

endlocal
echo Press any key to exit . . .
pause >nul
exit /b 1