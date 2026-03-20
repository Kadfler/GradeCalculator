import pytest
from src.GradeCalculator import GradeCalculator
from conftest import *

def test_getGrade_100_returns_A(gradeCalculator):
    result = gradeCalculator.getGrade(100)
    assert result == 'A'

def test_getGrade_0_returns_F(gradeCalculator):
    result = gradeCalculator.getGrade(0)
    assert result == 'F'

def test_getGrade_minus1_returns_ValueError(gradeCalculator):
    result = gradeCalculator.getGrade(-1)
    assert result == GradeCalculator.ValueError

def test_getGrade_ab_returns_ValueError(gradeCalculator):
    result = gradeCalculator.getGrade('ab')
    assert result == GradeCalculator.ValueError