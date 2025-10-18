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
    def __init__(self, name: str) -> None:
        """
        This class represents a hacker object.
        """
        self.name = name
        # Set initial values for private attributes.
        self.__rig = None
        self.__inventory = [Asset("CryptoToken")]
        self.__trace_level = 0
        self.__exposed = False

    def __get_name(self) -> str:
        """
        This method returns the Hacker name.
        """
        return self.__name

    def __get_rig(self) -> Rig:
        """
        This method returns the Hacker's rig.
        """
        return self.__rig

    def __get_trace_level(self) -> int:
        """
        This method returns the Hacker trace level which is a measure of their notoriety.
        """
        return self.__trace_level

    def __get_exposed(self) -> bool:
        """
        This method returns whether the Hacker has been exposed.
        """
        return self.__exposed

    def __set_name(self, name: str) -> None:
        """
        This method sets the Hacker name.
        """
        if isinstance(name, str):
            self.__name = name
        else:
            print(f"Hacker name must be a string.")

    def __set_trace_level(self, trace_level: int) -> None:
        """
        This method sets the Hacker trace level.
        """
        max_trace_level = 5
        self.__trace_level = trace_level
        if self.__trace_level > max_trace_level:
            self.exposed = True

    def __set_exposed(self, exposed: bool) -> None:
        """
        This method sets whether the Hacker has been exposed.
        """
        if isinstance(exposed, bool):
            self.__exposed = exposed
        else:
            print(f"Hacker exposed must be a boolean.")

    def acquire_rig(self, rig) -> None:
        # Check that this hacker doesn't already have a rig
        if self.__rig is None:
            crypto_token = None
            for asset in self.__inventory:
                if asset.name == "CryptoToken":
                    crypto_token = asset
            if crypto_token is not None:
                if isinstance(rig, Rig):
                    self.__rig = rig
                    self.__inventory.remove(crypto_token)
                elif isinstance(rig, str):
                    self.__rig = Rig(rig)
                    self.__inventory.remove(crypto_token)
                else:
                    print(f"The rig could not be activated.")
            else:
                print(f"You do not have sufficient CryptoTokens.")
        else:
            print(f"You already have a Rig activated.")

    def encrypt_asset(self, asset: Asset) -> None:
        """
        This method encrypts the asset object.
        :return: void
        """
        if isinstance(asset, Asset):
            security_chip = None
            for asset in self.__inventory:
                if asset.name == "Security Chip":
                    security_chip = asset
            if security_chip is not None:
                asset.encrypted = True

    def decrypt_asset(self, asset: Asset) -> None:
        """
        This method decrypts the asset object.
        :return: void
        """
        if isinstance(asset, Asset):
            security_chip = None
            for asset in self.__inventory:
                if asset.name == "Security Chip":
                    security_chip = asset
            if security_chip is not None:
                asset.encrypted = False

    def store_asset(self, asset: Asset) -> None:
        """
        This method stores an asset in the Hacker inventory.
        """
        if isinstance(asset, Asset):
            if self.__rig not in None:
                if asset in self.__inventory:
                    self.__rig.store_asset(asset)
                    self.__inventory.remove(asset)
                else:
                    print(f"The asset is not in your inventory.")
            else:
                print(f"You do not have a Rig activated.")
        else:
            print(f"The object is not an asset.")

    def retrieve_asset(self, asset: Asset) -> None:
        """
        This method retrieves an asset from the Hacker inventory.
        """
        if isinstance(asset, Asset):
            if self.__rig not in None:
                if asset in self.__rig.stored_assets:
                    self.__rig.remove_asset(asset)
                    self.__inventory.append(asset)
                else:
                    print(f"You do not have a Rig activated.")
            else:
                print(f"The asset is not in your inventory.")
        else:
            print(f"The object is not an asset.")

    def scan_inventory(self, asset_name: str):
        """
        This method scans the Hacker inventory.
        """
        if isinstance(asset_name, str):
            searched_asset = None
            for asset in self.__inventory:
                if asset.name == asset_name:
                    searched_asset = asset
            if searched_asset is not None:
                self.__inventory.remove(searched_asset)
                return searched_asset
            else:
                print(f"The asset is not in your inventory.")
                return None
        else:
            print(f"The Asset name must be a string.")
            return None

    def launch_attack(self, target_rig: Rig) -> None:
        """
        This method launches a data spike object.
        :param target_rig:
        :return: void
        """
        data_spike = None
        for asset in self.__inventory:
            if asset.name == "Data Spike":
                data_spike = asset
        if data_spike is not None:
            if isinstance(target_rig, Rig):
                target_rig.hit()
                self.__inventory.remove(data_spike)
        else:
            print(f"Target rig must be a Rig.")

    def extract_assets(self, target_rig) -> None:
        """
        This method extracts assets from a broken / hacker rig.
        """
        if isinstance(target_rig, Rig):
            if target_rig.broken_state:
                for asset in target_rig.stored_assets:
                    self.__inventory.append(asset)
                    target_rig.remove_asset(asset)
        else:
            print(f"Target rig must be a Rig.")

    def __str__(self):
        return_string = (f"{self.__name}\nTrace level:{self.__trace_level}")
        return_string += (f"\nRig:{self.__rig}")
        return_string += (f"\nInventory contents:")
        for asset in self.__inventory:
            return_string += f"\n{asset}\n"
        return return_string

    # Properties
    """
    Getters and Setters are set to private. The class can only be accessed through the class properties and methods.
    """
    name = property(__get_name, __set_name)
    trace_level = property(__get_trace_level, __set_trace_level)
    exposed = property(__get_exposed, __set_exposed)
    rig = property(__get_rig)
    # inventory = property(__get_encrypted, __set_encrypted)
