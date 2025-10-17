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
        self.__rig = None
        self.__inventory = [Asset("CryptoToken")]
        self.__max_trace_level = 5
        self.__trace_level = 0
        self.__exposed = False

    def __get_name(self):
        """
        This class returns the Hacker name.
        """
        return self.__name

    def __get_trace_level(self):
        """
        This class returns the Hacker trace level which is a measure of their notoriety.
        """
        return self.__trace_level

    def __get_exposed(self):
        """
        This class returns whether the Hacker has been exposed.
        """
        return self.__exposed

    def __set_name(self, name):
        """
        This class sets the Hacker name.
        """
        self.__name = name

    def __set_trace_level(self, trace_level):
        """
        This class sets the Hacker trace level.
        """
        self.__trace_level = trace_level

    def __set_exposed(self, exposed):
        """
        This class sets whether the Hacker has been exposed.
        """
        self.__exposed = exposed

    def acquire_rig(self, rig_name):
        for asset in self.__inventory:
            if asset.name == "CryptoToken":
                self.__inventory.remove(asset)
                self.__rig = Rig(rig_name)

    def launch_attack(self, target_rig):
        """
        This method launches a data spike object.
        :return: void
        """
        pass

    def encrypt_asset(self, asset_name):
        """
        This method encrypts the asset object.
        :return: void
        """
        for asset in self.__inventory:
            if asset.name == asset_name:
                asset.encryption = True

    def decrypt_asset(self, asset_name):
        """
        This method decrypts the asset object.
        :return: void
        """
        for asset in self.__inventory:
            if asset.get_name() == asset_name:
                asset.decrypt()

    def store_asset(self, asset_name):
        """
        This class stores an asset in the Hacker inventory.
        """
        pass

    def extract_assets(self, target_rig):
        """
        This class extracts assets from a broken / hacker rig.
        """
        pass

    def retrieve_asset(self, asset_name):
        """
        This class retrieves an asset from the Hacker inventory.
        """
        pass

    def scan_inventory(self):
        """
        This class scans the Hacker inventory.
        """
        pass

    def __str__(self):
        return_string = (f"{self.__name}\nTrace level:{self.__trace_level}")
        return_string += (f"\nRig:{self.__rig}")
        return_string += (f"\nInventory contents:")
        for asset in self.__inventory:
            return_string += f"\n{asset}"
        return return_string

    #Properties
    """
    Getters and Setters are set to private. The class can only be accessed through the class properties.
    """
    name = property(__get_name, __set_name)
    trace_level = property(__get_trace_level, __set_trace_level)
    exposed = property(__get_exposed, __set_exposed)
    #rig = property(__get_description)
    #inventory = property(__get_encrypted, __set_encrypted)