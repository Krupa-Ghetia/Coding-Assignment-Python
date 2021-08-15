from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


list_of_names = []
list_of_links = []
repo_url = "https://github.com/vinta/awesome-python"


def scrape_links_from_repo():
    driver = get_firefox_driver()
    driver.get(repo_url)

    readme_section = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "readme")))
    elements = readme_section.find_elements_by_tag_name('a')

    for elem in elements:
        list_of_names.append(elem.get_attribute("innerHTML"))
        list_of_links.append(elem.get_attribute("href"))


def search_link_by_name():
    input_name = input("Query? ")

    if input_name in list_of_names:
        name_idx = list_of_names.index(input_name)
        print(f"""Output: {list_of_links[name_idx]}""")

    else:
        print(f"""{input_name} does not exist!""")


def get_firefox_driver():
    options = Options()
    options.headless = True

    return webdriver.Firefox(options=options)


if __name__ == "__main__":
    scrape_links_from_repo()
    search_link_by_name()
