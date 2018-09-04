from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
option = webdriver.ChromeOptions()
browser = webdriver.Chrome(executable_path="D:\chromedriver_win32\chromedriver.exe", chrome_options=option)
browser.get("https://www.amazon.com/Kenmore-04661219-Top-Freezer-Refrigerator-Lighting/product-reviews/B073RL7JZB/ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&reviewerType=all_reviews&pageNumber=1")
# Wait 20 seconds for page to load
timeout = 20
Titlelist=list()
Commentslist=list()

for i in range (1 and 40):
        CustomerReview = browser.find_element_by_id("cm_cr-review_list")
        list_of_Review = CustomerReview.find_elements_by_xpath(".//*")
        for r in list_of_Review:
                Title = r.find_elements_by_xpath('//*[@class="a-section celwidget"]//div[1]//a[2]')
        for t in Title:
                Titlelist.append(t.text)
                Comments = r.find_elements_by_xpath('//*[@class="a-section celwidget"]/div[4]/span')
        for c in Comments:
                Commentslist.append(c.text)
        elem=browser.find_element_by_xpath('//*[@id="cm_cr-pagination_bar"]/ul/li[@class="a-last"]/a')
        if elem.is_displayed()==False:
            break
        #You were clicking before checking if the element is displayed. Thus the crashes - Prashant
        elem.click
        browser.get(elem.get_attribute('href'))
        print(Commentslist)
        print(Titlelist)























