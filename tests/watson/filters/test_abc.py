# -*- coding: utf-8 -*-
from pytest import raises
from watson.filters import abc


class TestFilterBase(object):

    def test_call_error(self):
        with raises(TypeError):
            abc.Filter()
