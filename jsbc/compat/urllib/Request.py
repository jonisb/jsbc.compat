# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, division, absolute_import
import logging

logger = logging.getLogger(__name__)

__version__ = '0.0.0'
__all__ = ["Request"]

logger.info('Importing "Request" module.')
try:
    from urllib.request import Request
except ImportError:
    from urllib2 import Request
logger.info('Importing "Request" module, done.')
