"""
File: main.py
Description: <A brief description of this Python module.>
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from Rig import Rig
from Hacker import Hacker


def main():
    asset = Asset("ss", "CryptoToken")
    print(asset)

    hacker = Hacker()
    print(hacker)


if __name__ == '__main__':
    main()
