# Easy Mark (ezmk)
Easy-to-use color coordination terminal library with simple custmization & function binding.

Use now with `pip install ezmk`

## mark(string, **kwargs)
Use the `mark()` as you would use the `print()` function but with the additional features of easy-to-add format modification. 

Modify text color by prefixing your statement with `^`, followed by an appropriate color specification. 

> Example `mark("^red This text is red!")` 

Use the `#` key to specify the background color, and use the `~` key to specify styling such as bold, underline, or italic. Colors and styles autocomplete if identifying initial words are used like `mark("#r This text is also red!")`. 

You can add multiple modifiers if you indicate their end with a space like `mark("#m^b~u working text!")`. Using `mark("#m ^b ~u failed text!")` will only interpret the first modifier. 

To print a simple and noticeable message to the console simply fire the `mark()` function without arguments.

#### Text Foreground and Background Colors
`black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`, `gray`, `light-red`/`lr`, `light-green`/`lg`, `light-yellow`/`ly`, `light-blue`/`lb`, `light-magenta`/`lm`, `light-cyan`/`lc`, `light-white`/`lw`

#### Text Style Effects
`bold`/`b`, `dim`/`d`, `italic`/`i`, `underline`/`u`, `blink`/`bl`, `reverse`/`r`, `hidden`/`r`, `strikethrough`/`r`

## bind(func, activation_string, args=(args), kwargs=(kwargs))

To pass a function and bind it to a custom key you can use `bind()`. When the key is used following the bind character: `@` like `mark("@bnd_fnc Binded function fired!")` the function will be called. 

To set a function to bind to the `mark()` function itself pass the function without a key.

## Presets
You can specify presets in configuration, allowing you to use a key(activation string) to add a collection of modifiers to a statement. No space is needed to indicate a preset's ending unless the preset contents a space itself. This enables very handy color-coordinated printing to the console:

> Example `mark("!Alert preset.")` or `mark("$Success preset.")` (using default presets.)

## Configuration
To configure, create `ezmk.cfg` file in the project directory. 

- `ping:string` What's printed to the console when `mark()` when fired without any arguments.
- `debug:bool` If set to true, print's to terminal the raw interpretation of each mark statement.
- `presets:dict` Custom keys that load configured format modifiers. Defaults include(to change default either override or list in blacklist):
    - `!` as `~b^r#y`
    - `$` as `^lg#g`
    - `warn` as `^y~b`
    - `test` as `^m~i`
    - `main` as `^blu#bla~u`
- `blacklist` Presets or modifiers that don't get interpreted.

