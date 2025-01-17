from dataclasses import dataclass

from Options import Choice, Toggle, PerGameCommonOptions, DefaultOnToggle


class DownpourDLC(Toggle):
    """
    Whether the More Slugcats Expansion will be enabled
    You MUST have the
    """
    display_name = "Use MSC"

class Slugcat(Choice):
    """
    Which slugcat you intend to play as.
    The campaign you start in-game MUST match this option
    """
    display_name = "Chosen Slugcat"
    default = 0
    option_survivor = 0
    option_monk = 1
    option_hunter = 2
    option_gourmand = 3
    option_artificer = 4
    option_rivulet = 5
    option_spearmaster = 6
    option_saint = 7

    # ---aliases---
    alias_white = 0
    alias_yellow = 1
    alias_red = 2
    alias_gourm = 3
    alias_arty = 4
    alias_wetmouse = 5
    alias_spear = 6
    alias_sait = 7

class Passages(DefaultOnToggle):
    """
    Whether Passages should be randomized
    The teleport tokens will also be randomized
    """
    display_name = "Randomize Passages"

class Echoes(DefaultOnToggle):
    """
    Whether Echoes count as locations
    Karma increases will still be randomized regardless
    """
    display_name = "Randomize Echoes"

class Pearls(DefaultOnToggle):
    """
    Whether collecting pearls count as locations
    """
    display_name = "Randomize Pearls"

class Tokens(DefaultOnToggle):
    """
    Whether collecting sandbox tokens count as locations
    """
    display_name = "Randomize Sandbox Tokens"

@dataclass
class RainOptions(PerGameCommonOptions):
    downpour: DownpourDLC
    slugcat: Slugcat
    passages: Passages
    echoes: Echoes
    pearls: Pearls
    tokens: Tokens
