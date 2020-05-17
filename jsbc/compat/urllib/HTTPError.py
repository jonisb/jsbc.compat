# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, division, absolute_import
import logging

logger = logging.getLogger(__name__)

__version__ = '0.0.0'
__all__ = ["HTTPError"]

logger.info('Importing "HTTPError" module.')
try:
    from urllib.error import HTTPError
except ImportError:
    from urllib2 import HTTPError
logger.info('Importing "HTTPError" module, done.')