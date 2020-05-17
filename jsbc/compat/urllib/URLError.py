# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, division, absolute_import
import logging

logger = logging.getLogger(__name__)

__version__ = '0.0.0'
__all__ = ["URLError"]

logger.info('Importing "URLError" module.')
try:
    from urllib.error import URLError
except ImportError:
    from urllib2 import URLError
logger.info('Importing "URLError" module, done.')
