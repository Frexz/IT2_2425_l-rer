from random import randint
from math import floor

def main():
    character = {
        'name': '',
        'level': 1,
        'armor': 10,
        'hp': 0,
        'speed': 30,
        'str': 0,
        'dex': 0,
        'con': 0,
        'int': 0,
        'wis': 0,
        'cha': 0
    }

    stats = choose_stat_generation()
    assign_stats(character, stats)
    character['name'] = input('\nWhat is the name of your character?\n')
    print_sheet(character)

def print_sheet(char):
    print()
    for line in make_sheet(char):
        print(line)

def make_sheet(char):
    sheet = []
    stats = []
    sheet.append(f'{char["name"].center(49, "-")}')
    sheet.append(f'Level: {char["level"]:>42}')
    sheet.append(f'Armor Class: {char["armor"]:>36}')
    sheet.append(f'Hit Points: {char["hp"]:>37}')
    sheet.append(f'Speed: {char["speed"]:>38} ft.')
    sheet.append('-' * 49)
    sheet.append('|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |')
    sheet.append('|-------|-------|-------|-------|-------|-------|')
    stats.append(f'|{char["str"]:2} ({"+" if get_modifier(char["str"]) >= 0 else ""}{get_modifier(char["str"])})')
    stats.append(f'|{char["dex"]:2} ({"+" if get_modifier(char["dex"]) >= 0 else ""}{get_modifier(char["dex"])})')
    stats.append(f'|{char["con"]:2} ({"+" if get_modifier(char["con"]) >= 0 else ""}{get_modifier(char["con"])})')
    stats.append(f'|{char["int"]:2} ({"+" if get_modifier(char["int"]) >= 0 else ""}{get_modifier(char["int"])})')
    stats.append(f'|{char["wis"]:2} ({"+" if get_modifier(char["wis"]) >= 0 else ""}{get_modifier(char["wis"])})')
    stats.append(f'|{char["cha"]:2} ({"+" if get_modifier(char["cha"]) >= 0 else ""}{get_modifier(char["cha"])})|')
    sheet.append(''.join(stats))
    sheet.append('-' * 49)
    return sheet

def standard_array():
    return [8, 10, 12, 13, 14, 15]

def roll_stats():
    stats = []
    for i in range(6):
        rolls = [randint(1, 6) for x in range(4)]
        rolls.sort(reverse=True)
        stats.append(sum(rolls[:3]))
    return stats

def choose_stat_generation():
    print('\nWelcome to this Dungeons & Dragons Character Creator.')
    print('Please choose between standard array and random generation for generating stats'
          'for your character.')
    user_input = input('Type "standard" or "random" followed by ENTER to choose: ')

    while user_input.lower() != 'standard' and user_input.lower() != 'random':
        user_input = input('Type "standard" or "random" followed by ENTER to choose: ')

    if user_input.lower() == 'standard':
        return standard_array()
    else:
        return roll_stats()

def assign_stats(char, stats):
    abilities = ['str', 'dex', 'con', 'int', 'wis', 'cha']
    print("\nStats need to be assigned to your character's six abilities:")
    print('Strength (str), Dexterity (dex), Constitution (con), Intelligence (int), Wisdom (wis), and Charisma (cha)')

    while len(stats) > 0:
        print(f'\nStats to assign: {stats}')
        print(f'Abilities to assign to: {abilities}')
        try:
            score, ability = input('Enter the number you want to assign and the ability to assign it to, seperated by a space.'
                                'Then press ENTER:\n').split(' ')
        except ValueError:
            continue
        
        if int(score) in stats and ability.lower() in abilities:
            char[ability.lower()] = int(score)
            stats.remove(int(score))
            abilities.remove(ability.lower())
        else:
            continue
    
    char['armor'] = 10 + get_modifier(char['dex'])
    char['hp'] = 10 + get_modifier(char['con'])

def get_modifier(score):
    return floor((score - 10) / 2)


main()