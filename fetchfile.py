from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def get_drvier():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("no-sandbox")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver

def main():
    driver = get_drvier()
    driver.get('https://et.wikipedia.org/wiki/Eesti')
    element = driver.find_element(by="xpath", value="/html/body/div[3]/div[3]/div[5]/div[1]/p[1]/b")
    return element.text

print(main())