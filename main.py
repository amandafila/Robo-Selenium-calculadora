import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#pandas reconhecendo a lista
numeros = pd.read_csv("n decimais.csv")
listagem = numeros.iloc[:, 0].tolist()

binario = []

#adicionando webdriver
driver = webdriver.Chrome()
driver.get("https://www.calculadoraonline.com.br/conversao-bases")

for numero in listagem:
    try: 

        wait = WebDriverWait(driver, 10)  
        caixa_decimal = wait.until(EC.presence_of_element_located((By.ID, 'c3')))
        caixa_decimal.clear()
        caixa_decimal.send_keys(numero)
        campo_binario = driver.find_element(By.ID, 'c1')
        valor = campo_binario.get_attribute("value")

        print(f"{numero} = {valor}")
        binario.append((numero, valor))
    
    except:
        print("erro")

df_resultado = pd.DataFrame(binario, columns=["Decimal", "Binário"])
df_resultado.to_csv("resultados_binarios.csv", index=False)
