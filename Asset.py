"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Asset:
    def __init__(self, name, description):
        """
        This class represents a digital asset. Assets have a name, description, and a new attribute encrypted,
        which is a boolean. By default, assets are not encrypted.
        """
        self.__valid_descriptions = ["CryptoToken", "Data Spike", "Removable Drive", "Security Chip", "Hardware Patch"]
        # If the asset description is in the list of valid descriptions, add the asset otherwise raise an error.
        if description in self.__valid_descriptions:
            self.__name = name
            self.__description = description
            self.__encrypted = False
        else:
            print(f"Invalid description")

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def is_encrypted(self):
        return self.__encrypted

    def set_name(self, name):
        self.__name = name

    def set_description(self, description):
        self.__description = description

    def encrypt(self):
        self.__encrypted = True
        print(f"Encrypted: {self.__name}")

    def decrypt(self):
        self.__encrypted = False
        print(f"decrypted: {self.__name}")

    def __str__(self):
        return_string = f"{self.__name}: {self.__description} {"Encrypted" if self.__encrypted else ""}"
        return return_string
