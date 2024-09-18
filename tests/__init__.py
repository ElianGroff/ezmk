# tests/__init__.py

from .test_easymark import test_get_interpreted_print_without_config 

__all__ = [ 'test_get_interpreted_print_without_config'] 

'''
#!If using "ezmk_for_testing.json", use the commented-out assertions in order to test configuration overrides

from .test_easymark import test_get_interpreted_print_with_config

__all__ = [ 'test_get_interpreted_print_with_config']
'''