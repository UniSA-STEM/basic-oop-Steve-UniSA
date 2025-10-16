"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Rig:
    def __init__(self, name):
        """
        This class represents a Rig object.
        """
        self.__name = name
        self.__damage_counter = 0
        self.__broken_state = False
        self.__stored_assets = []
        self.__upgrade_level = 0

    def get_name(self):
        """
        This class returns the Rig name.
        """
        return self.__name

    def get_damage_count(self):
        """
        This class returns the Rig damage level.
        """
        return self.__damage_counter

    def get_broken_state(self):
        """
        This class returns the state of the Rig.
        """
        return self.__broken_state

    def get_stored_assets(self):
        return self.__stored_assets

    def get_upgrade_level(self):
        return self.__upgrade_level

    def set_name(self, name):
        self.__name = name

    def set_damage_count(self, damage_count):
        self.__damage_counter = damage_count

    def set_broken_state(self, broken_state):
        self.__broken_state = broken_state

    def set_stored_assets(self, stored_assets):
        self.__stored_assets = stored_assets

    def set_upgrade_level(self, upgrade_level):
        self.__upgrade_level = upgrade_level

    def repair(self):
        """
        This method repairs the rig object.
        :return: void
        """
        if self.damage_counter > 0:
            self.damage_counter = 0
            self.broken_state = False
        else:
            print("No repair is needed")

    def upgrade(self):
        """
        This method upgrades the rig object.
        :return: void
        """
        self.__upgrade_level += 1

    def hit(self):
        """
        This method records damage to the rig object.
        :return: void
        """
        self.damage_counter += 1

    def condition(self):
        """
        This method checks whether the rig object is damaged or not.
        :return:
        """
        return self.__damage_counter

    def generate_asset(self):
        """
        This method generates a new asset.
        :return:
        """

    def __str__(self):
        return_string = f"{self.__name}\nCondition:"
        return return_string
