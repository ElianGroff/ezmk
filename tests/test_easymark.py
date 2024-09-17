
#test_easymark.py

from ezmk import mark, bind

#! The following tests are run considering the use of a ezmk.json file that should exist in tests folder
# XXX Indicates it's not being printed through the mark() function
# XX Indicates the same but that it's also being printed from the easymark.py script


# Functions for testing the bind() function 
def bind_test():
    print("XXX BIND TRIGGERED XXX")

def default_bind_test():
    print("XXX DEFUALT BIND TRIGGERED XXX")

def complex_bind_test(arg1, arg2, **kwargs):
    print("XXX COMPLEX BIND TRIGGERED XXX:", arg1, arg2, kwargs)


# Testing mark() with increasing complexity.
def test_mark():
    mark('Plain Text!')

    mark() # PPPINGGG!!!! Plain text, configuration overrides.

    mark('#green Green background. Fullly named.')
    
    mark('~hid hidden text.')

    mark('~b#c Bold text. Shorthanded')

    mark('prst_tst Preset: Tilted with white background and red text.')

    mark('!Default preset.')

    mark('$Blacklisted preset.')

    mark('~u^c Blacklisted underlined.')

    mark('#r^bla Blacklisted red background. Black text')

    mark('main main line')

    mark('test test line')

    mark('warn warn line')


# Testing bind() with increasing complexity.
def test_bind():
    bind(bind_test, 'bd_ts')

    mark('@bd_ts Bind Trigger!')

    bind(default_bind_test)

    mark('Default Bind Trigger!')

    bind(complex_bind_test, 'cmpx_bt', args=('arg1', 'arg2'), kwargs={'kwarg1': 'kwargValue1', 'kwarg2': 'kwargValue2'})

    mark('@cmpx_bt Complex Bind Trigger!')

