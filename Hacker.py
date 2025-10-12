"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from Rig import Rig


class Hacker:
    def __init__(self, name):
        """
        This class represents a hacker object.
        """
        self.__name = name
        self.__inventory = [Asset("CryptoToken1", "CryptoToken")]
        self.__trace_level = 0
        self.__exposed = False

    def acquire_rig(self):
        pass

    def launch_attack(self, target_rig):
        """
        This method launches a data spike object.
        :return: void
        """

    def extract_assets(self, target_rig):
        pass

    def encrypt_asset(self, asset_name):
        pass

    def decrypt_asset(self, asset_name):
        pass

    def store_asset(self, asset_name):
        pass

    def retrieve_asset(self, asset_name):
        pass

    def scan_inventory(self):
        pass

    def __str__(self):
        return_string = f"{self.__name}\nTrace level:{self.__trace_level}\nInventory contents:"
        for asset in self.__inventory:
            return_string += f"\n{asset}"
        return return_string
