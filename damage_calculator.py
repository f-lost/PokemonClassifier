
# matrix of type matchups as a dictionary
damage_received = {
    'Normal':
            {
            'Fighting':2.,
            'Ghost':0.,
            },
    'Fire':
            {
            'Fire':0.5,
            'Water':2,
            'Grass':0.5,
            'Ice':0.5,
            'Ground':2,
            'Bug':0.5,
            'Rock': 2,
            'Steel': 0.5,
            'Fairy': 0.5
            },
    'Water':
            {
            'Fire':0.5,
            'Water':0.5,
            'Electric': 2,
            'Grass':2,
            'Ice':0.5,
            'Ground':2,
            'Bug':0.5,
            'Rock': 2,
            'Steel': 0.5,
            'Fairy': 0.5
            },        
    'Electric':
            {
            'Electric': 0.5,
            'Ground':2,
            'Flying':.5,
            'Steel': 0.5,
            },
    'Grass':
            {
            'Fire':2,
            'Water':0.5,
            'Electric': 0.5,
            'Grass':0.5,
            'Ice':2,
            'Poison':2,
            'Ground':0.5,
            'Flying':2,
            'Bug':2,
            },
    'Ice':
            {
            'Fire':2,
            'Ice':0.5,
            'Fighting':2,
            'Poison':2,
            'Ground':.5,
            'Flying':2,
            'Bug':2,
            } ,
    'Fighting':
            {
            'Flying':2,
            'Psychic':2,
            'Bug':.5,
            'Rock':.5,
            'Dark': .5,
            'Steel': 2,
            },
    'Poison': 
            {
            'Grass':0.5,
            'Fighting':0.5,
            'Poison':0.5,
            'Ground':2,
            'Psychic':2,
            'Bug':0.5,
            'Fairy': 0.5
            },
    'Ground':
            {
            'Water':2,
            'Electric': 0,
            'Grass':2,
            'Ice':2,
            'Fighting':1,
            'Poison':0.5,
            'Ground':0.5,
            'Flying':1,
            'Psychic':1,
            'Bug':1,
            'Rock':0.5,
            'Ghost':1,
            'Dragon':1,
            'Dark': 0.5,
            'Steel': 1,
            'Fairy': 2
            },
    'Flying':
            {
            'Electric': 2,
            'Grass':0.5,
            'Ice':2,
            'Fighting':0.5,
            'Poison':1,
            'Ground':0,
            'Flying':1,
            'Psychic':1,
            'Bug':0.5,
            },
    'Psychic':
            {
            'Fighting':.5,
            'Psychic':.5,
            'Bug':2,
            'Ghost':2,
            'Dragon':1,
            'Dark': 2,
            'Steel': 1,
            'Fairy': 1},
    'Bug':
            {
            'Fire':2,
            'Grass':0.5,
            'Ice':1,
            'Fighting':0.5,
            'Poison':1,
            'Ground':0.5,
            'Flying':2,
            'Psychic':1,
            'Bug':1,
            'Rock':2,
            },
    'Rock':
            {
            'Normal':0.5,
            'Fire':0.5,
            'Water':2,
            'Electric': 1,
            'Grass':2,
            'Ice':1,
            'Fighting':2,
            'Poison':0.5,
            'Ground':2,
            'Flying':0.5,
            },
        "Ghost":
            {            
            'Normal':0,
            'Fighting':0,
            'Poison':0.5,
            'Ground':1,
            'Flying':1,
            'Psychic':1,
            'Bug':0.5,
            'Rock':1,
            'Ghost':2,
            'Dragon':1,
            'Dark': 2,
            'Steel': 1,
            'Fairy': 1},
        'Dragon':
                {
            
            'Fire':0.5,
            'Water':0.5,
            'Electric': 0.5,
            'Grass':0.5,
            'Ice':2,
            'Dragon':2,
            'Dark': 1,
            'Steel': 1,
            'Fairy': 2
                },
        'Dark': 
            {
            'Fighting':2,
            'Psychic':0,
            'Bug':2,
            'Rock':1,
            'Ghost':0.5,
            'Dragon':1,
            'Dark': 0.5,
            'Steel': 1,
            'Fairy': 0.5
                },
        "Steel": 
            {
            'Normal':0.5,
            'Fire':2,
            'Water':1,
            'Electric': 1,
            'Grass':0.5,
            'Ice':0.5,
            'Fighting':2,
            'Poison':0,
            'Ground':2,
            'Flying':0.5,
            'Psychic':0.5,
            'Bug':0.5,
            'Rock':0.5,
            'Ghost':1,
            'Dragon':0.5,
            'Dark': 1,
            'Steel': 0.5,
            'Fairy': 0.5
                },
        "Fairy": {

            'Fighting':0.5,
            'Poison':2,
            'Bug':0.5,
            'Dragon':0,
            'Dark': 0.5,
            'Steel': 2,
            'Fairy': 1
        },

    'Nessuno':
            {}
            }



def binary_damage_calculation(atk_type, def_type):
    if atk_type in damage_received[def_type].keys():
        return damage_received[def_type][atk_type]
    else:
        return 1.0

def damage_double_typing(atk_types, def_types):
    damage = 1
    for atk_type in atk_types:
        
        for def_type in def_types:
            for atk_type in atk_types:
                damage *= binary_damage_calculation(atk_type, def_type)
    return damage

def damage_between_two_pokemons(atk_pokemon, def_pokemon):
    atk_types = [atk_pokemon.type1_pred, atk_pokemon.type2]
    def_types = [def_pokemon.type1_pred, def_pokemon.type2]
    return damage_double_typing(atk_types, def_types)

