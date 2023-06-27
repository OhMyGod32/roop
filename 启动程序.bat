@echo off
CHCP 65001
.\venv\python run.py --execution-provider cuda --execution-threads 16
pause