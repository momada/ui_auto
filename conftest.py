def pytest_addoption(parser):
    parser.addoption('--settings', action='store')
    # parser.addoption("--driver", action="store", default="chrome", help="Type in browser type (e.g. chrome)")
    # parser.addoption("--headless", action="store", default="headless", help="Is headless driver?")
