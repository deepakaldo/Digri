from digri.src.pages.dashboard_page import DashboardPage


class LoginPage:
    def __init__(self, page):
        self.page = page
        self._username = page.get_by_placeholder("Email")
        self._password = page.get_by_placeholder("Password")
        self._login_btn = page.get_by_text("Login")

    def enter_username(self, u_name):
        self._username.clear()
        self._username.fill(u_name)

    def enter_password(self, p_word):
        self._password.clear()
        self._password.fill(p_word)

    def click_login(self):
        self._login_btn.click()

    def login_button(self):
        return self._login_btn.is_visible()  # Check if the login button is visible

    def wait_for_login_button(self):
        # Explicitly wait for the login button to be visible
        self.page.wait_for_selector('text=Login')

    def do_login(self, credentials):
        self.enter_username(credentials['Email'])
        self.enter_password(credentials['Password'])
        self.click_login()
        self.page.wait_for_url("https://test.digri.ai/user/dashboard")
        return DashboardPage(self.page)
