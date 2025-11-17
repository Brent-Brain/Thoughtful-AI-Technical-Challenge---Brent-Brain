import pytest
from package_manager import sort

def test_standard_package():
    assert sort(10, 10, 10, 5) == "STANDARD"

def test_special_heavy_package():
    assert sort(10, 10, 10, 25) == "SPECIAL"

def test_special_bulky_package():
    assert sort(200, 10, 10, 5) == "SPECIAL"

def test_rejected_package():
    assert sort(200, 10, 10, 25) == "REJECTED"

def test_invalid_dimensions():
    with pytest.raises(ValueError):
        sort(-10, 10, 10, 5)
    with pytest.raises(ValueError):
        sort(10, 0, 10, 5)
    with pytest.raises(ValueError):
        sort(10, 10, 'length', 5)
    with pytest.raises(ValueError):
        sort(10, 10, 10, -5)

def test_edge_case_heavy_threshold():
    assert sort(10, 10, 10, 20) == "SPECIAL"

def test_edge_case_bulky_threshold():
    assert sort(100, 100, 100, 5) == "SPECIAL"

def test_edge_case_dimension_threshold():
    assert sort(150, 10, 10, 5) == "SPECIAL"

def test_edge_case_rejected_threshold():
    assert sort(150, 10, 10, 20) == "REJECTED"
