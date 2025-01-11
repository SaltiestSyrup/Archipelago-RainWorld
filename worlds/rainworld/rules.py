from typing import TYPE_CHECKING

from ..generic.Rules import CollectionRule

if TYPE_CHECKING:
    from . import RainWorld

class RainRules:
    player: int
    world: "RainWorld"
    region_rules: dict[str, CollectionRule]

    def __init__(self, world: "RainWorld") -> None:
        self.player = world.player
        self.world = world

        self.region_rules = {
            "Outskirts":
                lambda state: state.has_any("SU_HI")
        }