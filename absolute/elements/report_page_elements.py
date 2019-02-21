class ReportPageElements:
    def __init__(self, drive):
        self.driver = drive

    def rpt_search_box(self):
        return self.driver.find_element_by_xpath('//input[@class="c0277 c0261 list-filter is-valid form-control"]')

    # def find_search_box(self):
    #     return self.driver.find_element_by_xpath('//li[@data-automation-id="nav-list-item-10"]')
    #
    # def find_search_box(self):
    #     return self.driver.find_element_by_xpath('//li[@data-automation-id="nav-list-item-10"]')