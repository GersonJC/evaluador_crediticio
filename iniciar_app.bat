@echo off
echo ================================
echo INICIO DE LA APLICACIÓN FASTAPI
echo ================================

:: Activar el entorno virtual
call "%~dp0.venv\Scripts\activate"

:: Verificar si FastAPI está instalado
where uvicorn >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo Instalando dependencias desde requirements.txt...
    pip install --upgrade pip
    pip install -r requirements.txt
) ELSE (
    echo Dependencias ya instaladas.
)

:: Iniciar el servidor
echo Iniciando el servidor FastAPI en http://127.0.0.1:8000 ...
python -m uvicorn app.main:app --reload

pause