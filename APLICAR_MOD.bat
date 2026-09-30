@echo off
title Yu-Gi-Oh! Forbidden Memories — Overhaul Mod Patcher
cd /d "%~dp0"
echo ===================================================
echo   Aplicando o Mod Overhaul no Yu-Gi-Oh! FM
echo ===================================================
python tools/apply_all_patches.py
pause
