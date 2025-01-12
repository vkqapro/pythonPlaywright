from src.locators.locators import Locators

import pytest
class BaseTest:
    locator: Locators
    @pytest.fixture(autouse=True)
    def setup(self, request):
        request.cls.locator = Locators()

