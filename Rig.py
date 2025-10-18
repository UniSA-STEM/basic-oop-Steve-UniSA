"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset


class Rig:
    def __init__(self, name: str) -> None:
        """
        This class represents a Rig object.
        :return: void
        """
        self.name = name
        self.__damage_counter = 0
        self.__broken_state = False
        self.__stored_assets = [Asset("Data Spike"), Asset("Data Spike"), Asset("Removable Drive")]
        self.__upgrade_level = 0

    def __get_name(self) -> str:
        """
        This method returns the Rig name.
        """
        return self.__name

    def __get_damage_count(self) -> int:
        """
        This method returns the Rig damage level.
        """
        return self.__damage_counter

    def __get_broken_state(self) -> bool:
        """
        This method returns whether the Rig is broken or not.
        """
        return self.__broken_state

    def __get_stored_assets(self) -> list[Asset]:
        """
        This method returns the Assets stored by the Rig.
        """
        return self.__stored_assets

    def __get_upgrade_level(self) -> int:
        """
        This method returns the upgrade level of the Rig.
        """
        return self.__upgrade_level

    def __set_name(self, name: str) -> None:
        """
        This method updates the name of the Rig.
        :return: void
        """
        if isinstance(name, str):
            self.__name = name

    def store_asset(self, asset: Asset) -> None:
        """
        This method stores an Asset in the rig object.
        :return: void
        """
        if isinstance(asset, Asset):
            self.__stored_assets.append(asset)

    def remove_asset(self, asset: Asset) -> None:
        """
        This method stores an Asset in the rig object.
        :return: void
        """
        if isinstance(asset, Asset):
            self.__stored_assets.remove(asset)

    def repair(self, asset: Asset) -> None:
        """
        This method repairs the rig object.
        :return: void
        """
        if isinstance(asset, Asset):
            crypto_token = None
            for asset in self.stored_assets:
               if asset.name == "CryptoToken":
                    crypto_token = asset
            if crypto_token is not None:
                if self.__damage_counter > 0:
                    self.__damage_counter = 0
                    self.__broken_state = False
                    self.__stored_assets.remove(crypto_token)
                else:
                    print("No repair is needed")

    def upgrade(self) -> None:
        """
        This method upgrades the rig object.
        :return: void
        """
        hardware_patch = None
        for asset in self.stored_assets:
            if asset.name == "Hardware Patch":
                hardware_patch = asset
            if hardware_patch is not None:
                self.__upgrade_level += 1
                self.__stored_assets.remove(hardware_patch)

    def hit(self) -> None:
        """
        This method records damage to the rig object.
        :return: void
        """
        self.__damage_counter += 1

    def generate_asset(self) -> None:
        """
        This method generates a random new asset and stores it in the rig object.
        :return: void
        """
        random_asset = Asset("Random Asset")
        self.store_asset(random_asset)

    def __str__(self) -> str:
        """
        The string conversion method returns the rig name and details.
        :return: str
        """
        return_string = f"{self.__name}\nDamage count:{self.damage_count}"
        return_string += f"\nBroken state:{self.broken_state}"
        return_string += f"\nUpgrade level:{self.upgrade_level}"
        return_string += f"\nStored assets:"
        for asset in self.stored_assets:
            return_string += f"\n{asset}"
        return return_string

    # Properties
    """
    Getters and Setters are set to private. The class can only be accessed through the class properties and methods.
    """
    name = property(__get_name, __set_name)
    damage_count = property(__get_damage_count)
    broken_state = property(__get_broken_state)
    stored_assets = property(__get_stored_assets)
    upgrade_level = property(__get_upgrade_level)
