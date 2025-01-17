from worlds.rainworld.constants import TOKEN_LOCATIONS

LOCATIONS_MAP: dict[str, list[str]] = {
    "SU": [
        "Pearl-SU",
        *TOKEN_LOCATIONS["SU"]
    ],
    "HI": [
        "Pearl-HI",
        *TOKEN_LOCATIONS["HI"]
    ],
    "DS": [
        "Pearl-DS",
        *TOKEN_LOCATIONS["DS"]
    ],
    "GW": [
        "Pearl-GW",
        *TOKEN_LOCATIONS["GW"]
    ],
    "SL": [
        "Pearl-SL_bridge",
        "Pearl-SL_chimney",
        "Pearl-SL_moon",
        *TOKEN_LOCATIONS["SL"],
        "Meet_LttM",
        "Save_LttM"
    ],
    "SH": [
        "Echo-SH",
        "Pearl-SH",
        *TOKEN_LOCATIONS["SH"]
    ],
    "UW": [
        "Echo-UW",
        "Pearl-UW",
        *TOKEN_LOCATIONS["UW"]
    ],
    "SS": [
        *TOKEN_LOCATIONS["SS"],
        "Eat_Neuron",
        "Meet_FP",
    ],
    "CC": [
        "Echo-CC",
        "Pearl-CC",
        *TOKEN_LOCATIONS["CC"],
    ],
    "SI": [
        "Echo-SI",
        "Pearl-SI_top",
        "Pearl-SI_west",
        *TOKEN_LOCATIONS["SI"]
    ],
    "LF": [
        "Echo-LF",
        "Pearl-LF_west",
        "Pearl-LF_bottom",
        *TOKEN_LOCATIONS["LF"]
    ],
    "SB": [
        "Echo-SB",
        "Pearl-SB_ravine",
        "Pearl-SB_filtration",
        *TOKEN_LOCATIONS["SB"]
    ]
}

ALL_REGIONS: list[str] = [
    "SU",
    "HI",
    "DS",
    "GW",
    "SL",
    "SH",
    "UW",
    "SS",
    "CC",
    "SI",
    "LF",
    "SB"
]

GATES: list[tuple[str, str]] = [
    ("SU", "HI"),
    ("SU", "DS"),
    ("HI", "GW"),
    ("HI", "SH"),
    ("HI", "CC"),
    ("DS", "SB"),
    ("DS", "GW"),
    ("GW", "SL"),
    ("SH", "UW"),
    ("SH", "SL"),
    ("UW", "SS"),
    ("SS", "UW"),
    ("CC", "UW"),
    ("SI", "LF"),
    ("SI", "CC"),
    ("LF", "SB"),
    ("LF", "SU"),
    ("SB", "SL"),
]