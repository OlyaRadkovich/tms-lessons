import pytest


class TestHomework:
    @pytest.mark.wizard
    @pytest.mark.parametrize("first_name", ["John", "Harry", "Ron"])
    @pytest.mark.parametrize("last_name", ["Smith", "Weasly", "Potter"])
    def test_fail_if_john_smith(self, first_name, last_name, fixture_for_age):
        print(f"\nHello, {first_name} {last_name}! Your age is {fixture_for_age}.")
        if first_name == "John" and last_name == "Smith":
            pytest.xfail("Muggle")