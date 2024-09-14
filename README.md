# easymark
Easy-to-use color coordinated terminal debug/testing resource with simple custmization.


i should learn to use the standard debugger but my program makes it very hard to use. also 

### ideas:
- easy color marks with `mk('@r red')`
    - autocompletes customized words
    - @ is color
    - !is background color
    - ^ is bold
    - / is italisized
    - & for special functions
- stack resolution:
    - indents matching the stack
    - manually with + or -
    - or by checking the call stack
- snapshots
    - timestamped snapshots of certain data while things happen
    - can be turned on or off
    - can happen at set interval or with `mk.snp()`
- auto formats
    - lists as lists
    - use `&s` for removing \n special function
