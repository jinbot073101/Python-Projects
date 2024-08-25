import subprocess
import platform

def open_terminal():
    so = platform.system()
    if so == "Windows":
        subprocess.run('start powershell -NoExit -Command "cd ~"', shell=True)
    elif so == "Darwin": 
        subprocess.run(['open', '-a', 'Terminal'])
    elif so == "Linux":
        subprocess.run(['gnome-terminal'])
    else:
        print(f"could not open a terminal in {so}.")

open_terminal()