# module to be used
from typing import NamedTuple

# defined a class that defines the data types of the following class attribute
class City(NamedTuple):
    name: str
    country: str
    year: int | None
    latitude: float
    longitude: float

    # defines a class method that takes a dictionary of attributes extracted from a DOT file and returns a new instance of the City class
    @classmethod
    def from_dict(cls, attrs):
        return cls(
            name = attrs["xlabel"],
            country = attrs["country"],
            year = int(attrs["years"]) or None,
            latitude = float(attrs["latitude"]),
            longitude = float(attrs["longitude"]),
        )