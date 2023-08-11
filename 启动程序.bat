@echo off
CHCP 65001
.\venv\python run.py --execution-provider cuda --frame-processor face_swapper face_enhancer --execution-threads 16 --many-faces
pause