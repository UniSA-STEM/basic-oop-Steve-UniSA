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
        self.__damage_count = 0
        self.__broken_state = False
        self.__storage = [Asset("Data Spike"), Asset("Data Spike"), Asset("Removable Drive")]
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
        return self.__damage_count

    def __get_condition(self) -> str:
        """
        This method returns the Rig condition.
        """
        if self.damage_count == 0:
            condition = "Pristine (Level 2)"
        elif self.damage_count == 1:
            condition = "Damaged (Level 1)"
        else:
            condition = "Broken (Level 0)"
        return condition

    def __get_broken_state(self) -> bool:
        """
        This method returns whether the Rig is broken or not.
        """
        return self.__broken_state

    def __get_stored_assets(self) -> list[Asset]:
        """
        This method returns the Assets stored by the Rig.
        """
        return self.__storage

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

    def __set_broken_state(self, broken_state: bool) -> None:
        """
        This method updates the broken state of the Rig.
        :return: void
        """
        if isinstance(broken_state, bool):
            self.__broken_state = broken_state

    def __set_damage_count(self, damage_count: int) -> None:
        """
        This method updates the broken state of the Rig.
        :return: void
        """
        if isinstance(damage_count, int):
            self.__damage_count = damage_count

    def store_asset(self, asset: Asset) -> None:
        """
        This method stores an Asset in the rig object.
        :return: void
        """
        if isinstance(asset, Asset):
            self.__storage.append(asset)

    def release_asset(self, asset: Asset) -> None:
        """
        This method stores an Asset in the rig object.
        :return: void
        """
        if isinstance(asset, Asset):
            self.__storage.remove(asset)

    def upgrade(self) -> None:
        """
        This method upgrades the rig object.
        :return: void
        """
        hardware_patch = None
        for asset in self.storage:
            if asset.name == "Hardware Patch":
                hardware_patch = asset
        if hardware_patch:
            self.__upgrade_level += 1
            self.__storage.remove(hardware_patch)
        else:
            print(f"A Hardware Patch is required to perform an upgrade\n")

    def hit(self) -> None:
        """
        This method records damage to the rig object.
        :return: void
        """
        self.damage_count += 1

    def repair(self) -> None:
        """
        This method repairs the rig object.
        :return: void
        """
        self.damage_count = 0
        self.broken_state = False

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
        return_string = f"Rig name: {self.__name}"
        return_string += f"\nCondition: {self.condition}"
        return_string += f"\nUpgrade level: {self.upgrade_level}"
        return_string += f"\nStored assets: "
        for asset in self.storage:
            return_string += f"\n\t{asset}"
        return_string += f"\n"
        return return_string

    # Properties
    """
    Getters and Setters are set to private. The class can only be accessed through the class properties and methods.
    """
    name = property(__get_name, __set_name)
    damage_count = property(__get_damage_count, __set_damage_count)
    broken_state = property(__get_broken_state, __set_broken_state)
    storage = property(__get_stored_assets)
    upgrade_level = property(__get_upgrade_level)
    condition = property(__get_condition)
