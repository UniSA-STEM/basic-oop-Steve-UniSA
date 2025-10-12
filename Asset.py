"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Asset:
    def __init__(self):
        """
        This class represents an asset object.
        """
        self.__name = ""
        self.__description = ""
        self.__encrypted = False
        self.__valid_assets = ["CryptoToken", "Data Spike", "Removable Drive", "Security Chip", "Hardware Patch"]

    def __str__(self):
        return_string = f"{self.__name}:{self.__description} {"Encrypted" if self.__encrypted else ""}"
        return return_string
