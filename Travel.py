#!/usr/bin/env python
# coding: utf-8
import time
from time import sleep
import ast
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys


driver = webdriver.Chrome("C:\chromedriver.exe")
driver.get('https://tn.tunisiebooking.com/')

def exists(xpath):
        try:
            time.sleep(5)
            driver.find_element_by_css_selector(xpath);
        except NoSuchElementException:
            return "false"
        else:
            return "true"

# params to select
params = {
    'destination': sys.argv[1],
    'date_from': sys.argv[2],
    'date_to': sys.argv[3],
    'bedroom': '1'
}

# select destination
destination_select = Select(WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'ville_des'))))
destination_select.select_by_value(params['destination'])

# select bedroom
bedroom_select = Select(WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'select_ch'))))
bedroom_select.select_by_value(params['bedroom'])

# select dates
script = f"document.getElementById('checkin').value ='{params['date_from']}';"
script += f"document.getElementById('checkout').value ='{params['date_to']}';"
script +=  f"document.getElementById('depart').value ='{params['date_from']}';"
script += f"document.getElementById('arrivee').value ='{params['date_to']}';"
driver.execute_script(script)

# submit form
btn_rechercher = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="boutonr"]')))
btn_rechercher.click()
    
#----------  
#fonction pour tester l'existance de la bouton plus
def exists(xpath):
        try:
            time.sleep(5)
            driver.find_element_by_css_selector(xpath);
        except NoSuchElementException:
            return "false"
        else:
            return "true"
        
#Si le bouton exist il va le cliquer sinon il va passer        
if (exists('img[src="https://tn.tunisiebooking.com/theme/images/plus_resv2.png"]')=="true"):
    time.sleep(5)
    driver.find_element_by_css_selector('img[src="https://tn.tunisiebooking.com/theme/images/plus_resv2.png"]').click()
    sleep(10)
else :
    pass


#Stocker les liens des hotels dans une liste
i=0
ds = []    
urls = []    
records = []
hotels = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[starts-with(@id,'produit_affair')]")))

for hotel in hotels:
    link = hotel.find_element_by_xpath(".//span[@class='tittre_hotel']/a").get_attribute("href")
    i=i+1
    urls.append(link)
print(i)

#parcourir les liens un par un
for url in urls:
    driver.get(url)
    
    #Fonction qui teste l'existance de bouton tarifs et dispo   
    def existsElement(xpath):
        try:
            driver.find_element_by_id(xpath);
        except NoSuchElementException:
            return "false"
        else:
            return "true"
    
    if (existsElement('result_par_arrangement')=="false"):
   
        btn_t = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="moteur_rech"]/form/div/div[3]/div')))

        btn_t.click()
        sleep(10)
    else :
        pass
               
    
    try:
        #nom hotel
        name = str(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='bloc_titre_hotels']/h2"))).text)
        #arrangement
        arropt = driver.find_element_by_xpath("//div[contains(@class,'line_result')][1]")
        #type chambre
        opt = str(arropt.find_element_by_tag_name("b").text)
        #Compteur pour savoir le nombre d'arrangements pour chaque hotel
        num = len(arropt.find_elements_by_tag_name("option"))
        optiondata = {}
        achats = {}
        marges= {}
        #selectionner les arrangement 
       # selection = Select(driver.find_element_by_id("arrangement"))
        #parcourir les arrangement un par un
        for i in range(num):
            try:
                time.sleep(2)
                WebDriverWait(driver, 190).until(EC.presence_of_element_located((By.ID, 'result_par_arrangement'))) 

                selection = Select(driver.find_element_by_id("arrangement"))
                selection.select_by_index(i)
                time.sleep(2)
                #stocker le text d'arrangemet
                arr = driver.find_element_by_xpath("//select[@id='arrangement']/option[@selected='selected']").text
                #stocker le prix de vente
                prize = driver.find_element_by_id("prix_total").text

                optiondata[arr] = (int(prize))
                #click sur bouton "je passe à l'agence "
                btn_passe = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="resultat"]/div/form/div/div[2]/div[1]/div[2]/div[2]/div')))
                btn_passe.click()



                # params to select
                params = {
                            'civilite_acheteur': 'Mlle',
                            'prenom_acheteur': 'test',
                            'nom_acheteur': 'test',
                            'e_mail_acheteur': 'test@gmail.com',
                            'portable_acheteur': '22222222',
                            'ville_acheteur': 'Test',
                        }

                # select civilite
                civilite_acheteur = Select(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'civilite_acheteur'))))
                civilite_acheteur.select_by_value(params['civilite_acheteur'])

                # saisir prenom 
                script  = f"document.getElementsByName('prenom_acheteur')[0].value ='{params['prenom_acheteur']}';"
                script += f"document.getElementsByName('nom_acheteur')[0].value ='{params['nom_acheteur']}';"
                script += f"document.getElementsByName('e_mail_acheteur')[0].value ='{params['e_mail_acheteur']}';"
                script += f"document.getElementsByName('portable_acheteur')[0].value ='{params['portable_acheteur']}';"
                script += f"document.getElementsByName('ville_acheteur')[0].value ='{params['ville_acheteur']}';"
                driver.execute_script(script)

                # choisir agence
                btn_agence = driver.find_element_by_id('titre_Nabeul')
                btn_agence.click()

                btn_continuez = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'boutonr')))
                btn_continuez.click()
                
                achat = str(int(driver.find_element_by_xpath('/html/body/header/div[2]/div[1]/div[1]/div[4]/div[2]/div[2]').text.replace(' TND', '')))

                achats[arr]=achat

                marge =str(int(((float(prize) - float(achat)) / float(achat)) * 100))+"%";
                marges[arr]=marge
                optiondata[arr]=prize,achat,marge
                
                
                driver.get(url)
                btn_display = WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="moteur_rech"]/form/div/div[3]/div')))

                btn_display.click()
                time.sleep(0.5)
               

            except StaleElementReferenceException:
                pass

            

    except NoSuchElementException:
        pass
    

    s="{} - {}".format(name,optiondata)


    cols = []
    from ast import literal_eval

    for l in s.splitlines():
            d = l.split("-")
            print(d)
            if len(d) > 1:
                from ast import literal_eval
               
                vals = literal_eval(d[1].strip())
                #df = pd.DataFrame({k: v if isinstance(v, (list, tuple)) else [v] for k, v in vals.items()})
                df =pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in vals.items() ])) #B (Better)
               
                cols = df.columns
                cols = [((d[0], col)) for col in df.columns]
             
                df.columns=pd.MultiIndex.from_tuples(cols)
                ds.append(df)
                
for df in ds:
    df.reset_index(drop=True, inplace=True)

df = pd.concat(ds, axis= 1)


print(df.T)
df.T.to_excel(sys.argv[4]+".xlsx")
driver.quit()
