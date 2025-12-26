#!/usr/bin/env python3
"""
Konverter HEIC ke JPG untuk galeri foto
Jalankan script ini untuk mengkonversi semua file HEIC di folder 'foto' ke JPG
"""

import os
from pathlib import Path
from PIL import Image
import sys

def convert_heic_to_jpg():
    """Konversi semua file HEIC dan MOV ke JPG/MP4 yang lebih compatible"""
    
    foto_dir = Path('foto')
    
    if not foto_dir.exists():
        print(f"Folder '{foto_dir}' tidak ditemukan!")
        return False
    
    heic_files = list(foto_dir.glob('*.HEIC'))
    jpg_files = list(foto_dir.glob('*.JPG'))
    jpeg_files = list(foto_dir.glob('*.JPEG'))
    
    print(f"Ditemukan {len(heic_files)} file HEIC")
    print(f"Ditemukan {len(jpg_files)} file JPG")
    print(f"Ditemukan {len(jpeg_files)} file JPEG")
    
    converted_count = 0
    
    # Konversi HEIC files
    for heic_file in heic_files:
        try:
            jpg_file = heic_file.with_suffix('.jpg')
            
            # Skip jika sudah ada versi JPG-nya
            if jpg_file.exists():
                print(f"✓ {heic_file.name} -> sudah ada {jpg_file.name}")
                continue
            
            print(f"Converting {heic_file.name}...", end=' ')
            
            # Buka dan konversi HEIC ke JPG
            image = Image.open(heic_file)
            
            # Rotate jika diperlukan berdasarkan EXIF
            try:
                from PIL import ExifTags
                exif = image._getexif()
                if exif:
                    for tag, value in exif.items():
                        if tag == 274:  # Orientation tag
                            if value == 3:
                                image = image.rotate(180, expand=True)
                            elif value == 6:
                                image = image.rotate(270, expand=True)
                            elif value == 8:
                                image = image.rotate(90, expand=True)
                            break
            except:
                pass
            
            # Convert RGBA to RGB jika diperlukan
            if image.mode in ('RGBA', 'LA', 'P'):
                background = Image.new('RGB', image.size, (255, 255, 255))
                background.paste(image, mask=image.split()[-1] if image.mode in ('RGBA', 'LA') else None)
                image = background
            elif image.mode != 'RGB':
                image = image.convert('RGB')
            
            # Save sebagai JPG
            image.save(jpg_file, 'JPEG', quality=95, optimize=True)
            print(f"✓ Berhasil -> {jpg_file.name}")
            converted_count += 1
            
        except Exception as e:
            print(f"✗ Error: {str(e)}")
    
    if converted_count > 0:
        print(f"\n✓ Berhasil mengkonversi {converted_count} file!")
        return True
    elif len(jpg_files) + len(jpeg_files) > 0:
        print(f"\n✓ Semua file sudah dalam format JPG/JPEG!")
        return True
    else:
        print(f"\n✗ Tidak ada file yang bisa dikonversi")
        return False

if __name__ == '__main__':
    try:
        # Check if PIL is available
        from PIL import Image
        convert_heic_to_jpg()
    except ImportError:
        print("Pillow library tidak terinstall.")
        print("Install dengan menjalankan: pip install Pillow")
        sys.exit(1)
