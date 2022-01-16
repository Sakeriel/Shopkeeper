# Shopkeeper Main file
import random

items = {'Sword': 20, 'Shield': 10, 'Helmet': 8, 'Armor': 30, 'Gloves': 5, 'Boots': 5}
current_coin = 100
current_inventory = []

def command(cmd):
    print('What would you like to do?')
    cmd = input('> ')
    return commands[cmd]('')

def buy(cmd):
    global current_coin
    global items
    item_list = list(items.keys())
    print('What would you like to buy?')
    print(list(item_list))
    cmd = input('> ')
    if cmd in items and items[cmd] <= current_coin:
        current_inventory.append(cmd)
        current_coin -= items[cmd]
        return command('')
    elif cmd in items and items[cmd] > current_coin:
        print('Not enough coin!')
        return command('')
    else:
        print("That's not a valid item.")
        return command('')

def inventory(cmd):
    print('You currently have on hand:')
    print(current_inventory)
    return command('')

def coin(cmd):
    print(f'You currently have {current_coin} coins.')
    print()
    return command('')

def day(cmd):
    global current_coin
    sales = random.randint(0, 30)
    current_coin += sales
    print(f'You open for the day and make {sales} coin!')
    print()
    return command('')


commands = {'buy': buy, 'inventory': inventory, 'coin': coin, 'day': day}

command('')