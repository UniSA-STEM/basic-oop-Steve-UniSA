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
            print(f"The asset {name} has an invalid description.")

    def get_name(self):
        """
        This method returns the name of the asset.
        :return: void
        """
        return self.__name

    def get_description(self):
        """
        This method returns the description of the asset.
        :return: void
        """
        return self.__description

    def is_encrypted(self):
        """
        This method returns the encryption status if the asset.
        :return: void
        """
        return self.__encrypted

    def set_name(self, name):
        """
        This method sets the name of the asset.
        :return: void
        """
        self.__name = name

    def set_description(self, description):
        """
        This method sets the description of the asset.
        :return: void
        """
        self.__description = description

    def set_encryption(self, encrypted):
        """
        This method encrypts the asset.
        :return: void
        """
        self.__encrypted = encrypted

    def __str__(self):
        """
        The string conversion method returns the asset name, description and encryption status.
        :return: void
        """
        return_string = f"{self.__name}: {self.__description} {"Encrypted" if self.__encrypted else ""}"
        return return_string

    # Properties
    name = property(get_name, set_name)
    description = property(get_description, set_description)
    encryption = property(is_encrypted, set_encryption)
