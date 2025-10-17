"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
#from Hacker import Hacker

class Rig:
    def __init__(self, name : str)  -> None:
        """
        This class represents a Rig object.
        :return: void
        """
        self.name = name
        self.__damage_counter = 0
        self.__broken_state = False
        self.__stored_assets = [Asset("Data Spike"), Asset("Data Spike")]
        self.__upgrade_level = 0

    def __get_name(self) -> str:
        """
        This class returns the Rig name.
        """
        return self.__name

    def __get_damage_count(self) -> int:
        """
        This class returns the Rig damage level.
        """
        return self.__damage_counter

    def __get_broken_state(self) -> bool:
        """
        This class returns whether the Rig is broken or not.
        """
        return self.__broken_state

    def __get_stored_assets(self):
        """
        This class returns the Assets stored by the Rig.
        """
        return self.__stored_assets

    def __get_upgrade_level(self) -> int:
        """
        This class returns the upgrade level of the Rig.
        """
        return self.__upgrade_level

    def __set_name(self, name : str) -> None:
        """
        This class updates the name of the Rig.
        :return: void
        """
        self.__name = name

    def store_asset(self, asset : Asset) -> None:
        """
        This method stores an Asset in the rig object.
        :return: void
        """
        if isinstance(asset, Asset):
            self.__stored_assets.append(asset)

    def repair(self, asset : Asset) -> None:
        """
        This method repairs the rig object.
        :return: void
        """
        if isinstance(asset, Asset):
            if asset.name == "CryptoToken":
                if self.__damage_counter > 0:
                    self.__damage_counter = 0
                    self.__broken_state = False
                else:
                    print("No repair is needed")

    def upgrade(self) -> None:
        """
        This method upgrades the rig object.
        :return: void
        """
        self.__upgrade_level += 1

    def hit(self) -> None:
        """
        This method records damage to the rig object.
        :return: void
        """
        self.__damage_counter += 1

    def generate_asset(self) -> None:
        """
        This method generates a new asset.
        :return: void
        """
        pass

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

    #Properties
    """
    Getters and Setters are set to private. The class can only be accessed through the class properties and methods.
    """
    name = property(__get_name, __set_name)
    damage_count = property(__get_damage_count)
    broken_state = property(__get_broken_state)
    stored_assets = property(__get_stored_assets)
    upgrade_level = property(__get_upgrade_level)