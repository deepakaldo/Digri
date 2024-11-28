import pytest
from playwright.sync_api import Page, sync_playwright


@pytest.fixture(scope="function")
def set_up_tear_down_login() -> Page:
    """Fixture for setting up the login page."""
    with sync_playwright() as p:
        # Launch the browser in headed mode
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Set the viewport size and navigate to the login URL
        page.set_viewport_size({"width": 1536, "height": 800})
        page.goto("https://test.digri.ai/?callbackUrl=https%3A%2F%2Ftest.digri.ai%2Fuser%2Fdashboard")

        yield page  # Yield the page for the test to use


@pytest.fixture(scope="function")
def set_up_tear_down_logout() -> Page:
    """Fixture for setting up the logout process."""
    with sync_playwright() as p:
        # Launch the browser in headed mode
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to the login page (adjust URL as necessary)
        page.goto("https://test.digri.ai/?callbackUrl=https%3A%2F%2Ftest.digri.ai%2Fuser%2Fdashboard")

        yield page  # Yield the page for the test to use


@pytest.fixture(scope="function")
def set_up_tear_down_login_datadriven() -> Page:
    """Fixture for setting up the login page for data-driven tests."""
    with sync_playwright() as p:
        # Launch the browser in headed mode
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Set the viewport size and navigate to the login URL
        page.set_viewport_size({"width": 1536, "height": 800})
        page.goto("https://test.digri.ai/?callbackUrl=https%3A%2F%2Ftest.digri.ai%2Fuser%2Fdashboard")

        yield page  # Yield the page for the test to use
