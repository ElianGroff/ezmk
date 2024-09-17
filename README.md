# EZMK - Easy Mark
Easy-to-use color coordinated terminal resource with simple custmization.

## Mark Key

### Text Formmatting Effects (**~**)
`bold`/`b` ● `dim`/`d` ● `italic`/`i` ● `underline`/`u` ● `blink`/`bl` ● `reverse`/`r` ● `hidden`/`r` ● `strikethrough`/`r`

> Usage: `mark('~i~b This text is italic and bold!')`

### Text Foreground(**^**) and Background Colors(**~**)
`black`/`bla` ● `red`/`r` ● `green`/`gre` ● `yellow`/`y` ● `blue`/`blu` ● `magenta`/`m` ● `cyan`/`c` ● `white`/`w` ● `gray`/`gra` ● `red light`/`r-l` ● `green light`/`g-l` ● `yellow light`/`y-l` ● `blue light`/`b-l` ● `magenta light`/`m-l` ● `cyan light`/`c-l` ● `white light`/`w-l`

> Usage: `mark('^green #r-l This text is green with light red background!')`

## Configuration

To configure create `ezmk.cfg` file in the project directory. 

- `ping:string` What's printed to terminal when `mark()` if fired without any arguments.
- `presets:dict` Custom activation characters that repersent presetted formats. Default include:
    - `!` as `~b^r#y`
    - `$` as `^g-l#g`
    - `warn` as `^y~b`
    - `test` as `^m~i`
    - `main` as `^blu#bla~u`
- `blacklist` Of classes or properties that you don't want to be executed.

## Function Binding

If you want to pass a function and bind it to a custom activation string you can use `bind(func, activation_string, args=(args), kwargs=(kwargs))` and whenever that string is fired with @ like `mark("@updategui update gui")` the function will be called. To set a function to bind to the `mark()` function itself just pass the function.

