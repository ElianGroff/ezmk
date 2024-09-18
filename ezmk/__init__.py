# __init__.py

from .easymark import load_config, mark, bind, get_interpreted_print

#&print("XXX")
load_config()

__all__ = ['mark', 'bind']
