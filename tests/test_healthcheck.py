

import pytest
import logging as log
import re
from playwright.sync_api import Page, expect

@pytest.mark.health
def test_healthcheck():
    log.info('Hello World')