from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time

def main():
    # Caminho para o executável do EdgeDriver
    caminho_executavel_edge = r"C:\Users\Kauã Rodrigo\Documents\Scripts-Python\Curso em vídeo\Idea\CursoEmVideo\cursoapi\msedgedriver.exe"

    # Configuração do serviço
    service = Service(executable_path=caminho_executavel_edge, verbose=True)

    # Configuração das opções
    options = Options()

    # Inicialização do driver
    with webdriver.Edge(service=service, options=options) as driver:

        # Navega até o site
        driver.get('https://www.nba.com/standings?Season=2022-23')

        # Localiza o elemento pelo ID e envia as teclas
        element = driver.find_element(By.ID, 'sb_form_q')
        element.send_keys('WebDriver')
        element.submit()

        # Aguarda por 5 segundos
        time.sleep(5)

# Chamada da função principal
if __name__ == "__main__":
    main()
