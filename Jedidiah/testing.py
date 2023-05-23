import subprocess

sound_file = '/home/pi/dev/hutto/Jedidiah/output.mp3'
subprocess.call(['xdg-open', sound_file])