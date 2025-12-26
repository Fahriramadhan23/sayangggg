@echo off
chcp 65001 >nul
echo.
echo ╔═════════════════════════════════════════════════════════╗
echo ║     Konverter HEIC ke JPG - Untuk Sayangku             ║
echo ╚═════════════════════════════════════════════════════════╝
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ✗ Python tidak ditemukan!
    echo.
    echo Solusi:
    echo 1. Install Python dari https://www.python.org/
    echo 2. Pastikan "Add Python to PATH" dicentang saat install
    echo 3. Buka Command Prompt baru dan jalankan script ini lagi
    echo.
    pause
    exit /b 1
)

echo ✓ Python ditemukan
echo.

REM Check if Pillow is installed
python -c "from PIL import Image" >nul 2>&1
if errorlevel 1 (
    echo ℹ Menginstall Pillow library...
    echo.
    pip install Pillow
    if errorlevel 1 (
        echo ✗ Gagal menginstall Pillow
        pause
        exit /b 1
    )
    echo.
    echo ✓ Pillow berhasil diinstall
    echo.
)

echo Memulai konversi gambar...
echo.
python convert_images.py

echo.
echo ╔═════════════════════════════════════════════════════════╗
echo ║              Konversi Selesai!                          ║
echo ╚═════════════════════════════════════════════════════════╝
echo.
pause
