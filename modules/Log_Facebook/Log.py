from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Log_In():

    def __init__(self,driver,usuario,password):
        self.password = password
        self.usuario = usuario
        self.driver = driver
    def Start_Log(self):
        driver = self.driver
        driver.get('https://www.facebook.com/')
        driver.execute_script("arguments[0].value= '" + self.usuario + "';", WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.NAME,"email"))))
        driver.execute_script("arguments[0].value= '" + self.password + "';", WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.NAME,"pass"))))
        #WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH,'//*[@name="pass"]'))).send_keys(se)
        WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.NAME,"login"))).click()
        return driver
def Init(driver,usuario,password):
    Start = Log_In(driver,usuario,password)
    driver = Start.Start_Log()
    return driver