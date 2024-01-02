driver = webdriver.Chrome()
driver.get("https://www.cowin.gov.in/")
home_window = driver.current_window_handle
create_faq_link = driver.find_element_by_link_text("Create FAQ")
create_faq_link.click()

partners_link = driver.find_element_by_link_text("Partners")
partners_link.click()
window_handles = driver.window_handles
for handle in window_handles:
    print("Window ID:", handle)
for handle in window_handles:
    if handle != home_window:
        driver.switch_to.window(handle)
        driver.close()
driver.switch_to.window(home_window)
driver.quit()
