class HomePageElements:
    def __init__(self, drive):
        self.driver = drive

    def device_btn(self):
        return self.driver.find_element_by_xpath('//li[@data-automation-id="nav-list-item-10"]')

    def activedevice_title(self):
        return self.driver.find_element_by_xpath('//h1[@class="list-title list-header-name__title list-header-title"]')

    def default_filter(self):
        return self.driver.find_element_by_xpath('//span[@class="is-op "]')
