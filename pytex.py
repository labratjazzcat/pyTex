#!/usr/bin/python
from __future__ import print_function
import sys
from help_me import help_me
from expand_ptex import init as compile_me
"""
    WISH_LIST_FOR_GUI:
        - ability to add packages (", ".join[:-2])
        - optional date override
        - optional make title (author)
        - add / remove micro-expression definition

"""


if sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print(help_me())
else:
    compile_me(sys.argv[1])
