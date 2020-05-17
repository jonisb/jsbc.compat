# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, division, absolute_import
import logging

logger = logging.getLogger(__name__)

__version__ = '0.0.0'
__all__ = ["pickle"]

logger.info('Importing "pickle" module.')
try:
    import cPickle as pickle
except ImportError:
    import pickle
logger.info('Importing "pickle" module, done.')
