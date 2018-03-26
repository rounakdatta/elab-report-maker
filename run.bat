@echo off
python -m pip install Flask img2pdf requests
python %~dp0%app.py