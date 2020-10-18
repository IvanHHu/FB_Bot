import modules.StartChrome.StartChromedriver as StartGoogle
import modules.Log_Facebook.Log as Log_in
import modules.LoopCarrusel.Scroll_down as Scroll
import time

if __name__ == '__main__':
    print("Por favor, ingrese el correo de su cuenta de correo: ", end="")
    Usuario = input()
    print("Por favor, la password correspondiente: ", end="")
    password = input()
    RunSelenium = StartGoogle.RunSelenium()
    driver = RunSelenium.driverSetup()
    driver = Log_in.Init(driver,Usuario,password)
    Scroll.Init(driver)