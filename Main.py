"""
File: main.py
Description: <A brief description of this Python module.>
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""
#from Hacker import Hacker
#from Asset import Asset
from Rig import Rig

if __name__ == "__main__":
    rig = Rig("CrazyRig")
    for num in range(1, 110):
        rig.generate_asset()
    print(rig)