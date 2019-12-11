ingredient_schema = {
    'properties': {
        'main_name': {'type': 'string', 'minLength': 3, 'maxLength': 50},
        'description': {'type': 'string', 'minLength': 10},
        'ingredient_type': {
            'type': 'string', 
            'enum': ['preservative','emolient','emulsifier','extract','solvent','antioxidant','consistency','chelating','fragrance','antibacterial','ph-regulator','vitamin','sunscreen','moisturizing','cleansing'],
            'minLength': 5, 
            'maxLength': 50
            },
        'natural': {'type': 'boolean'},
        'hypoallergenic': {'type': 'boolean'},
        'related_names': {
            'type': 'array',
            'items': {'type': 'string', 'minLength': 3, 'maxLength': 50},
        },
    },
    "required": [
        "main_name",
        "description",
        "ingredient_type",
        "natural",
        "hypoallergenic",
    ],
}

basic_cosmetic_schema = {
    'properties':{
        'type':{
            'type':'string',
            'enum':['hair','body','face','hands','feet'],
            'minLength':3,
            'maxLength':10
            },
        'name': {'type': 'string', 'minLength': 3, 'maxLength': 50},
        'target_gender': {
            'type:': 'string', 
            'enum':['both','female','male'],
            'minLength': 3, 
            'maxLength': 6
            },
        'description': {'type': 'string'},
        'ingredients': {
            'type': 'array',
            'items': {'type': 'string',  'maxLength': 50},
        },
        },
        "required":[
            "name",
            "type",
            "target_gender",
        ]
}

body_cosmetic_schema = {
    'properties': {
        'skin_type': {
            'type:': 'string', 
            'enum':['dehyderated','imperfections','inelastic','cellulite','sweating','sensitive'],
            'minLength': 3, 
            'maxLength': 50 
            },
        'properties': {
            'type': 'array',
            'items': {
                'type': 'string', 
                'minLength': 3, 
                'maxLength': 50, 
                'enum':['moisturizing','reviviscent','antiaging','cleansing','sunscreen'],
            },
            
        },
        'commonCosmeticData': {'type': 'object', **basic_cosmetic_schema}
    },
    "required": [
        "skin_type",
        "properties",
        "commonCosmeticData",
    ],
}

hands_feet_cosmetic_schema = {
    'properties': {
        'skin_type': {
            'type:': 'string', 
            'enum':['dry','normal','dehyderated','inelastic'],
            'minLength': 3, 
            'maxLength': 50 
            },
        'properties': {
            'type': 'array',
            'items': {
                'type': 'string', 
                'enum':['moisturizing','reviviscent','sunscreen'],
                'minLength': 3, 
                'maxLength': 50
                },
        },
        'commonCosmeticData': {'type': 'object', **basic_cosmetic_schema}
    },
    "required": [
        "skin_type",
        "properties",
        "commonCosmeticData",
    ],
}


hair_cosmetic_schema = {
    'properties': {
        'hair_type': {
            'type:': 'string', 
            'enum':['high-porosity','low-porosity','medium-porosity','all-porosity'],
            'minLength': 3, 
            'maxLength': 50
            },
        'hair_problem': {
            'type:': 'string', 
            'enum':['weak','colored','oily','dandruff','all-hair'],
            'minLength': 3, 
            'maxLength': 50
            },
        'properties': {
            'type': 'array',
            'items': {
                'type': 'string', 
                'enum':['moisturizing','reviviscent','color-protection','against-hair-loss','against-dandruff','hair-growth','smoothing','against-greasiness'],
                'minLength': 3, 
                'maxLength': 50},
        },
        'commonCosmeticData': {'type': 'object', **basic_cosmetic_schema}

    },
    "required": [
        "hair_type",
        "hair_problem",
        'properties',
        "commonCosmeticData",
    ],
}

face_cosmetic_schema = {
    'properties': {
        'skin_type': {
            'type:': 'string', 
            'enum':['dry','normal','oily','combination'],
            'minLength': 3, 
            'maxLength': 50
            },
        'skin_subtype': {
            'type:': 'string',
            'enum':['capillaries','sensitive','acne','contaminated','allergic','dehyderated','mature'], 
            'minLength': 3, 
            'maxLength': 50
            },
        'time_of_day': {'type:': 'string', 'minLength': 3, 'maxLength': 10},
        'commonCosmeticData': {'type': 'object', **basic_cosmetic_schema},
         'properties': {
            'type': 'array',
            'items': {
                'type': 'string', 
                 'enum':['moisturizing','reviviscent','antiaging','cleansing','sunscreen'],
                'minLength': 3, 
                'maxLength': 50
                },
        },
    },
    "required": [
        "skin_type",
        "skin_subtype",
        "time_of_day",
        "properties",
        "commonCosmeticData",
    ],
}

