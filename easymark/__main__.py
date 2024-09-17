import os
import configparser

from constants import DEFAULT_CONFIG, DEFAULT_KEYS

# Global Variables
keys = DEFAULT_KEYS
config = None

def bind(func, key='!'):
    global keys
    keys["functions"][key] = func

#! SERIOUSLY NEEDS A LOT OF WORK BEFORE IT WORKSH


def mark(*args, **kwargs): 
    global config

    if not config:
        config = load_config()

    if not args and not kwargs:
        ping()

    args.map(lambda string: interpret_mark(string))
    
    print(*args, **kwargs)
    

def load_config():
    global config
    config = DEFAULT_CONFIG
    config_file = "ezmk.cfg"

    if os.path.exists(config_file):
        parser = configparser.ConfigParser()
        parser.read(config_file)

        for section in parser.sections():
            for option in parser.options(section):
                keys[section][option] = parser.get(section, option)


def ping():
    global ping
    mark = interpret_mark(ping)
    print(mark) 


def interpret_mark(string): 
    global config

    modifiers, length = get_modifiers_from_string(string)

    for modifier in modifiers:
        string = modifier + string

    return string[length:] + f"\033[0m"


def get_modifiers_from_string(string):
    global keys
    global config

    modifiers = []

    if string[0] in "@~^#":
        tokens, length = get_tokens(string)
    else:
        tokens, length = get_preset_tokens(string)

    tokens = get_tokens(string)
    revered_tokens = tokens[::-1]

    for token in revered_tokens:
        if revered_tokens.count(token) > 1:
            revered_tokens.remove(token)

    for token in revered_tokens:
        if token in config["blacklist"]:
            revered_tokens.remove(token)
            continue
        
        if token['type'] == '@':
            keys['@'][token['value']]()

        modifiers.append(keys[token['type']][token['value']])

    return modifiers, length


def get_tokens(string):
    global keys

    tokens = []

    active_token = None
    token_value = ''
    idx = 0
    last_matching = None
    seek_next = False
    
    while idx < len(string):
        cur_char = string[idx]
        
        if seek_next and cur_char not in "@~^#":
            idx += 1
            continue

        if not active_token:
            if cur_char in "@~^#":
                active_token = cur_char
                continue
            break

        if last_matching := could_be(keys[active_token].keys(), token_value):
            token_value += cur_char
            idx += 1
            continue
        elif last_matching:
            tokens.append({
                'type': active_token, 
                'value': last_matching
            })
            token_value = ''
            seek_next = True
        else:
            seek_next = True


def get_preset_tokens(string):
    global keys
    global config

    last_matching = None
    idx = 0

    while last_matching := could_be(config["presets"], string[:idx]):
        idx += 1

    if not last_matching:
        return None
    
    class_value = config["presets"][last_matching]
    tokens = get_tokens(class_value)

    return tokens


def could_be(list, value):
    list.sort(key=len, reverse=True)

    for item in list:
        if item.startswith(value):
            return item

    return False 
