from contextlib import nullcontext
from typing import ClassVar, TextIO

from BaseClasses import Tutorial
from settings import Group, FilePath
from worlds.AutoWorld import WebWorld, World

class RainSettings(Group):
    class GamePath(FilePath):
        description = "Rain World game executable"
        # is_exe = True TODO
        # md5s = [???]

    game_path: GamePath = GamePath("RainWorld.exe")

class RainWeb(WebWorld):
    theme = "ice"
    # bug_report_page = "???" TODO

    tut_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Rain World randomizer on your computer.",
        "English",
        "setup_en.md"
        "setup/en",
        ["SaltySyrup"],
    )

    tutorials = [tut_en]

class RainWorld(World):
    """
    You are a nomadic slugcat, both predator and prey in a broken ecosystem.
    Grab your spear and brave the industrial wastes, hunting enough food to survive, but be wary— other,
    bigger creatures have the same plan... and slugcats look delicious.
    """
    game = "Rain World"
    # options_dataclass = RainOptions TODO
    # options: RainOptions
    settings_key = "rain_settings"
    settings: ClassVar[RainSettings]

    web = RainWeb()

    # item_name_to_id TODO
    # location_name_to_id

    item_name_groups = {
        "Gates": {},
        "Karma": {"Karma"},
        "Passages": {},
        "Story": {},
        "Items": {}
    }
    location_name_groups = {
        "Passages": {},
        "Echoes": {},
        "Pearls": {},
        "SandboxTokens": {},
        "Story": {}
    }

    def generate_early(self) -> None:
        pass

    def create_regions(self) -> None:
        pass

    def create_items(self) -> None:
        pass

    def set_rules(self) -> None:
        pass

    def write_spoiler_header(self, spoiler_handle: TextIO) -> None:
        pass