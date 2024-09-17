# EZMK - Easy Mark
Easy-to-use color coordinated terminal resource with simple custmization.

## Mark Key
Finish format specifications with a space like `#m^b~u working text` not like `#m ^b ~u failed text`. This doesn't apply to custom presets where if you'd like there to be a space you need to configure one with the activation string.

### Text Formmatting Effects:  **key is ~**
`bold`/`b` • `dim`/`d` • `italic`/`i` • `underline`/`u` • `blink`/`bl` • `reverse`/`r` • `hidden`/`r` • `strikethrough`/`r`

> Usage: `mark('~i~b This text is italic and bold!')`

### Text Foreground: **key is ^** and Background Colors: **key is #**
`black` • `red` • `green` • `yellow` • `blue` • `magenta` • `cyan` • `white` • `gray` • `light-red`/`lr` • `light-green`/`lg` • `light-yellow`/`ly` • `light-blue`/`lb` • `light-magenta`/`lm` • `light-cyan`/`lc` • `light-white`/`lw`

> Usage: `mark('^gre#lr This text is green with light red background!')`

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
- `blocklist` Of classes or properties that won't be printed to terminal.

## Function Binding

If you want to pass a function and bind it to a custom activation string you can use `bind(func, activation_string, args=(args), kwargs=(kwargs))` and whenever that string is fired with @ like `mark("@updategui update gui")` the function will be called. To set a function to bind to the `mark()` function itself just pass the function.

