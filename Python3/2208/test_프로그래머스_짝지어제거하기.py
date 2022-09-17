from unittest import TestCase
from 프로그래머스_짝지어제거하기 import solution
class Test(TestCase):
    def test_case1(self):
        assert 1 == solution("baabaa")
    def test_case2(self):
        assert 0 == solution("cdcd")



