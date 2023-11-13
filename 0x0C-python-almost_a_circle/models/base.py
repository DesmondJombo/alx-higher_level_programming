#!/usr/bin/python3
"""This defines a base model class."""
import json
import csv


class Base:
    """the base model.

    represents the "base" for all other classes in the  project .

    Attributes:
        __nb_objects (int): instantiated Bases numbers.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initialize a new Base.

        Args:
            id (int): The new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_striing(list_dictionaries):
        """ JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list):list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """The JSON serialization of a list of objects to a file.

        Args:
            list_objs (list):inherited Base instances list.
        """
        fname = cls.__name__ + ".json"
        with open(fname, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """deserialization of a JSON string.

        Args:
            json_string (str):  JSON string  representation of dict lists .
        Returns:
            If json_string is None|| empty - an empty list.
            if correct -Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """class instantiated from a dictionary of attributes.

        Args:
            **dictionary (dict): Key pairs of attributes for initializtion.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """list of classes instantiated
        from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file doesn't exist - an empty list.
            if exists - a list of instantiated classes.
        """
        fname = str(cls.__name__) + ".json"
        try:
            with open(fname, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """CSV serialization of a list of objects to a file.

        Args:
            list_objs (list):inherited Base instances list.
        """
        fname = cls.__name__ + ".csv"
        with open(fname, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file doesn't exist -empty list.
            if it exists - a list of instantiated classes.
        """
        fname = cls.__name__ + ".csv"
        try:
            with open(fname, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([j, int(v)] for j, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
