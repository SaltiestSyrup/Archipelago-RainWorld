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
    # Values stored as to make comparisons to an IntFlag easier
    display_name = "Chosen Slugcat"
    default = 1
    option_survivor = 1
    option_monk = 2
    option_hunter = 4
    option_gourmand = 8
    option_artificer = 16
    option_rivulet = 32
    option_spearmaster = 64
    option_saint = 128

    # ---aliases---
    alias_white = 1
    alias_yellow = 2
    alias_red = 4
    alias_gourm = 8
    alias_arty = 16
    alias_wetmouse = 32
    alias_spear = 64
    alias_sait = 128

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
