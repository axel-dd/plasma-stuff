import subprocess
from glob import glob
from pathlib import Path
from shutil import copy2

scriptDir = str(Path(__file__).resolve().parent)

stdout = subprocess.run(['kf5-config', '--path', 'services'], stdout=subprocess.PIPE).stdout.decode('utf-8')
firstLine = stdout.split('\n', 1)[0]
paths = firstLine.split(":")
home = str(Path.home())

if home in paths[0]:
    installDir = paths[0]
elif home in paths[1]:
    installDir = paths[1]

if Path(installDir).exists():
    for file in glob(f'{scriptDir}/*.desktop'):
        print(f'Installing "{file}" to "{installDir}"')
        copy2(file, installDir)