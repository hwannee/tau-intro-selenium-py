"""
These tests cover DuckDuckGo searches.
"""
import pytest
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

@pytest.mark.parametrize('phrase', ['panda','python','polar bear'])
def test_basic_duckduckgo_search(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    # PHRASE = 'panda'
    PHRASE = phrase

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for "panda"
    search_page.search(PHRASE)

    # Then the search result title contains "panda"
    # from selenium.webdriver.support.ui import WebDriverWait
    # from selenium.webdriver.support import expected_conditions as EC
    # WebDriverWait(browser.b, 10).until(EC.title_contains(PHRASE))

    # assert PHRASE in result_page.title()

    # And the search result query is "panda"
    assert PHRASE == result_page.search_input_value()

    # And the search result links pertain to "panda"
    for title in result_page.result_link_titles():
        assert PHRASE.lower() in title.lower()

    # TODO: Remove this exception once the test is complete
    # raise Exception("Incomplete Test")

    assert PHRASE in result_page.title()
