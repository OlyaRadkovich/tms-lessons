import pytest
from random import randint

@pytest.fixture
def fixture_for_age():
    age = randint(1,100)
    print(f"\nRandom age is {age}")
    yield age
    print("\nDeleting random age... Done")