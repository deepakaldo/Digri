from digri.tests.confest import set_up_tear_down_logout
from digri.src.pages.student_logout_page import StudentLogoutPage
from digri.src.pages.student_login_page import LoginPage
from digri.src.pages.dashboard_page import DashboardPage


def test_logout_with_standard_user(set_up_tear_down_logout) -> None:
    page = set_up_tear_down_logout
    login_p = LoginPage(page)
    credentials = {'Email': 'demo0015@digri.in', 'Password': 'Colourfull@123'}
    login_p.do_login(credentials)
    # Create an instance of DashboardPage with the page object
    logout = StudentLogoutPage(page)
    # Interact with the logout dropdown and the logout option
    logout.logout_dropdown()  # Open the logout dropdown
    logout.select_dropdown_option("Logout")  # Click the logout option
    logout.confirm_logout()  # Confirm logout in popup

    # Create an instance of LoginPage to check if the login page is visible
    login_page = LoginPage(page)

    login_page.wait_for_login_button()

    # Assert that the login button (or a specific login page element) is visible
    assert login_page.login_button(), "Logout failed, Login page is not visible."


def test_cancel_logout_functionality(set_up_tear_down_logout):
    page = set_up_tear_down_logout
    login_p = LoginPage(page)
    credentials = {'Email': 'demo0015@digri.in', 'Password': 'Colourfull@123'}
    login_p.do_login(credentials)

    logout = StudentLogoutPage(page)

    # Open the logout dropdown and select the 'Logout' option
    logout.logout_dropdown()  # Open the dropdown
    logout.select_dropdown_option("Logout")  # Select the Logout option

    # Cancel the logout process
    logout.cancel_logout()  # Click the Cancel button in the popup

    dashboard= DashboardPage(page)

    # Assert that the dashboard is still visible
    assert dashboard.is_dashboard_visible()  # Ensure you're still on the dashboard
