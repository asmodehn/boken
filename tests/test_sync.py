import pytest

from boken.sync import kraken

from boken.model import time

@pytest.mark.vcr()
def test_time():
    response = kraken.get_time()
    print(response)
    assert isinstance(response, time.Time)


if __name__ == '__main__':
    pytest.main(['-s', __file__])
