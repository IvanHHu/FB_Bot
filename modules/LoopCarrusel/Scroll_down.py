import modules.ExtractInfo.Extract_info as GetInfo
import time
from collections import defaultdict
import json

class Scroll_on():

    def __init__(self,driver):
        self.driver = driver
        
    def StartScroll(self):
        driver = self.driver
        contador = 1
        time.sleep(10)
        d = {}
        gt = driver.find_elements_by_css_selector("div[data-pagelet='FeedUnit_0']")
        for value in gt:
            pictures = ''
            links = ''
            if 'Sponsored' in value.text or 'Publicidad' in value.text:
                    name_company = str(str(value.text).split('\n')[0]).strip()
                    for x in value.find_elements_by_tag_name('img'):
                        if 'https://scontent.fmex' in x.get_attribute('src') and not '5FB1575B' in x.get_attribute('src'):
                            pics = str(x.get_attribute('src'))
                            pictures = pics + '\n' + pictures
                    for r in value.find_elements_by_xpath('//h4/div/a'):
                        if str(r.text).strip() == name_company:
                            fb_link = r.get_attribute('href')
                            links = fb_link + '\n' + links
                    d[name_company] = {'Perfil': links, 'Imagenes': pictures}
        gt = driver.find_elements_by_css_selector("div[data-pagelet='FeedUnit_1']")
        for value in gt:
            pictures = ''
            links = ''
            if 'Sponsored' in value.text or 'Publicidad' in value.text:
                    name_company = str(str(value.text).split('\n')[0]).strip()
                    for x in value.find_elements_by_tag_name('img'):
                        if 'https://scontent.fmex' in x.get_attribute('src') and not '5FB1575B' in x.get_attribute('src'):
                            pics = str(x.get_attribute('src'))
                            pictures = pics + '\n' + pictures
                    for r in value.find_elements_by_xpath('//h4/div/a'):
                        if str(r.text).strip() == name_company:
                            fb_link = r.get_attribute('href')
                            links = fb_link + '\n' + links
                    d[name_company] = {'Perfil': links, 'Imagenes': pictures}
        while contador < 10:
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            d = GetInfo.Init(driver,d)
            contador += 1
            time.sleep(5)
            with open('data_fb.json', 'w') as f:
                json.dump(d, f)
        return driver
    
def Init(driver):
    Start = Scroll_on(driver)
    driver = Start.StartScroll()
    return driver