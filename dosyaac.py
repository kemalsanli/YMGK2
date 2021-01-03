import os, sys, subprocess
def Open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

def Clear_Console():
    if sys.platform == "win32":
        stream = os.system('cls')
    else:
        stream = os.popen('clear')
        output = stream.read()
        print(output)
