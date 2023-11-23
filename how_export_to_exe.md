# Guide: How to compress calculator into Executable(.exe) using PyInstaller

This guide provides step-by-step instructions on how to create an executable (.exe) file from
the calculator project using PyInstaller.

## Steps:
### 1 - install PyInstaller: but it's already in the requirements.txt so just install it with 
``pip install -r requirements.txt``

[//]: # (``` python)

[//]: # (pip install -r requirements.txt)




### 2 - Run Pyinstaller command to package into .exe

``pyinstaller --name="Calculator" --noconfirm --noconsole --onefile --add-data='../files/:files/' --icon='../files/icon.png' --clean --log-level=WARN --distpath="outputEXE/dist" --workpath="outputEXE/build" --specpath="outputEXE" main.py``

go to the root folder of the project and open the "outputEXE" folder -> dist and open the .exe calculator and you're done :)