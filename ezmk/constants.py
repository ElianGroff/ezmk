# constants.py

CONFIG_FILE_NAME = "ezmk.json"

DEFAULT_CONFIG = {
    "ping" :  "#bla^m~b  ⚠︎ ⚠︎ ⚠︎   Ｍ Ａ Ｒ Ｋ   ⚠︎ ⚠︎ ⚠︎   Ｍ Ａ Ｒ Ｋ   ⚠︎ ⚠︎ ⚠︎   Ｍ Ａ Ｒ Ｋ   ⚠︎ ⚠︎ ⚠︎   Ｍ Ａ Ｒ Ｋ   ⚠︎ ⚠︎ ⚠︎   Ｍ Ａ Ｒ Ｋ   ⚠︎ ⚠︎ ⚠︎   Ｍ Ａ Ｒ Ｋ   ⚠︎ ⚠︎ ⚠︎  ",
    "default_bind" : None,
    "presets" : {
        "!" : '~b^r#y',
        "$" : '^lg#g',
        "warn " : '^y~b',
        "test " : '^m~i' ,
        "main " : '^blu#bla~u'
        # More added in configuration file.
    },
    "blacklist" : [
        # Added in configuration file.
    ]
}

DEFAULT_KEYS = {

    # Colors
    "^" : { 
        "black" : "\033[30m",
        "red" : "\033[31m",
        "green" : "\033[32m",
        "yellow" : "\033[33m",
        "blue" : "\033[34m",
        "magenta" : "\033[35m",
        "cyan" : "\033[36m",
        "white" : "\033[37m",
        "gray" : "\033[90m",
        #? Other previously used shortcuts
        #?"bla" : "\033[30m",
        #?"r" : "\033[31m",
        #?"gre" : "\033[32m",
        #?"y" : "\033[33m",
        #?"blu" : "\033[34m",
        #?"m" : "\033[35m",
        #?"c" : "\033[36m",
        #?"w" : "\033[37m",
        #?"gra" : "\033[90m",
        "light-red" : "\033[91m",
        "light-green" : "\033[92m",
        "light-yellow" : "\033[93m",
        "light-blue" : "\033[94m",
        "light-magenta" : "\033[95m",
        "light-cyan" : "\033[96m",
        "light-white" : "\033[97m",
        "lr" : "\033[91m",
        "lg" : "\033[92m",
        "ly" : "\033[93m",
        "lb" : "\033[94m",
        "lm" : "\033[95m",
        "lc" : "\033[96m",
        "lw" : "\033[97m"
    },

    # Styles
    "~" : { 
        "bold" : "\033[1m",
        "dim" : "\033[2m",
        "italic" : "\033[3m",
        "underline" : "\033[4m",
        "blink" : "\033[5m",
        "reverse" : "\033[7m",
        "hidden" : "\033[8m",
        "strikethrough" : "\033[9m"
    },

    # Backgrounds
    "#" : { 
        "black" : "\033[40m",
        "red" : "\033[41m",
        "green" : "\033[42m",
        "yellow" : "\033[43m",
        "blue" : "\033[44m",
        "magenta" : "\033[45m",
        "cyan" : "\033[46m",
        "white" : "\033[47m",
        "gray" : "\033[100m",
        #? Other previously used shortcuts
        #?"bla" : "\033[40m",
        #?"r" : "\033[41m",
        #?"gre" : "\033[42m",
        #?"y" : "\033[43m",
        #?"blu" : "\033[44m",
        #?"m" : "\033[45m",
        #?"c" : "\033[46m",
        #?"w" : "\033[47m",
        #?"gra" : "\033[100m",
        "light-red" : "\033[101m",
        "light-green" : "\033[102m",
        "light-yellow" : "\033[103m",
        "light-blue" : "\033[104m",
        "light-magenta" : "\033[105m",
        "light-cyan" : "\033[106m",
        "light-white" : "\033[107m",
        "lr" : "\033[101m",
        "lg" : "\033[102m",
        "ly" : "\033[103m",
        "lb" : "\033[104m",
        "lm" : "\033[105m",
        "lc" : "\033[106m",
        "lw" : "\033[107m"
    },

    # Functions
    "@" : { 
        # Added with the bind() function
    }
}
