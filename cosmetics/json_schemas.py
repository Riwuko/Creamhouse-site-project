ingredient_schema = {
    'properties': {
        'main_name': {'type': 'string', 'minLength': 3, 'maxLength': 50},
        'description': {'type': 'string', 'minLength': 10},
        'ingredient_type': {'type:': 'string', 'minLength': 5, 'maxLength': 50},
        'natural': {'type': 'boolean'},
        'hypoallergenic': {'type': 'boolean'},
        'related_names': {
            'type': 'array',
            'items': {'type': 'string', 'minLength': 3, 'maxLength': 50},
        },
    },
    "required": [
        "type",
        "main_name",
        "description",
        "ingredient_type",
        "natural",
        "hypoallergenic",
    ],
}

basic_cosmetic_schema = {
    'properties':{
        'type':{'type':'string','minLength':3,'maxLength':10},
        'name': {'type': 'string', 'minLength': 3, 'maxLength': 50},
        'target_gender': {'type:': 'string', 'minLength': 3, 'maxLength': 6},
        'properties': {
            'type': 'array',
            'items': {'type': 'string', 'minLength': 3, 'maxLength': 50},
        },
        'description': {'type': 'string'},
        'ingredients': {
            'type': 'array',
            'items': {'type': 'string', 'minLength': 3, 'maxLength': 50},
        },
        },
        "required":[
            "name",
            "type",
            "target_gender",
            "properties",
        ]
}

body_hands_feet_cosmetic_schema = {
    'properties': {
        'skin_type': {'type:': 'string', 'minLength': 3, 'maxLength': 50},
        'commonCosmeticData': {'type': 'object', **basic_cosmetic_schema}
    },
    "required": [
        "skin_type",
        "commonCosmeticData",
    ],
}

hair_cosmetic_schema = {
    'properties': {
        'hair_type': {'type:': 'string', 'minLength': 3, 'maxLength': 50},
        'hair_problem': {'type:': 'string', 'minLength': 3, 'maxLength': 50},
        'commonCosmeticData': {'type': 'object', **basic_cosmetic_schema}

    },
    "required": [
        "hair_type",
        "hair_problem",
        "commonCosmeticData",
    ],
}

face_cosmetic_schema = {
    'properties': {
        'skin_type': {'type:': 'string', 'minLength': 3, 'maxLength': 50},
        'skin_subtype': {'type:': 'string', 'minLength': 3, 'maxLength': 50},
        'time_of_day': {'type:': 'string', 'minLength': 3, 'maxLength': 10},
        'commonCosmeticData': {'type': 'object', **basic_cosmetic_schema},
    },
    "required": [
        "skin_type",
        "skin_subtype",
        "time_of_day",
        "commonCosmeticData",
    ],
}

