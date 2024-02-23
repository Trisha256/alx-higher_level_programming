#!/usr/bin/python3

"""Defines models of a base class."""
import json
import turtle
import csv


class Base:
    """Base model.

    This represents the "base" of all other classes in this project.

    private class attributes: Number of instantiated objects.
    """
    __nb_objects = 0


    def __init__(self, id=None):
        """Initiate a new base.

        Args:
            id(int): identity of the new base.
        """
        if id is not None:
            self.id = id
        else:
            Base. __nb_objects += 1
            self.id =  Base. __nb_objects



