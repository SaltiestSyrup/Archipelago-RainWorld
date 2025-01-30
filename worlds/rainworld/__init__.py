from typing import ClassVar, TextIO, Any

from BaseClasses import Tutorial, ItemClassification, LocationProgressType
from settings import Group, FilePath
from worlds.AutoWorld import WebWorld, World
from .constants import ALL_ITEMS, ALL_LOCATIONS, PASSAGE_LOCATIONS, ECHO_LOCATIONS, PEARL_LOCATIONS, TOKEN_LOCATIONS, \
    SURVIVOR_LOCATIONS, MONK_LOCATIONS, HUNTER_LOCATIONS, GATE_ITEMS, PASSAGE_ITEMS, STORY_ITEMS, OBJECT_ITEMS
from .options import RainOptions, Slugcat
from .regions import ALL_REGIONS, GATES, ALL_REGIONS, LOCATIONS_MAP
from .rules import SLUGCAT_RULES, SlugcatAccessibility
from .subclasses import RainRegion, RainLocation, RainItem
from worlds.generic.Rules import set_rule


class RainSettings(Group):
    class GamePath(FilePath):
        description = "Rain World game executable"
        is_exe = True
        # md5s = [???]

    game_path: GamePath = GamePath("RainWorld.exe")

class RainWeb(WebWorld):
    theme = "ice"
    rich_text_options_doc = True

    tut_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Rain World randomizer on your computer.",
        "English",
        "setup_en.md",
        "setup/en",
        ["SaltySyrup"]
    )

    tutorials = [tut_en]

class RainWorld(World):
    """
    You are a nomadic slugcat, both predator and prey in a broken ecosystem.
    Grab your spear and brave the industrial wastes, hunting enough food to survive, but be wary— other,
    bigger creatures have the same plan... and slugcats look delicious.
    """
    game = "Rain World"
    options_dataclass = RainOptions
    options: RainOptions
    settings_key = "rain_settings"
    settings: ClassVar[RainSettings]
    topology_present = True

    web = RainWeb()

    item_name_to_id = {item: item_id
                       for item_id, item in enumerate(ALL_ITEMS, 1)}
    location_name_to_id = {location: location_id
                           for location_id, location in enumerate(ALL_LOCATIONS, 1)}

    item_name_groups = {
        "Gates": set(GATE_ITEMS),
        "Passages": set(PASSAGE_ITEMS),
        "Story": set(STORY_ITEMS),
        "Items": set(OBJECT_ITEMS)
    }
    location_name_groups = {
        "Passages": set(PASSAGE_LOCATIONS),
        "Echoes": set(ECHO_LOCATIONS),
        "Pearls": set(PEARL_LOCATIONS),
        # Split token dict into individual tokens
        #"SandboxTokens": set(token for token in (v for k, v in TOKEN_LOCATIONS.items())),
        "Story": {"Eat_Neuron", "Meet_LttM", "Save_LttM", "Meet_FP"}
    }

    total_karma: int = 7
    required_karma: int = 4

    def generate_early(self) -> None:
        pass

    def create_regions(self) -> None:
        menu_region = RainRegion("Menu", self.player, self.multiworld)

        # Each slugcat has a subset of locations they can reach
        relevant_locations = self.find_relevant_locations()

        all_regions = [RainRegion(name, self.player, self.multiworld) for name in ALL_REGIONS]

        for region in all_regions:
            # - Add locations to region
            region.locations = \
                [RainLocation(self.player, loc, self.location_name_to_id[loc], region)
                for loc in LOCATIONS_MAP[region.name]
                if loc in relevant_locations]

            ## Event location for Ascending
            if region.name == "SB":
                region.locations.append(RainLocation(self.player, "Ascension", None, region))

            # - Add region to multiworld
            self.multiworld.regions.append(region)

            # - Connect region through gates
            # for each connection, add an exit to region with condition matching gate item
            for gate in GATES:
                if region.name not in gate:
                    continue
                reg1, reg2 = gate
                other = reg1 if reg2 == region.name else reg2
                other_region = [reg for reg in all_regions if reg.name == other]
                entrance_name = f"Gate {reg1} {"<-" if other == reg1 else "->"} {reg2}"
                region.connect(other_region[0], entrance_name,
                               lambda state: state.has(f"GATE_{reg1}_{reg2}", self.player))

        # Add passages to menu region since they are region agnostic
        floating_locations = \
            [RainLocation(self.player, loc, self.location_name_to_id[loc], menu_region)
             for loc in PASSAGE_LOCATIONS
             if loc in relevant_locations]
        for loc in floating_locations:
            loc.progress_type = LocationProgressType.EXCLUDED

        menu_region.locations = floating_locations
        self.multiworld.regions.append(menu_region)

        # Connect to starting region
        # TODO: Add starting den randomization with weighted options menu
        starting_region: str = "SU"
        match self.options.slugcat:
            case Slugcat.option_survivor | Slugcat.option_monk:
                starting_region = "SU"
            case Slugcat.option_hunter:
                starting_region = "LF"

        menu_region.connect([item for item in all_regions if item.name == starting_region][0])


    def create_items(self) -> None:
        # Not confident in this implementation, should double-check this
        precollected = [item for item in self.multiworld.precollected_items[self.player]]
        precollected_names = [item.name for item in precollected]
        total_locations = len(self.find_relevant_locations())
        owed_filler = 0
        item_count = 0

        # - Gates
        for item in map(self.create_item, GATE_ITEMS):
            if item in precollected:
                precollected.remove(item)
                owed_filler += 1
            else:
                self.multiworld.itempool.append(item)
                item_count += 1

        # - Passages
        if self.options.passages:
            for item in map(self.create_item, PASSAGE_ITEMS):
                if item in precollected:
                    precollected.remove(item)
                    owed_filler += 1
                else:
                    self.multiworld.itempool.append(item)
                    item_count += 1

        # - Special items
        if "The Glow" not in precollected_names:
            self.multiworld.itempool.append(self.create_item("The Glow"))
            item_count += 1
        else:
            precollected.remove([item for item in precollected if item.name == "The Glow"][0])
            owed_filler += 1
        if "The Mark" not in precollected_names:
            self.multiworld.itempool.append(self.create_item("The Mark"))
            item_count += 1
        else:
            precollected.remove([item for item in precollected if item.name == "The Mark"][0])
            owed_filler += 1

        # Karma
        for i in range(self.total_karma):
            if "Karma" in precollected_names:
                precollected.remove([item for item in precollected if item.name == "Karma"][0])
                owed_filler += 1
                continue
            self.multiworld.itempool.append(self.create_item("Karma"))
            item_count += 1

        # Filler
        if item_count > total_locations:
            # Is it okay to just return here?
            # This is kind of a fatal issue
            return

        owed_filler += total_locations - item_count
        self.multiworld.itempool += [self.create_item("Object-Spear") for _ in range(owed_filler)]


    def set_rules(self) -> None:
        # TODO: Add logic for determining passage possibility
        ## Survivor: Always completable
        ## Monk: May be difficult / impossible in certain regions
        ## Hunter: May be difficult / impossible in certain regions
        ## Saint: May be difficult / impossible for hunter in certain regions
        ## Outlaw: Impossible in regions without sufficient creatures (Five Pebbles)
        ## Chieftain: Impossible in regions without scavengers
        ## Wanderer: Requires full map access
        ## Dragon Slayer: Requires access to 6 unique lizards in all available regions
        ## Friend: Impossible in regions without lizards, difficult with certain lizards
        ## Scholar: Conditions vary by slugcat
        ## Martyr: May be difficult in certain regions
        ## Nomad: Requires 4 regions connected in a line. Is every gate -> gate travel feasible in a cycle? Needs testing.
        ## Pilgrim: Requires access to every Echo region
        ## Mother: Impossible in regions where slugpups cannot spawn

        # Assign Ascension event
        ascension_loc = self.multiworld.get_location("Ascension", self.player)
        ascension_loc.place_locked_item(self.create_event("Ascension"))
        # TODO: Make ascension condition dynamic based on starting karma
        # Make ascension require karma increase to 10
        set_rule(ascension_loc, lambda state: state.has("Karma", self.player, 4))

        # TODO: Choose win condition from settings
        # Assign win condition to ascending for now
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Ascension", self.player)

        from Utils import visualize_regions
        visualize_regions(self.multiworld.get_region("Menu", self.player), "rain_world.puml")
        pass

    def write_spoiler_header(self, spoiler_handle: TextIO) -> None:
        pass

    def create_item(self, name: str) -> RainItem:
        item_id: int | None = self.item_name_to_id.get(name, None)
        return RainItem(
            name,
            self.get_item_classification(name),
            item_id,
            self.player
        )

    def create_event(self, event: str):
        return RainItem(event, ItemClassification.progression, None, self.player)

    def fill_slot_data(self) -> dict[str, Any]:
        slot_data = {
            "MSC": bool(self.options.downpour.value),
            "Slugcat": int(self.options.slugcat.value),
        }
        return slot_data

    def get_item_classification(self, name: str) -> ItemClassification:
        if name in GATE_ITEMS:
            return ItemClassification.progression
        if name in PASSAGE_ITEMS or name == "The Glow":
            return ItemClassification.skip_balancing
        if name in STORY_ITEMS:
            return ItemClassification.progression | ItemClassification.useful
        return ItemClassification.filler

    def find_relevant_locations(self) -> list[str]:
        """
        Returns all the locations that should be used based on settings
        """
        # Each slugcat has a subset of locations they can reach
        relevant_locations = ALL_LOCATIONS.copy()

        #match self.options.slugcat:
        #    case Slugcat.option_survivor:
        #        relevant_locations = SURVIVOR_LOCATIONS
        #    case Slugcat.option_monk:
        #        relevant_locations = MONK_LOCATIONS
        #    case Slugcat.option_hunter:
        #        relevant_locations = HUNTER_LOCATIONS

        # Remove locations that have been excluded by settings
        if not self.options.passages:
            relevant_locations -= PASSAGE_LOCATIONS
        if not self.options.echoes:
            relevant_locations -= ECHO_LOCATIONS
        if not self.options.pearls:
            relevant_locations -= PEARL_LOCATIONS
        if not self.options.tokens:
            relevant_locations -= TOKEN_LOCATIONS

        # Filter out locations this slugcat can't reach
        for loc, rule in SLUGCAT_RULES.items():
            if self.options.slugcat.value & rule == 0:
                print(loc)
                relevant_locations.remove(loc)

        return relevant_locations