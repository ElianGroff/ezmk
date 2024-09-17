# EZMK - Easy Mark
Easy-to-use color coordination terminal library with simple custmization & function binding.

Start by installing with pip:
- `pip install ezmk`

Import desired functions:
- `from ezmk import mark`
- `from ezmk import bind`

## mark(string, **kwargs)
Use the `mark()` as you would use the `print()` function but with the additional features of easy to add formatting. 

Change text color be prefixing your print statement with `^` followed by an appropriate color specialization. 

> Example `mark("^red This text is red!")` 

Use the `#` key to specify the background color, and use the `~` key to specify additional formatting such as bold, underline, or italic. You also can have colors autocomplete by using idenifying inital words like `mark("#r")`. 

You can add multiple keys but make sure to indicate the end of keys with a space like `mark("#m^b~u working text")`. Using `mark("#m ^b ~u failed text")` will only interpret the first modifier. 

#### Text Foreground and Background Colors
`black` • `red` • `green` • `yellow` • `blue` • `magenta` • `cyan` • `white` • `gray` • `light-red`/`lr` • `light-green`/`lg` • `light-yellow`/`ly` • `light-blue`/`lb` • `light-magenta`/`lm` • `light-cyan`/`lc` • `light-white`/`lw`

#### Text Style Effects
`bold`/`b` • `dim`/`d` • `italic`/`i` • `underline`/`u` • `blink`/`bl` • `reverse`/`r` • `hidden`/`r` • `strikethrough`/`r`

## Ping

Also to print a simple noticable message to the terminal simply fire the `mark()` function without any arguments.

## Presets
You can specify presets in configuration, allowing you to use an activation string to add a collection of configured modifiers to a mark statement. No space is needed to indicate the ending a preset, unless the preset contents a space. This allows very handy color coordinated printing to console:

> Example `mark("!Alert preset.")` or `mark("$Success preset.")`

## Configuration
To configure create `ezmk.cfg` file in the project directory. 

- `ping:string` What's printed to terminal when `mark()` if fired without any arguments.
- `presets:dict` Custom activation characters that repersent presetted formats. Default include:
    - `!` as `~b^r#y`
    - `$` as `^lg#g`
    - `warn` as `^y~b`
    - `test` as `^m~i`
    - `main` as `^blu#bla~u`
- `blacklist` Of classes or properties that you don't want to be interpreted.

## bind(func, activation_string, args=(args), kwargs=(kwargs)) - Function Binding

If you want to pass a function and bind it to a custom activation string you can use `bind(func, activation_string, args=(args), kwargs=(kwargs))` and whenever that string is fired with `@` like `mark("@bnd_fnc Binded function fired!")` the function will be called. To set a function to bind to the `mark()` function itself pass the function without an activation_string.

