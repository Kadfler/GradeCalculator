import pytest
from src.GradeCalculator import GradeCalculator

@pytest.fixture
def gradeCalculator():
    return GradeCalculator(0)

@pytest.fixture
def grades_factory():
    def _make_grades(*values):
        return list(values)
    return _make_grades