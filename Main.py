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
    cc = Asset("CryptoToken")
    print(cc.name)
    cc.name = "Data Spike"
    print(cc)