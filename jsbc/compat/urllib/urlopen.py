# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, division, absolute_import
import logging

logger = logging.getLogger(__name__)

__version__ = '0.0.0'
__all__ = ["urlopen"]

logger.info('Importing "urlopen" module.')
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
logger.info('Importing "urlopen" module, done.')
