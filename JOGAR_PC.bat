@echo off
title Yu-Gi-Oh! Forbidden Memories (PC Recompiled)
echo ========================================================
echo   Iniciando Yu-Gi-Oh! Forbidden Memories (Nativo PC)
echo   - Mod Overhaul: Drops do Ato 1 ATIVADO!
echo   - Multi-Drop: 5 cartas por vitoria ATIVADO!
echo   - Indicador de Fusoes na Tela ATIVADO!
echo ========================================================
echo.

set MEMORIES_MOD_OVERHAUL_MOD=1
set MEMORIES_CARD_DROPS=5
set MEMORIES_FUSION_HELPER=1

cd /d "%~dp0pc_game\yfm-redecomp-v0.1.2"
start memories-pc.exe
exit
