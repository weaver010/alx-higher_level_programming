#!/usr/bin/python3

"""base class."""
import json
import csv
import turtle


class Base:
    """Base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Args:
            id
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Args:
            list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Args:
            list_objs
        """
        r = cls.__name__ + ".json"
        with open(r, "w") as t:
            if list_objs is None:
                t.write("[]")
            else:
                e = [o.to_dictionary() for o in list_objs]
                t.write(Base.to_json_string(e))

    @staticmethod
    def from_json_string(json_string):
        """
        Args:
            json_string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Args:
            **dictionary
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                s = cls(1, 1)
            else:
                s = cls(1)
            s.update(**dictionary)
            return s

    @classmethod
    def load_from_file(cls):
        """Returns:
        """
        f = str(cls.__name__) + ".json"
        try:
            with open(f, "r") as e:
                s = Base.from_json_string(e.read())
                return [cls.create(**d) for d in s]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Args:
            list_objs
        """
        f = cls.__name__ + ".csv"
        with open(f, "w", newline="") as r:
            if list_objs is None or list_objs == []:
                r.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    w = ["id", "width", "height", "x", "y"]
                else:
                    w = ["id", "size", "x", "y"]
                q = csv.DictWriter(r, fieldnames=w)
                for i in list_objs:
                    q.writerow(i.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Returns:
        """
        f = cls.__name__ + ".csv"
        try:
            with open(f, "r", newline="") as r:
                if cls.__name__ == "Rectangle":
                    d = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                w = csv.DictReader(r, fieldnames=d)
                w = [dict([k, int(v)] for k, v in d.items())
                              for d in w]
                return [cls.create(**d) for d in w]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Args:
            list_rectangles
            list_squares
        """
        tu = turtle.Turtle()
        tu.screen.bgcolor("#b7312c")
        tu.pensize(3)
        tu.shape("turtle")

        tu.color("#ffffff")
        for i in list_rectangles:
            tu.showturtle()
            tu.up()
            tu.goto(i.x, i.y)
            tu.down()
            for i in range(2):
                tu.forward(i.width)
                tu.left(90)
                tu.forward(i.height)
                tu.left(90)
            tu.hideturtle()

        tu.color("#b5e3d8")
        for s in list_squares:
            tu.showturtle()
            tu.up()
            tu.goto(s.x, s.y)
            tu.down()
            for i in range(2):
                tu.forward(s.width)
                tu.left(90)
                tu.forward(s.height)
                tu.left(90)
            tu.hideturtle()

        tu.exitonclick()
