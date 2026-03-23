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
    assert result == ValueError

def test_getGrade_ab_returns_ValueError(gradeCalculator):
    result = gradeCalculator.getGrade('ab')
    assert result == TypeError

def test_IsPassed_100_returns_True(gradeCalculator):
    result = gradeCalculator.is_passed(100)
    assert result == True

def test_IsPassed_45_returns_False(gradeCalculator):
    result = gradeCalculator.is_passed(45)
    assert result == False

def test_IsPassed_minus1_returns_ValueError(gradeCalculator):
    with pytest.raises(ValueError) as exc_info:
        gradeCalculator.is_passed(-1)
        exc_info == ValueError


def test_IsPassed_ab_returns_TypeError(gradeCalculator):
    result = gradeCalculator.is_passed('ab')
    assert result == TypeError

