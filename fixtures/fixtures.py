import pytest
import random
import string


@pytest.fixture
def name_generator():
    length = 8
    first_name = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    last_name = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return first_name, last_name