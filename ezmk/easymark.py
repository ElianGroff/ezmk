# easymark.py

import os
import json

from ezmk.constants import DEFAULT_CONFIG, DEFAULT_KEYS, CONFIG_FILE_NAME

# Global variables
keys = DEFAULT_KEYS
config = None

# Exposed function for binding a function to a specific key
def bind(func, key=None, **kwargs):
    global keys
    global config

    # Gets the binded function's arguments and keyword arguments from the bind() function's kwargs
    func_args = kwargs.get('args', ())
    func_kwargs = kwargs.get('kwargs', {})

    # Stores the binded function and it's arguments and keyword arguments in a list
    func_list = [func, func_args, func_kwargs]

    # If no key is provided, the binded function is set as the default bind
    if not key:
        config['default_bind'] = func_list
        return 
    
    # If a key is provided, the binded function is stored in mapped to the key
    keys["@"][key] = func_list


# Exposed function for printing text to the console
def mark(*args, **kwargs):
    global config

    interpreted_string = get_interpreted_print(*args, **kwargs)

    if not interpreted_string: return

    if config['debug']:
        print(repr(interpreted_string))

    print(interpreted_string, **kwargs)


# Loads the configuration file and overrides the default configuration
def load_config():
    global config
    config = DEFAULT_CONFIG
    config_file = CONFIG_FILE_NAME

    if os.path.exists(config_file): ##^ STINKMARK: maybe could have done better with this...
        with open(config_file) as f:
            custom_config = json.load(f)

            for key, value in custom_config.items():
                if key == "presets" and isinstance(value, dict):
                    config[key].update(value)
                elif key == "blacklist" and isinstance(value, list):
                    config[key].extend(v for v in value if v not in config[key])
                elif key == 'ping' and isinstance(value, str):
                        config[key] = value
                elif key == 'debug' and isinstance(value, bool):
                        config[key] = value

    #&Prints the config to console on import
    #&print("XX", config)


# Interprets all the arguments and returns the interpreted string
def get_interpreted_print(*args, **kwargs): 
    global config
    global keys

    if not config or not keys:
        raise RuntimeError("Configuration or keys are missing!")

    # If no arguments are provided, the ping is printed
    if not args:
        return interpret_mark(config['ping'])

    # If a default bind is set, it is executed
    if config['default_bind']:
        func, func_args, func_kwargs = config['default_bind']
        func(*func_args, **func_kwargs)

    sep = ' '
    if kwargs.get('sep'): 
        sep = kwargs.get('sep')    
    
    inter_args = ''

    # Interprets the given strings one at a time
    for arg in args:
        is_string = isinstance(arg, str)
        
        if is_string and arg and arg and not not arg.strip(): #^ ik this is goofy ahh ahh if statement
            inter_mark = interpret_mark(arg)
            #&print('XX', inter_mark)
            inter_args = f'{inter_args}\033[0m{sep}{inter_mark}'
        else:
            inter_args = f'{inter_args}{sep}{arg}'
    
    return inter_args + '\033[0m'


# Interprets the given string and returns a string with the correct modifiers prior to it and a reset escape key at the end
def interpret_mark(string) -> str: 
    global config

    # Get's a list of modifiers and the length of the activation strings
    modifiers, length = get_modifiers_from_string(string)

    # Removes the activation string from the string
    string = string[length:]

    # Adds the modifiers to the string
    for modifier in modifiers:
        string = modifier + string

    # Returns the string with the reset escape key
    return string 


# Returns a list of modifiers and the length of the activation string
def get_modifiers_from_string(string) -> tuple[list, int]:
    global keys
    global config

    modifiers = []

    # If the string starts with a activation string character, get tokens
    if string[0] in "@~^#": 
        tokens, length = get_tokens(string)
    else: # Else search for preset
        tokens, length = get_preset_tokens(string)

    # If no tokens are found, return the nothing and 0
    if not tokens:
        return [], 0

    # For each token with bind type, fire the binded function
    for bind_token in [token for token in tokens if token['type'] == '@']:
        binded_func = keys['@'][bind_token['value']]
        args = binded_func[1]
        kwargs = binded_func[2]
        
        binded_func[0](*args, **kwargs)
    
    # For each token without bind type and not in the blacklist, add the appropriate modifier
    for token in [token for token in tokens if (token['type'] != '@' and (token['type'] + token['value'] not in config["blacklist"]))]:
        #&print('XX', config["blacklist"], token)
        modifiers.append(keys[token['type']][token['value']])

    return modifiers, length


# Returns a list of tokens and the length of the activation string
def get_tokens(string) -> tuple[list, int]:
    global keys

    tokens = []

    active_token = None
    token_value = ''
    idx = 0
    last_match = None
    
    while idx < len(string):

        #Progresses variables
        cur_char = string[idx]
        token_value = token_value + cur_char
        idx += 1

        # If the current character is a valid key or a space
        if cur_char in '@~^# ':

            # If there's been a match add token
            if last_match:
                tokens.append({
                    'type': active_token, 
                    'value': last_match
                })

            # Reset variables
            token_value = ''
            active_token = cur_char

            # If the current character is a space, end search
            if cur_char == ' ':
                break

        # Else if the current value matches any of the keys, update last_match
        elif last_match := could_be(keys[active_token].keys(), token_value):
            continue

    return tokens, idx


# Searches for preset and if finds one, returnsa list of tokens and the length of the activation string
def get_preset_tokens(string) -> tuple[list, int]:
    global config

    last_matching = None
    idx = 0

    while idx < len(string):
        idx += 1
        cur_value = string[:idx]

        # If the current progressed value is a valid preset
        if cur_value in config["presets"].keys() and cur_value not in config["blacklist"]:
            last_matching = cur_value


    # If no preset was found, return None
    if not last_matching:
        return None, 0
    
    # Get the preset's activation string
    class_value = config["presets"][last_matching]

    # Get the tokens from the activation string
    tokens, _  = get_tokens(class_value + " ")

    return tokens, len(last_matching)


# Returns the first item in the list that starts with the value, else False
def could_be(list, value):
    list = sorted(list, key=len, reverse=False)

    for item in list:
        if item.startswith(value):
            return item

    return False 

