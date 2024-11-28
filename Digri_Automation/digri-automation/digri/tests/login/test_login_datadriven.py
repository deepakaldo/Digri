import pytest
from digri.src.pages.dashboard_page import DashboardPage
from digri.tests.utils import read_excel
from digri.src.pages.student_login_page import LoginPage
from digri.tests.confest import set_up_tear_down_login_datadriven


@pytest.mark.parametrize("credentials", read_excel("C://Users//Deepak//Downloads//DigriLogin.xlsx", "Digri"))
def test_login_credentials(set_up_tear_down_login_datadriven, credentials):
    page = set_up_tear_down_login_datadriven
    login_page = LoginPage(page)
    login_page.do_login(credentials)
    dashboard = DashboardPage(page)
    assert dashboard.is_dashboard_visible()