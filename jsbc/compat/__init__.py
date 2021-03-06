# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, division, absolute_import
import logging

logger = logging.getLogger(__name__)

__version__ = '0.0.0'
__all__ = []

try:
    basestring
except Exception:
    basestring = str
    __all__.append('basestring')

try:
    unicode
except Exception:
    unicode = str
    __all__.append('unicode')
