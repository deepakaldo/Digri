class DigitalProfile:
    def __init__(self, page):
        self.page = page

        # Standards & Skills
        self._digital_profile_tab = page.locator("//div[contains(text(),'Digital Profile')]")
        self._foundation_skills = page.locator("//div[contains(@class,'flex flex-row w-full h-[4rem] p-2 bg-white "
                                               "mr-2 text-xs font-semibold  text-[#85878D] rounded-lg leading-["
                                               "2.2rem] items-center justify-between shadow-sm')]")
        self._projects_summary = page.locator("//div[contains(@class,'flex lg:gap-4 bg-[#EFF6FF] lg:w-full md:w-["
                                              "355px] lg:h-[100px] md:h-[80px] sm:h-[80px] md:gap-4 sm:gap-2  sm:px-4 "
                                              "justify-between items-center lg:p-4 md:p-3 md:pt-4 lg:rounded-b-lg "
                                              "sm:rounded-b-lg md:rounded-lg')]")
        self._project_details1 = page.locator("//div[contains(@class,' w-full lg:h-[150px] md:h-[125px] border-[1px] "
                                              "border-[#9595951C] bg-[#F5F7F9] rounded-lg sm:py-2')]")
        self._project_details2 = page.locator("//div[contains(@class,'flex flex-row  w-full h-[40px] items-center "
                                              "rounded-md border border-[#E8EAEE] justify-between pl-6 ')]")
        self._previous_project_button = page.locator("//div[contains(@class,'w-[32px] h-[32px] border-[1px] "
                                                     "rounded-lg flex items-center justify-center opacity-30')]")
        self._next_project_button = page.locator("//div[contains(@class,'w-[32px] h-[32px] border-[1px] rounded-lg "
                                                 "flex items-center justify-center rotate-180 opacity-30')]")

        # Problem Solving
        self._problem_solving_tab = page.locator(
            "(//div[contains(@class,'flex flex-row items-center justify-center lg:gap-4 md:gap-1 sm:gap-1')])[1]")
        self._practice_stats = page.locator("//div[contains(@class,'h-[13.75rem] overflow-y-auto pr-12 flex "
                                            "items-center justify-center pt-3')]")
        self._practice_details = page.locator("//div[contains(@class,'p-[1.5rem] border-[1.5px] border-[#E8EAEE] "
                                              "rounded-lg')]")
        self._digitalprofile_details_section = page.locator("//div[contains(@class,'flex flex-col items-center "
                                                            "lg:max-w-[350px] lg:w-2/6 sm:min-w-[24rem] md:min-w-["
                                                            "24rem] bg-white rounded-lg max-h-[370px] h-full border-["
                                                            "1.5px] border-[#EFEFEF] shadow-[0_2px_15px_-3px_rgba(0,"
                                                            "0,0,0.1)] justify-between p-6 relative')]")
        self._source_leetcode = page.locator("//a[contains(@href,'https://leetcode.com')]")
        self._source_hackerrank = page.locator("//a[contains(@href,'https://www.hackerrank.com')]")
        self._source_hackerearth = page.locator("//a[contains(@href,'https://www.hackerearth.com')]")

        # Project Experience
        self._project_experience_tab = page.locator("//p[contains(text(),'Project Experience')]")
        self._github_stats = page.locator("//div[contains(@class,'grid grid-cols-3 w-[21.7rem] gap-4 lg:h-full')]")
        self._github_projects = page.locator("//a[contains(@class,'flex items-center gap-4 w-full font-text font-xs')]")

        # Accomplishment
        self._accomplishment_tab = page.locator(
            "(//div[contains(@class,'flex flex-row items-center justify-center lg:gap-4 md:gap-1 sm:gap-1')])[4]")
        self._learning_accomplishments_add_data = page.locator("(//span[contains(@class, 'flex flex-row items-center "
                                                               "gap-2 mr-3 cursor-pointer')])[1]")
        self._name_of_the_learning = page.locator("//input[@placeholder='Ex: JAVA verified skill in HackerRank']")
        self._certificate_url = page.locator("//input[@placeholder='Ex: http://www.google.com']")
        self._certificate_issued_date = page.locator("//input[@placeholder='Pick a date']")
        self._cancel_button = page.locator("//p[text()='Cancel']")
        self._submit_for_approval = page.locator("//button[normalize-space()='Submit For Approval']")
        self._certificate = page.locator("(//div[contains(@class,'flex flex-row items-center justify-between w-[97%] "
                                         "h-[79px] border-[#EFEFEF] py-10 border-b-[1px]')])[1]/following-sibling::*[1]")
        # Locator for the divs containing the buttons
        self._div_elements = page.locator(
            "//div[contains(@class,'flex flex-row items-center justify-between w-[97%] h-[79px] border-[#EFEFEF] py-10 border-b-')]")

        # Locator for the buttons
        self._buttons = page.locator(
            "a.flex.flex-row.items-center.gap-2.cursor-pointer.font-text.self-start.justify-self-start")

    @property
    def digital_profile_icon_click(self):
        return self._digital_profile_tab.click()

    def digital_profile_icon_click2(self):
        return self._digital_profile_tab.click()

    def projects_summary_details(self):
        return self._projects_summary.all_inner_texts()

    def foundation_skills_details(self):
        return self._foundation_skills.all_inner_texts()

    def project_details_1(self):
        return self._project_details1.all_inner_texts()

    def project_details_2(self):
        return self._project_details2.all_inner_texts()

    def previous_project_button_click(self):
        return self._previous_project_button.click()

    def next_project_button_click(self):
        return self._next_project_button.click()

    # Problem Solving
    def problem_solving_section(self):
        return self._problem_solving_tab.click()

    def digri_practice_status(self):
        return self._practice_stats.all_inner_texts()

    def digri_practice_details(self):
        return self._practice_details.all_inner_texts()

    def digitalprofile_details(self):
        return self._digitalprofile_details_section.all_inner_texts()

    def source_leetcode_button(self):
        return self._source_leetcode.click()

    def source_hackerrank_button(self):
        return self._source_hackerrank.click()

    def source_hackerearth_button(self):
        return self._source_hackerearth.click()

    # Project Experience
    def project_experience_button(self):
        return self._project_experience_tab.click()

    def github_all_projects(self):
        return self._github_projects

    # Accomplishment
    def accomplishments_tab_section(self):
        return self._accomplishment_tab.click()

    def learning_accomplishments_add_data_button(self):
        return self._learning_accomplishments_add_data.click()

    def name_of_the_learning_certificate_field(self, name):
        self._name_of_the_learning.clear()
        self._name_of_the_learning.fill(name)

    def certificate_url_field(self, certificate):
        self._certificate_url.clear()
        self._certificate_url.fill(certificate)

    def certificate_issued_date_field(self, issued_date):
        self._certificate_issued_date.clear()
        self._certificate_issued_date.fill(issued_date)

    def submit_for_approval_button(self):
        self._submit_for_approval.click()

    def add_data_cancel_button(self):
        self._cancel_button.click()

    def add_learning_accomplishments(self, name_certificate, certificate_url, issued_data):
        self.learning_accomplishments_add_data_button()
        self.name_of_the_learning_certificate_field(name_certificate)
        self.certificate_url_field(certificate_url)
        self.certificate_issued_date_field(issued_data)
        self.submit_for_approval_button()

    def click_link_if_text_matches(self, search_text):
        div_elements = self._div_elements.element_handles()
        print(f"Number of div elements found: {len(div_elements)}")

        for div_element in div_elements:
            try:
                div_text = div_element.inner_text()
                print(f"Found text: {div_text}")

                if search_text in div_text:
                    a_tag = div_element.query_selector(
                        "a.flex.flex-row.items-center.gap-2.cursor-pointer.font-text.self-start.justify-self-start")
                    if a_tag:
                        a_tag.click()
                        print(f"Clicked the link containing text: {search_text}")
                        return
            except Exception as e:
                print(f"An error occurred while processing a div element: {e}")

        print(f"No link found corresponding to text: {search_text}")
