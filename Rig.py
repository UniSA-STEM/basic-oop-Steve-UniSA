"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Rig:
    def __init__(self):
        """
        This class represents a rig object.
        """
        self.name = ""
        self.damage_counter = 0
        self.broken_state = False
        self.storage = []
        self.upgrade_level = 0

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
