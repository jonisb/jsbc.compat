# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, division, absolute_import

import unittest


class test_compat(unittest.TestCase):
    def test_compat_unicode(self):
        import sys
        if sys.version_info.major>2:  # Python 3+ don't have "unicode" string type so we import a fake one
            from jsbc.compat import unicode
            assert unicode == str
        else:  # Python <3 don't need to fake "unicode" string type
            try:
                from jsbc.compat import unicode
            except ImportError:
                pass
            else:
                assert False, "Should not be able to import unicode"

    def test_compat_basestring(self):
        import sys
        if sys.version_info.major>2:  # Python 3+ don't have "basestring" string type so we import a fake one
            from jsbc.compat import basestring
            assert basestring == str
        else:  # Python <3 don't need to fake "basestring" string type
            try:
                from jsbc.compat import basestring
            except ImportError:
                pass
            else:
                assert False, "Should not be able to import basestring"

    def test_OrderedDict(self):
        try:
            from jsbc.compat.OrderedDict import OrderedDict
        except ImportError:  # OrderedDict was added in Python 2.7
            assert False, "OrderedDict can't be imported"
        assert type == type(OrderedDict)

    def test_pickle(self):
        try:
            from jsbc.compat.pickle import pickle
        except ImportError:
            assert False, "pickle can't be imported"
        assert True

    def test_urllib_urlopen(self):
        try:
            from jsbc.compat.urllib.urlopen import urlopen
        except ImportError:
            assert False, "urlopen can't be imported"
        assert True

    def test_urllib_Request(self):
        try:
            from jsbc.compat.urllib.Request import Request
        except ImportError:
            assert False, "Request can't be imported"
        assert True

    def test_urllib_HTTPError(self):
        try:
            from jsbc.compat.urllib.HTTPError import HTTPError
        except ImportError:
            assert False, "HTTPError can't be imported"
        assert True

    def test_urllib_URLError(self):
        try:
            from jsbc.compat.urllib.URLError import URLError
        except ImportError:
            assert False, "URLError can't be imported"
        assert True