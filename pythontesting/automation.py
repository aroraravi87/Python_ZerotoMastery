from selenium import webdriver

chrome_browser= webdriver.Chrome('./chromedriver')
chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'selenium easy web' in chrome_browser.title

assert 'selenium easy web' in chrome_browser.find_element_by_tag_name('body')

show_message_button=chrome_browser.find_elements_by_class_name('btn-default')
print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message=chrome_browser.find_elements_by_id('user-message')
user_message.clear()
user_message.send_keys('I am cool')

show_message_button.click()

output_message=chrome_browser.find_elements_by_id('display')

assert 'I am cool' in output_message.text


#chrome_browser.close()
chrome_browser.quit()
