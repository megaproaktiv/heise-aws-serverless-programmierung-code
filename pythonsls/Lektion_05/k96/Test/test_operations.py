import operations
import pytest

class TestOpsClass:

    def test_max(input_value):
        max = operations.max(input_value)
        weight = max['gramm']
        assert weight ==  98

