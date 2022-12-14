# module to be used
from typing import NamedTuple

# defined a class that defines the data types of the following class attribute
class City(NamedTuple):
    name: str
    country: str
    year: int | None
    latitude: float
    longitude: float

