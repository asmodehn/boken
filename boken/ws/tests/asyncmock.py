import unittest.mock


def AsyncMock(*args, **kwargs):
    """ A mock object for async functions / coroutines
    Ref : https://blog.miguelgrinberg.com/post/unit-testing-asyncio-code
    >>> import asyncio
    >>> f = AsyncMock(return_value='hello!')
    >>> f('foo', 'bar')  # doctest:+ELLIPSIS
    <coroutine object AsyncMock.<locals>.mock_coro at ...>
    >>> asyncio.get_event_loop().run_until_complete(f('foo', 'bar'))
    'hello!'
    >>> f.mock.assert_called_once_with('foo', 'bar')
    >>> f.mock.assert_called_once_with('foo')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File ".../unittest/mock.py", line 825, in assert_called_once_with
        return self.assert_called_with(*args, **kwargs)
      File ".../unittest/mock.py", line 814, in assert_called_with
        raise AssertionError(_error_message()) from cause
    AssertionError: Expected call: mock('foo')
    Actual call: mock('foo', 'bar')
    """

    m = unittest.mock.MagicMock(*args, **kwargs)

    async def mock_coro(*args, **kwargs):
        return m(*args, **kwargs)

    mock_coro.mock = m
    return mock_coro


if __name__ == '__main__':
    import doctest
    doctest.testmod()