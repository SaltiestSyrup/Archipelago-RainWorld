from enum import IntFlag
from typing import Optional, Callable

from BaseClasses import Location, Region, CollectionState, MultiWorld
from . import RainLocation

# Currently unused, will this actually be needed?
class LocationData:
    """Stores a location's information to be loaded during generation"""
    def __init__(self, name: str, address: int, region: str):
        self.name = name
        self.address = address
        self.region = region

    def make_location(self, player: int, multiworld: MultiWorld) -> Location:
        multi_region = multiworld.get_region(self.region, player)
        loc = RainLocation(player, self.name, self.address, multi_region)
        multi_region.locations.append(loc)
        return loc