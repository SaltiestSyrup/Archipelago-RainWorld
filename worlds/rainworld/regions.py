from worlds.rainworld.constants import TOKEN_LOCATIONS

LOCATIONS_MAP: dict[str, list[str]] = {
    "Outskirts": [
        "Pearl-SU",
        *TOKEN_LOCATIONS["SU"]
    ],
    "Industrial Complex": [
        "Pearl-HI",
        *TOKEN_LOCATIONS["HI"]
    ],
    "Drainage System": [
        "Pearl-DS",
        *TOKEN_LOCATIONS["DS"]
    ],
    "Garbage Wastes": [
        "Pearl-GW",
        *TOKEN_LOCATIONS["GW"]
    ],
    "Shoreline": [
        "Pearl-SL_bridge",
        "Pearl-SL_chimney",
        "Pearl-SL_moon",
        *TOKEN_LOCATIONS["SL"],
        "Meet_LttM",
        "Save_LttM"
    ],
    "Shaded Citadel": [
        "Echo-SH",
        "Pearl-SH",
        *TOKEN_LOCATIONS["SH"]
    ],
    "The Exterior": [
        "Echo-UW",
        "Pearl-UW",
        *TOKEN_LOCATIONS["UW"]
    ],
    "Five Pebbles": [
        *TOKEN_LOCATIONS["SS"],
        "Eat_Neuron",
        "Meet_FP",
    ],
    "Chimney Canopy": [
        "Echo-CC",
        "Pearl-CC",
        *TOKEN_LOCATIONS["CC"],
    ],
    "Sky Islands": [
        "Echo-SI",
        "Pearl-SI_top",
        "Pearl-SI_west",
        *TOKEN_LOCATIONS["SI"]
    ],
    "Farm Arrays": [
        "Echo-LF",
        "Pearl-LF_west",
        "Pearl-LF_bottom",
        *TOKEN_LOCATIONS["LF"]
    ],
    "Subterranean": [
        "Echo-SB",
        "Pearl-SB_ravine",
        "Pearl-SB_filtration",
        *TOKEN_LOCATIONS["SB"]
    ]
}

ALL_REGIONS: list[str] = [
    "Outskirts",
    "Industrial Complex",
    "Drainage System",
    "Garbage Wastes",
    "Shoreline",
    "Pipeyard",
    "Shaded Citadel",
    "The Exterior",
    "Five Pebbles",
    "Chimney Canopy",
    "Sky Islands",
    "Farm Arrays",
    "Subterranean",
    "Submerged Superstructure",
    "Outer Expanse"
]

ALL_GATES: list[set[str]] = [
    {"SU", "HI"}
]