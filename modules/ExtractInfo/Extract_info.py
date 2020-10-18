from collections import defaultdict

class Extract_Info():

    def __init__(self,driver,d):
        self.driver = driver
        self.d = d
    def Extract(self):
        driver = self.driver
        d = self.d
        gt = driver.find_elements_by_css_selector("div[data-pagelet='FeedUnit_{n}']")
        for value in gt:
            pictures = ''
            links = ''
            if 'Sponsored' in value.text:
                    name_company = str(str(value.text).split('\n')[0]).strip()
                    print(name_company)
                    for x in value.find_elements_by_tag_name('img'):
                        if 'https://scontent.fmex' in x.get_attribute('src') and not '5FB1575B' in x.get_attribute('src'):
                            pics = str(x.get_attribute('src'))
                            pictures = pics + '\n' + pictures
                    for r in value.find_elements_by_xpath('//h4/div/a'):
                        print(r.text)
                        if str(r.text).strip() == name_company:
                            fb_link = r.get_attribute('href')
                            links = fb_link + '\n' + links
                    d[name_company] = {'Perfil': links, 'Imagenes': pictures}
        return d
    
def Init(driver,d):
    Start = Extract_Info(driver,d)
    driver = Start.Extract()
    return driver