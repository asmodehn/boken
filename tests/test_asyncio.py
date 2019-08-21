import pytest

from boken.asyncio import kraken


@pytest.mark.asyncio
@pytest.mark.vcr
async def test_time():
    response = await kraken.get_time()
    print(response)
    # asserting structure (but marshmallow could do it)
    assert not response.get('error')
    assert response.get('result').get('rfc1123')
    assert response.get('result').get('unixtime')


if __name__ == '__main__':
    pytest.main(['-s', __file__])
