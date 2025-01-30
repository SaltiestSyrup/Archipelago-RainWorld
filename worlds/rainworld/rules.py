from enum import IntFlag

from BaseClasses import CollectionState
from ..generic.Rules import CollectionRule

class SlugcatAccessibility(IntFlag):
    """Helps determine locations that a given slugcat has in their seeds"""
    nobody = 0b00000000

    survivor = 0b00000001
    monk = 0b00000010
    hunter = 0b00000100
    gourmand = 0b00001000
    artificer = 0b00010000
    rivulet = 0b00100000
    spearmaster = 0b01000000
    saint = 0b10000000

    # Feel free to add more of these groupings if they make sense
    base_game = 0b00000111
    """Survivor, Monk, and Hunter"""
    downpour = 0b11111000
    """Gourmand, Artificer, Rivulet, Spearmaster, and Saint"""
    past = 0b01010000
    """Artificer and Spearmaster"""

    everybody = 0b11111111

#class RainRules:
    #slugcat_rules = dict[str, CollectionRule]
    #"""Rules defining which slugcats can reach locations"""

    #def __init__(self, world: "RainWorld"):
    #    self.player = world.player
    #    self.world = world

        # Convert accessibility flags into CollectionRules
        #self.slugcat_rules = {name: lambda state: self.slugcat_can_reach(rule)
        #                      for name, rule in SLUGCAT_RULES}

    #def slugcat_can_reach(self, accessibility: SlugcatAccessibility) -> bool:
    #    return self.world.chosen_slugcat & accessibility != 0

# TODO: Define slugcat accessibility rules for Downpour
# Currently only defined for Survivor, Monk, and Hunter
# Undefined locations are considered universally accessible
SLUGCAT_RULES: dict[str, SlugcatAccessibility] = {
    "Token-BubbleGrass": SlugcatAccessibility(0b00000101),
    "Token-CyanLizard": SlugcatAccessibility.hunter,
    "Token-DropBug": SlugcatAccessibility(0b00000101),
    "Token-RedLizard": SlugcatAccessibility.hunter,
    "Token-MirosBird": SlugcatAccessibility.hunter,
    "Token-SeaLeech": SlugcatAccessibility(0b00000101),
    "Token-BigEel": SlugcatAccessibility.hunter,
    "Token-KingVulture": SlugcatAccessibility.hunter,
    "Token-Centiwing": SlugcatAccessibility(0b00000101),
    "Token-SpitterSpider": SlugcatAccessibility.hunter,
    "Token-Deer": SlugcatAccessibility.hunter,
    "Token-SlimeMold": SlugcatAccessibility(0b00000101),
    "Token-RedCentipede": SlugcatAccessibility.hunter,
    "Token-TentaclePlant": SlugcatAccessibility.hunter,
    "Token-DaddyLongLegs": SlugcatAccessibility(0b00000011),
    "Meet_LttM": SlugcatAccessibility(0b00000011),
    "Save_LttM": SlugcatAccessibility.hunter,
}