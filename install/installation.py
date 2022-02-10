import os
import osr2mp4

code = int(os.system("python install.py"))

print('Oops look like something failed') if code == 1 else print("Successfully installed with optimized ffmpeg")

try:
    from osr2mp4.ImageProcess.Curves.libcurves import ccurves
    exists = True
except ImportError:
    exists = False

print("File is builded though so it's fine so shut the fuck up") if exists else ("No")