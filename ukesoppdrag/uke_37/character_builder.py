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

def print_sheet(char):
    for line in make_sheet(char):
        print(line)

def make_sheet(char):
    sheet = []
    stats = []
    sheet.append(f'{char["name"].center(49, "_")}')
    sheet.append(f'Level: {char["level"]:>42}')
    sheet.append(f'Armor Class: {char["armor"]:>36}')
    sheet.append(f'Hit Points: {char["hp"]:>37}')
    sheet.append(f'Speed: {char["speed"]:>38} ft.')
    sheet.append('-' * 49)
    sheet.append('|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |')
    sheet.append('|-------|-------|-------|-------|-------|-------|')
    stats.append(f'|{char["str"]:2} ({"+" if (char["str"] - 10) / 2 >= 0 else ""}{(floor((char["str"] - 10) / 2))})')
    stats.append(f'|{char["dex"]:2} ({"+" if (char["dex"] - 10) / 2 >= 0 else ""}{(floor((char["dex"] - 10) / 2))})')
    stats.append(f'|{char["con"]:2} ({"+" if (char["con"] - 10) / 2 >= 0 else ""}{(floor((char["con"] - 10) / 2))})')
    stats.append(f'|{char["int"]:2} ({"+" if (char["int"] - 10) / 2 >= 0 else ""}{(floor((char["int"] - 10) / 2))})')
    stats.append(f'|{char["wis"]:2} ({"+" if (char["wis"] - 10) / 2 >= 0 else ""}{(floor((char["wis"] - 10) / 2))})')
    stats.append(f'|{char["cha"]:2} ({"+" if (char["cha"] - 10) / 2 >= 0 else ""}{(floor((char["cha"] - 10) / 2))})|')
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
    print(f'Your stats are: {stats}')

main()