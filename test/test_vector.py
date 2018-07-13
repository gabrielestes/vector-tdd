from src.vector import Vector

def test_make_vector():
    v = Vector([1,2,3])
    assert len(v.nums) == 3

def test_dimensions():
    v = Vector([1, 2, 3])
    assert v.dims == len([1,2,3])

def test_norm():
    v = Vector([3,4])
    assert v.norm == 5

def test_unit_vector():
    v = Vector([1,2,3])
    assert v.unit_vector().norm == 1.0

def test_scale():
    v = Vector([1,2,3])
    assert v.scale(3) == Vector([3,6,9])
