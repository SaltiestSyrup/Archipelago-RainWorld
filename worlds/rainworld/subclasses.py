from BaseClasses import Item, Location, Entrance, Region


class RainItem(Item):
    game: str = "Rain World"

class RainLocation(Location):
    game: str = "Rain World"

class RainGateEntrance(Entrance):
    world: "RainWorld | None" = None

class RainRegion(Region):
    entrance_type = RainGateEntrance