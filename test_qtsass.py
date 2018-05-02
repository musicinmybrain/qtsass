# -*- coding: utf-8 -*-
from __future__ import absolute_import
import unittest
from textwrap import dedent
from qtsass.qtsass import NotConformer, QLinearGradientConformer


class TestNotConformer(unittest.TestCase):

    qss_str = "QAbstractItemView::item:!active"
    css_str = "QAbstractItemView::item:_qnot_active"

    def test_conform_to_css(self):
        """NotConformer qss to css"""

        c = NotConformer()
        self.assertEqual(c.to_css(self.qss_str), self.css_str)

    def test_conform_to_qss(self):
        """NotConformer css to qss"""

        c = NotConformer()
        self.assertEqual(c.to_qss(self.css_str), self.qss_str)

    def test_round_trip(self):
        """NotConformer roundtrip"""

        c = NotConformer()
        conformed_css = c.to_css(self.qss_str)
        self.assertEqual(c.to_qss(conformed_css), self.qss_str)


class TestQLinearGradientConformer(unittest.TestCase):

    css_str = "qlineargradient(0, 0, 0, 0, (0 red, 1 blue))"
    css_nostops_str = "qlineargradient(0, 0, 0, 0)"
    qss_nostops_str = "qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0)"
    qss_singleline_str = (
        "qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0, "
        "stop: 0 red, stop: 1 blue)"
    )
    qss_multiline_str = dedent("""
    qlineargradient(
        x1: 0,
        y1: 0,
        x2: 0,
        y2: 0,
        stop: 0 red,
        stop: 1 blue
    )
    """).strip()
    qss_weird_whitespace_str = (
        "qlineargradient( x1: 0, y1:0, x2: 0, y2:0, "
        "   stop:0 red, stop: 1 blue )"
    )

    def test_does_not_affect_css_form(self):
        """QLinearGradientConformer does not affect css qlineargradient func"""

        c = QLinearGradientConformer()
        self.assertEqual(c.to_css(self.css_str), self.css_str)
        self.assertEqual(c.to_qss(self.css_str), self.css_str)

    def test_conform_singleline_str(self):
        """QLinearGradientConformer singleline qss to css"""

        c = QLinearGradientConformer()
        self.assertEqual(c.to_css(self.qss_singleline_str), self.css_str)

    def test_conform_multiline_str(self):
        """QLinearGradientConformer multiline qss to css"""

        c = QLinearGradientConformer()
        self.assertEqual(c.to_css(self.qss_multiline_str), self.css_str)

    def test_conform_weird_whitespace_str(self):
        """QLinearGradientConformer weird whitespace qss to css"""

        c = QLinearGradientConformer()
        self.assertEqual(c.to_css(self.qss_weird_whitespace_str), self.css_str)

    def test_conform_nostops_str(self):
        """QLinearGradientConformer qss with no stops to css"""

        c = QLinearGradientConformer()
        self.assertEqual(c.to_css(self.qss_nostops_str), self.css_nostops_str)


if __name__ == '__main__':
    unittest.main()
