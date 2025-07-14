@echo off
cd /d C:\MidiaSocial\RadarAgro_Backend
call venv\Scripts\activate.bat
call venv\Scripts\uvicorn main:app --reload --port 8000
pause