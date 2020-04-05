"""
data_structure.py

Generate the composition file data stucture as a Python dictionary.  The dictionary may be written to a file in a
format such as toml, yaml, or json.

John Goldthorpe
04-APR-2020
"""

template = {
    "title": "",
    "stage": 8,
    "notes": [],
    "composer": {
        "composed_by": [
            "John M Goldthorpe",
        ],
        "arranged_by": [],
        "also_attributed_to": [],
        "selected_by": [],
        "jointly_composed_by": [],
        "opus": "",
        "date_composed": ""
    },
    "composition": {
        "methods": [ ],
        "start_row": 0,
        "backstroke_start": False,
        "extents": 1,
        "default_calls": "near",
        "basic": {
            # "partheads": [
            #     "13526478",
            #     "15634278",
            #     "16452378",
            #     "14263578",
            #     "12345678"
            # ],
            # "parts": 5,
            # "length": 5600,
            # "calling": [
            #     "CCC/CCCCCCC/C/CCCCCCC/CCC/CCCCCCC/YYYYYYY/"
            # ]
        },
        "rung": {
            # "partheads": [
            #     "12345678"
            # ],
            # "parts": 1,
            # "length": 5056,
            # "calling": [
            #     "CCC/CCCCCCC/C/CCCCCCC/CCC/CCCCCCC/YYYYYYY/",
            #     "CCC/CCCCCCC/C/CCCCCCC/CCC/CCCCCCC/YYYYYYY/",
            #     "CCC/CCCCCCC/C/CCCCCCC/CCC",
            #     "CCC/CCCCCCC/C/CCCCCCC/CCC/CCCCCCC/YYYYYYY/",
            #     "CCC/CCCCCCC/C/CCCCCCC/CCC/CCCCCCC/YYYYYYY/"
            # ]
        }
    },
    "display": {
        "coursehead_masks": [
            # "xxxxxxx8"
        ]
    },
    "links": {
        "first_rung": "",
        "other": []
    },
    "legacy_db": {
        "Peal No": 4,
        "Report No": 1,
        "Changes": 5184,
        "Method": "Plain Bob Major",
        "Composer Alphabetical": "Hubbard, H",
        "Composer Normal": "H Hubbard",
        "Comp No": 4,
        "Composition": "WBH/W54H",
        "Parts": 6,
        "Notes": ""
    },
    "representation": {
        "callstring": "",
        "ccf": [ ]
    },
    "checksums": { }
}


def _find_stage(stage_name):
    lookup = {'Singles': 3, 'Minimus': 4, 'Doubles': 5, 'Minor': 6, 'Triples': 7, 'Major': 8, 'Caters': 9,
              'Royal': 10, 'Cinques': 11, 'Maximus': 12, 'Sextuples': 13, 'Fourteen': 14, 'Septuples': 15, 'Sixteen': 16}
    return lookup[stage_name]


def _find_class(abbreviation):
    lookup = {'S': 'Surprise', 'D': 'Delight', 'TB': 'Treble Bob', 'A': 'Alliance', 'CB': 'Court Bob'}
    return lookup.get(abbreviation)


def _generate_composition_data(legacy_data):
    method = legacy_data['Method']
    fields = method.split()
    result = template
    result['stage'] = _find_stage(fields[-1])
    result['legacy_db'] = legacy_data
    class_type = _find_class(fields[-2])
    if class_type:
        fields[-2] = class_type
    full_method_name = ' '.join(fields)
    if not 'Spliced' in method:
        result['composition']['methods'] = [full_method_name]
    result['title'] = f"{legacy_data['Changes']} {full_method_name}"
    return result
