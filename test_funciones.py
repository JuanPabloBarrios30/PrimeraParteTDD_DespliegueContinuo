from min_val_array import min_val

def test_min_val():
    assert min_val([2, 3, 4, 6]) == 2
    assert min_val([-1, 10, 5, 7]) == -1
    assert min_val([0.001, 1, 2, 100]) == 0.001