class ReportPageElements:
    def __init__(self, drive):
        self.driver = drive

    def rpt_search_box(self):
        return self.driver.find_element_by_xpath('//input[@class="c0277 c0261 list-filter is-valid form-control"]')

    def activedevice_title(self):
        return self.driver.find_element_by_xpath('//h1[@class="list-title list-header-name__title list-header-title"]')

    def default_filter(self):
        return self.driver.find_element_by_xpath('//span[@class="is-op "]')

    def eventstore_btn(self):
        return self.driver.find_element_by_xpath('//a[@data-automation-id="00000000-0000-0000-0000-000000000401-nested-list-item"]')

    def eventstore_title(self):
        return self.driver.find_element_by_xpath('//div[contains(@class,"event-store-header row")]')
