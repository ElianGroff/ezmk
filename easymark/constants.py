

DEFAULT_CONFIG = {
    "ping" :  """#bla^y~b ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼\n
        Ｍ ⚠︎ Ａ ⚠︎ Ｒ ⚠︎ Ｋ ⚠︎ ⚠︎ ⚠︎ Ｍ ⚠︎ Ａ ⚠︎ Ｒ ⚠︎ Ｋ ⚠︎ ⚠︎ ⚠︎ Ｍ ⚠︎ Ａ ⚠︎ Ｒ ⚠︎ Ｋ ⚠︎ ⚠︎ ⚠︎ Ｍ ⚠︎ Ａ ⚠︎ Ｒ ⚠︎ Ｋ ⚠︎ ⚠︎ ⚠︎\n
        ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲""",
    "classes" : {
        "!" : '~b^r#y',
        "$" : '^g-l#g',
        "warn " : '^y~b',
        "test " : '^m~i' ,
        "main " : '^blu#bla~u'
    },
    "blacklist" : []
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
        "red light" : "\033[91m",
        "green light" : "\033[92m",
        "yellow light" : "\033[93m",
        "blue light" : "\033[94m",
        "magenta light" : "\033[95m",
        "cyan light" : "\033[96m",
        "white light" : "\033[97m",
        "r-l" : "\033[91m",
        "g-l" : "\033[92m",
        "y-l" : "\033[93m",
        "b-l" : "\033[94m",
        "m-l" : "\033[95m",
        "c-l" : "\033[96m",
        "w-l" : "\033[97m"
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
        "red light" : "\033[101m",
        "green light" : "\033[102m",
        "yellow light" : "\033[103m",
        "blue light" : "\033[104m",
        "magenta light" : "\033[105m",
        "cyan light" : "\033[106m",
        "white light" : "\033[107m",
        "r-l" : "\033[101m",
        "g-l" : "\033[102m",
        "y-l" : "\033[103m",
        "b-l" : "\033[104m",
        "m-l" : "\033[105m",
        "c-l" : "\033[106m",
        "w-l" : "\033[107m"
    },

    # Functions
    "@" : { 
        # Added with the bind() function
    }
}
