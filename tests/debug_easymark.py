# debug_easymark.py 
#! RUN THIS SCRIPT IN PROJECT DIRECTORY TO DIRECTLY TEST OR DEBUG EASYMARK

import sys
import os

# Adds the package root to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'ezmk')))

from ezmk import load_config, mark, bind
#? from tests import test_get_interpreted_print, test_bind


# Initiates ezmk and directly runs debug tests 
def debug():
    load_config()

    debug_mark()

    debug_bind()

    print("XXX: Debug script executed.")


# Directly run the mark function. Includes
def debug_mark():
    mark('Plain Text!')

    mark('    ')

    mark('')

    mark() 

    mark('#green Green background. Fullly named.')
    
    mark('~hid hidden text.')

    mark('~b#c Bold text. Shorthanded')
    
    mark('prst_tst Preset: Tilted with white background and red text.') #! Config dependent (check test_easymark.py)

    mark('!Default preset.')

    mark('tesIncomplete preset.')
    
    mark('$Configured blacklisted preset.') #! Config dependent (check test_easymark.py)

    mark('~u^c Cyan underlined text.')

    mark('#r^bla Blacklisted red background. Black text') #! Config dependent (check test_easymark.py)

    mark('main main line')

    mark('test test line')

    mark('warn warn line')

    mark('!Alert preset with,', 'two strings?')

    mark('#m Background megenta,', 'with a', '~b bold text!')

    mark('test Test line with test data:', False, 'main and main dictionary:', {'key1': 'value1', 'key2': 'value2'})

    mark('#w Passing more random value types as white:', [1,2,3], len, 123412.13, ValueError)


# Directly run the bind function
def debug_bind():

    # Functions for testing the bind() function 
    def bind_test():
        print("XXX BIND TRIGGERED XXX")

    def default_bind_test():
        print("XXX DEFUALT BIND TRIGGERED XXX")

    def complex_bind_test(arg1, arg2, **kwargs):
        print("XXX COMPLEX BIND TRIGGERED XXX:", arg1, arg2, kwargs)

    
    bind(bind_test, 'bd_ts')

    mark('@bd_ts Bind Trigger!')

    bind(default_bind_test)

    mark('Default Bind Trigger!')

    bind(complex_bind_test, 'cmpx_bt', args=('arg1', 'arg2'), kwargs={'kwarg1': 'kwargValue1', 'kwarg2': 'kwargValue2'})

    mark('@cmpx_bt Complex Bind Trigger!')



if __name__ == '__main__':
    debug()
