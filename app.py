from selenium import webdriver
from time import sleep

class TinderBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        self.driver.get('https://www.tinder.com')
        sleep(2)
    def login(self):
        botao_login = self.driver.find_element_by_xpath('//*[@id="o-1556761323"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
        sleep(2)
        botao_login.click()
        sleep(2)
    def logar_com_telefone(self):
        logar_com_telefone = self.driver.find_element_by_xpath('//*[@id="o-1335420887"]/div/div/div[1]/div/div[3]/span/div[3]/button')
        sleep(2)
        logar_com_telefone.click()
        sleep(2)
    def esperar_input(self):
        input()
    def fechar_localizacao(self):
        localizacao = self.driver.find_element_by_xpath('//*[@id="o-1335420887"]/div/div/div/div/div[3]/button[1]/span')
        sleep(2)
        localizacao.click()
        sleep(2)
    def fechar_notificacao(self):
        notificacao = self.driver.find_element_by_xpath('//*[@id="o-1335420887"]/div/div/div/div/div[3]/button[2]')
        sleep(2) 
        notificacao.click()
        sleep(2)
    def like(self):
        try:
            sleep(1)
            curtir = self.driver.find_element_by_xpath('//*[@id="o-1556761323"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
        
        except:
            try:
                curtir = self.driver.find_element_by_xpath('//div[@class="Mx(a) Fxs(0) Sq(70px) Sq(60px)--s Bd Bdrs(50%) Bdc($c-like-green)"]')
            except:
                pass
            
        finally:
            sleep(1)
            curtir.click()
            try:
                sleep(2)
                if self.driver.find_element_by_xpath("//label[text()='Diga algo legal!'") is not None:
                    sleep(2)
                    fechar_janela = self.driver.find_element_by_xpath("//button[@tittle='Back to Tinder")
                    sleep(2)
                    fechar_janela.click()  
                    sleep(2)
            except:
                pass
            try:
                sleep(2)
                if self.driver.find_element_by_xpath('//*[@id="o-1335420887"]/div/div/div[2]/button[2]') is not None:
                    fechar_janela_interesse = self.driver.find_element_by_xpath('//*[@id="o-1335420887"]/div/div/div[2]/button[2]')
                    sleep(2)
                    fechar_janela_interesse.click()
                    sleep(2)
            except:
                pass
            try:
                sleep(2)
                if self.driver.find_element_by_xpath('//*[@id="o-1335420887"]/div/div/button[1]') is not None:
                    fechar_janela_platinum = self.driver.find_element_by_xpath('//*[@id="o-1335420887"]/div/div/button[2]')
                    sleep(2)
                    fechar_janela_platinum.click()
                    sleep(2)
            except:
                pass



bot = TinderBot()
bot.login()
bot.logar_com_telefone()
bot.esperar_input()
bot.fechar_localizacao()
bot.fechar_notificacao()

while True:
    bot.like()
    