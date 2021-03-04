import pytest

def extract_position(line):
    if not line:
        pos = None
    else:
        if 'debug' in line or 'error' in line:
            pos = None
        else:
            if 'x:' in line:
                start_index = line.find('x:') + 2
                pos = line[start_index:] # from start_index to the end.
            else: 
                pos = None
    return pos

@pytest.fixture
def average():
    return "|update| the positron location in the particle accelerator is x:21.432"

@pytest.fixture
def null():
    return None

@pytest.fixture
def error():
    return "|error| numerical calculations could not converge."

def test_extract_positio_average(average):
    assert extract_position(average) == "21.432"

