"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import random


class Asset:
    def __init__(self, name: str):
        """
        This class represents a digital asset. Assets have a name, description, and a new attribute encrypted,
        which is a boolean. By default, assets are not encrypted.
        """
        # If the asset description is in the list of valid descriptions, add the asset otherwise raise an error.
        self.__valid_asset_names = ["CryptoToken", "Data Spike", "Removable Drive", "Security Chip", "Hardware Patch"]
        self.__asset_descriptions = ["Used to acquire or repair rigs.", "Used in battles.",
                                     "Found in rigs and used for extraction.",
                                     "Used to encrypt or decrypt assets.", "Used to upgrade rigs."]
        self.name = name
        self.encrypted = False

    def __get_name(self) -> str:
        """
        This method returns the name of the asset. This method is private and can only be accessed by the class properties.
        :return: str
        """
        return self.__name

    def __get_description(self) -> str:
        """
        This method returns the description of the asset. This method is private and can only be accessed by the class properties.
        :return: str
        """
        return self.__description

    def __get_encrypted(self) -> bool:
        """
        This method returns the encryption status if the asset. This method is private and can only be accessed by the class properties.
        :return: bool
        """
        return self.__encrypted

    def __set_name(self, name: str) -> None:
        """
        This method sets the name of the asset. This method is private and can only be accessed by the class properties.
        :param name: str
        :return: void
        """
        if isinstance(name, str):
            if name == "Random Asset":
                random_asset_name = self.__get_random_name()
                self.__name = random_asset_name
                self.__description = self.__asset_descriptions[self.__valid_asset_names.index(random_asset_name)]
            elif name in self.__valid_asset_names:
                self.__name = name
                self.__description = self.__asset_descriptions[self.__valid_asset_names.index(name)]
            else:
                print(f"The asset {name} is not a valid asset type.")
        else:
            print(f"Hacker name must be a string.")

    def __get_random_name(self) -> str:
        """
        This method returns a random Asset name and is used to generate a random Asset.
        :return: str
        """
        asset_name_index = random.randint(0, len(self.__valid_asset_names) - 1)
        asset_name = self.__valid_asset_names[asset_name_index]
        return asset_name

    def __set_encrypted(self, encrypted: bool) -> None:
        """
        This method encrypts the asset. This method is private and can only be accessed by the class properties.
        :param encrypted: bool
        :return: void
        """
        if isinstance(encrypted, bool):
            self.__encrypted = encrypted
        else:
            print(f"The encryption status of {encrypted} is not valid.")

    def __str__(self) -> str:
        """
        The string conversion method returns the asset name, description and encryption status.
        :return: str
        """
        return f"{self.__name}: {self.__description} {"Encrypted" if self.__encrypted else ""}"

    def __eq__(self, other) -> bool:
        """
        Define equality comparison for objects of the asset class.
        :param other: Asset object
        :return: bool
        """
        return self.__name == other.name and self.__encrypted == other.encrypted

    # Properties
    """
    Getters and Setters are set to private. The class can only be accessed through the class properties and methods.
    """
    name = property(__get_name, __set_name)
    description = property(__get_description)
    encrypted = property(__get_encrypted, __set_encrypted)
