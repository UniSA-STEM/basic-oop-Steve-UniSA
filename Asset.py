"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Asset:
    def __init__(self, name: str):
        """
        This class represents a digital asset. Assets have a name, description, and a new attribute encrypted,
        which is a boolean. By default, assets are not encrypted.
        """
        self.__valid_asset_names = ["CryptoToken", "Data Spike", "Removable Drive", "Security Chip", "Hardware Patch"]
        self.__asset_descriptions = ["Used to acquire or repair rigs.", "Used in battles.",
                                     "Found in rigs and used for extraction.",
                                     "Used to encrypt or decrypt assets.", "Used to upgrade rigs."]
        # If the asset description is in the list of valid descriptions, add the asset otherwise raise an error.
        if name in self.__valid_asset_names:
            self.__name = name
            self.__description = self.__asset_descriptions[self.__valid_asset_names.index(name)]
            self.__encrypted = False
        else:
            print(f"The asset {name} is not a valid asset type.")

    def __get_name(self) -> str:
        """
        This method returns the name of the asset.
        :return: void
        """
        return self.__name

    def __get_description(self) -> str:
        """
        This method returns the description of the asset.
        :return: void
        """
        return self.__description

    def __is_encrypted(self) -> bool:
        """
        This method returns the encryption status if the asset.
        :return: void
        """
        return self.__encrypted

    def __set_name(self, name: str) -> None:
        """
        This method sets the name of the asset.
        :return: void
        """
        if name in self.__valid_asset_names:
            self.__name = name
            self.__description = self.__asset_descriptions[self.__valid_asset_names.index(name)]
            self.__encrypted = False
        else:
            print(f"The asset {name} is not a valid asset type.")

    def __set_encryption(self, encrypted: bool) -> None:
        """
        This method encrypts the asset.
        :return: void
        """
        self.__encrypted = encrypted

    def __str__(self) -> str:
        """
        The string conversion method returns the asset name, description and encryption status.
        :return: void
        """
        return_string = f"{self.__name}: {self.__description} {"Encrypted" if self.__encrypted else ""}"
        return return_string

    # Properties
    name = property(__get_name, __set_name)
    description = property(__get_description)
    encryption = property(__is_encrypted, __set_encryption)
