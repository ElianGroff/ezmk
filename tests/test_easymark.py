#test_easymark.py

from ezmk import get_interpreted_print

#! The following tests are run considering the use of a ezmk.json file that should exist in tests folder
# XXX Indicates it's not being printed through the mark() function
# XX Indicates the same but that it's also being printed from the easymark.py script
# To test directly or use the debugger, use the debug_easymark.py script


# Testing mark() with increasing complexity.
def test_get_interpreted_print_without_config():

    assert get_interpreted_print('Plain Text!') == '\x1b[0m Plain Text!\x1b[0m'

    assert get_interpreted_print('    ') == '     \x1b[0m'

    assert get_interpreted_print('') == ' \x1b[0m'

    assert get_interpreted_print() == '\x1b[1m\x1b[35m\x1b[40m ⚠︎ ⚠︎ ⚠︎   Ｍ Ａ Ｒ Ｋ   ⚠︎ ⚠︎ ⚠︎   Ｍ Ａ Ｒ Ｋ   ⚠︎ ⚠︎ ⚠︎   Ｍ Ａ Ｒ Ｋ   ⚠︎ ⚠︎ ⚠︎   Ｍ Ａ Ｒ Ｋ   ⚠︎ ⚠︎ ⚠︎   Ｍ Ａ Ｒ Ｋ   ⚠︎ ⚠︎ ⚠︎   Ｍ Ａ Ｒ Ｋ   ⚠︎ ⚠︎ ⚠︎  '

    assert get_interpreted_print('#green Green background. Fullly named.') == '\x1b[0m \x1b[42mGreen background. Fullly named.\x1b[0m'
    
    assert get_interpreted_print('~hid hidden text.') == '\x1b[0m \x1b[8mhidden text.\x1b[0m'

    assert get_interpreted_print('~b#c Bold text. Shorthanded') == '\x1b[0m \x1b[46m\x1b[1mBold text. Shorthanded\x1b[0m'

    assert get_interpreted_print('prst_tst Preset: Tilted with white background and red text.') == '\x1b[0m prst_tst Preset: Tilted with white background and red text.\x1b[0m'

    assert get_interpreted_print('!Default preset.') == '\x1b[0m \x1b[43m\x1b[31m\x1b[1mDefault preset.\x1b[0m'

    assert get_interpreted_print('tesIncomplete preset.') == '\x1b[0m tesIncomplete preset.\x1b[0m'

    assert get_interpreted_print('$Configured blacklisted preset.') == '\x1b[0m \x1b[100m\x1b[92mConfigured blacklisted preset.\x1b[0m'

    assert get_interpreted_print('~u^c Cyan underlined text.') == '\x1b[0m \x1b[36m\x1b[4mCyan underlined text.\x1b[0m'

    assert get_interpreted_print('#r^bla Blacklisted red background. Black text') == '\x1b[0m \x1b[30m\x1b[41mBlacklisted red background. Black text\x1b[0m'

    assert get_interpreted_print('main main line') == '\x1b[0m \x1b[4m\x1b[40m\x1b[34mmain line\x1b[0m'

    assert get_interpreted_print('test test line') == '\x1b[0m \x1b[3m\x1b[35mtest line\x1b[0m'

    assert get_interpreted_print('warn warn line') == '\x1b[0m \x1b[1m\x1b[33mwarn line\x1b[0m'

    assert get_interpreted_print('!Alert preset with,', 'two strings?') == '\x1b[0m \x1b[43m\x1b[31m\x1b[1mAlert preset with,\x1b[0m two strings?\x1b[0m'

    assert get_interpreted_print('#m Background megenta,', 'with a', '~b bold text!') == '\x1b[0m \x1b[45mBackground megenta,\x1b[0m with a\x1b[0m \x1b[1mbold text!\x1b[0m'

    assert get_interpreted_print('test Test line with test data:', False, 'main and main dictionary:', {'key1': 'value1', 'key2': 'value2'}) == "\x1b[0m \x1b[3m\x1b[35mTest line with test data: False\x1b[0m \x1b[4m\x1b[40m\x1b[34mand main dictionary: {'key1': 'value1', 'key2': 'value2'}\x1b[0m"

    assert get_interpreted_print('#w Passing more random value types as white:', [1,2,3], len, 123412.13, ValueError) == "\x1b[0m \x1b[47mPassing more random value types as white: [1, 2, 3] <built-in function len> 123412.13 <class 'ValueError'>\x1b[0m"



'''
#! If using "ezmk_for_testing.json", use the commented-out assertions in order to test configuration overrides

def test_get_interpreted_print_with_config():
    
    assert get_interpreted_print() == "Plain text, configuration overrides default ping."

    assert get_interpreted_print('prst_tst Preset: Tilted with white background and red text.') == '\x1b[0m \x1b[31m\x1b[47m\x1b[3mPreset: Tilted with white background and red text.\x1b[0m'

    assert get_interpreted_print('$Configured blacklisted preset.') == '\x1b[0m $Configured blacklisted preset.\x1b[0m'

    assert get_interpreted_print('#r^bla Blacklisted red background. Black text') == '\x1b[0m \x1b[30mBlacklisted red background. Black text\x1b[0m'
    
'''
