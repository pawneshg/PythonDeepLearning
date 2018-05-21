# -*- coding: utf-8 -*-
"""
Created on Mon May 21 18:30:29 2018

@author: admin
"""

import unittest
from mock import MagicMock
from exMock import ProductionClass

def test_user_api():
    inst = ProductionClass()
    inst._internal_api_one = MagicMock()
    inst._internal_api_two = MagicMock()
    inst.user_api(2, True)
    inst._internal_api_one.assert_called_once_with(2)
    inst.user_api(2, True)
    inst._internal_api_two.assert_called_once_with(2)
    
    
# =============================================================================
#     with mock.patch.object(inst, '_internal_api_one',
#                            wraps=inst._internal_api_one) as monkey:
#         inst.user_api('foo', b=True)
#         monkey.assert_called_with('foo')
#     
#     with mock.patch.object(inst, '_internal_api_two',
#                            wraps=inst._internal_api_two) as monkey:
#         inst.user_api('bar', b=False)
#         monkey.assert_called_with('bar')
# ============================================================================