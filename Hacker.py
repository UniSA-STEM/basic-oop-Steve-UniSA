"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Stephen Corns
ID: 110457922
Username: CORSY034
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Hacker:
    def __init__(self):
        """
        This class represents a hacker object.
        """
        self.__name = ""
        self.__inventory = []
        self.__trace_level = 0
        self.__exposed = False

    def launch_data_spike(self):
        """
        This method launches a data spike object.
        :return: void
        """

    def __str__(self):
        return_string = f"{self.__name}\nTrace level:{self.__trace_level}\nInventory contents:"
        return return_string
