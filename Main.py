"""
File: main.py
Description: <A brief description of this Python module.>
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset

if __name__ == "__main__":
    asset = Asset("CryptoToken")
    asset.encryption = 1
    print(asset)
    asset.encryption = 3
    print(asset)
    asset.encryption = True
    print(asset)
    asset.encryption = False
    print(asset)
