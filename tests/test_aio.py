import pytest

from boken.aio import kraken
from boken.model import time

"""
Async tests

TODO : generate these from sync tests (simpler to manage)
"""



@pytest.mark.vcr
@pytest.mark.asyncio
async def test_time():
    response = await kraken.get_time()
    print(response)
    assert isinstance(response, time.Time)


if __name__ == '__main__':
    pytest.main(['-s', __file__])
