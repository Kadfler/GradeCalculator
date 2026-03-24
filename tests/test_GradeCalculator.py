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
    assert str(exc_info.value) == "Points must be a number between 0 and 100"

def test_IsPassed_ab_returns_TypeError(gradeCalculator):
    result = gradeCalculator.is_passed('ab')
    assert result == TypeError

def test_get_average_67_and_42_returns_54and5(gradeCalculator, grades_factory):
    points_list = grades_factory(67, 42)
    result = gradeCalculator.get_average(points_list)
    assert result == 54.5

def test_get_average_67_returns_67(gradeCalculator, grades_factory):
    points_list = grades_factory(67)
    result = gradeCalculator.get_average(points_list)
    assert result == 67

def test_get_average_none_returns_ZeroDivisionError(gradeCalculator, grades_factory):
    points_list = grades_factory()
    with pytest.raises(ZeroDivisionError) as exc_info:
        gradeCalculator.get_average(points_list)
    assert str(exc_info.value) == "Points list cannot be empty"

def test_get_average_minus1_and_zero_returns_ValueError(gradeCalculator, grades_factory):
    points_list = grades_factory(-1, 0)
    with pytest.raises(ValueError) as exc_info:
        gradeCalculator.get_average(points_list)
    assert str(exc_info.value) == "Points cannot be negative"

def test_get_average_ab_and_zero_returns_TypeError(gradeCalculator, grades_factory):
    points_list = grades_factory('ab', 0)
    result = gradeCalculator.get_average(points_list)
    assert result == TypeError