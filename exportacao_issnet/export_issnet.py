# -*- coding: utf-8 -*-
# -*- coding: cp1252 -*-
# import webdriver
from __future__ import unicode_literals
import time
from selenium.webdriver.support.select import Select
import pyautogui
from exception.lancar_excecao import lancamento_excecao, lancamento_excecao_telas
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By
PASTA_RELATORIO_CONTRATADOS = r'C:\ISS\relatorio_contratados'
PASTA_LIVRO_PRESTADOS = r'C:\ISS\livro_prestados'
# PASTA_RELATORIO_CONTRATADOS = r'C:\ISS\relatorio_contratados'
# PASTA_LIVRO_PRESTADOS = r'C:\ISS\livro_prestados'


class Cliente:
    primeiro = True


def inserir_IE(driver, IE):
    driver.find_element(By.XPATH, '//*[@id="txtCae"]').send_keys(IE)


def clicar_botao_procurar_empresa(driver):
    driver.find_element(By.CLASS_NAME, 'nc-search').click()


def seleciona_empresa(driver, IE):
    lancamento_excecao(inserir_IE, driver, IE)
    lancamento_excecao(clicar_botao_procurar_empresa, driver)


def menu_toggle(driver):
    driver.find_element(By.XPATH, '//*[@id="menu-toggle"]').click()


def mudar_barra_lateral(driver):

    for _ in range(10):
        try:
            elemento = driver.find_element(By.ID, 'wrapper')
            break
        except ElementNotInteractableException as e:
            print('Retry in 1 second', e)
            time.sleep(1)

    if elemento.get_attribute("class") != 'toggled':
        lancamento_excecao(menu_toggle, driver)


def seleciona_menu(driver):

    lancamento_excecao(mudar_barra_lateral, driver)


def seleciona_menu_livro_1(driver):
    driver.find_element(By.XPATH,
                        '//*[@id="Menu1_MenuPrincipal"]/ul/li[6]/div/span[3]').click()


def seleciona_menu_livro_2(driver):
    driver.find_element(By.XPATH,
                        '//*[@id="Menu1_MenuPrincipal"]/ul/li[4]/div/span[3]').click()


def seleciona_livro_fiscal(driver, IE, empresa):

    if empresa[6] == 'I':
        lancamento_excecao(seleciona_menu_livro_1, driver)

    else:
        lancamento_excecao(seleciona_menu_livro_2, driver)


def emitir_livro_fiscal_1(driver):
    driver.find_element(By.XPATH,
                        '//*[@id="Menu1_MenuPrincipal"]/ul/li[6]/ul/li/div/a').click()


def emitir_livro_fiscal_2(driver):
    driver.find_element(By.XPATH,
                        '//*[@id="Menu1_MenuPrincipal"]/ul/li[4]/ul/li/div/a').click()


def emitir_livro_fiscal(driver, simples, empresa):

    if empresa[6] == 'I':
        lancamento_excecao(emitir_livro_fiscal_1, driver)
    else:
        lancamento_excecao(emitir_livro_fiscal_2, driver)


def switch_frame(driver):
    frame = driver.find_element(By.XPATH,
                                '//*[@id="iframe"]')
    driver.switch_to.frame(frame)


def mudar_frame(driver):
    lancamento_excecao(switch_frame, driver)


def switch_relatorio(driver):
    frame = driver.find_element(By.XPATH,
                                '//*[@id="viewer"]')
    driver.switch_to.frame(frame)


def mudar_para_relatorio(driver):
    lancamento_excecao(switch_relatorio, driver)


def frame_principal(driver):
    driver.switch_to.default_content()


def mudar_frame_principal(driver):
    lancamento_excecao(frame_principal, driver)


def selecionar_livro(driver):
    select = Select(driver.find_element(By.ID, 'ddlTipoDocumento'))
    select.select_by_value('0')


def selecionar_tipo_livro(driver):
    lancamento_excecao(selecionar_livro, driver)


def inserir_data_inicial(driver, dt_inicial):
    driver.find_element(By.XPATH,
                        '//*[@id="txtLivroFiscalDtInicial"]').send_keys(dt_inicial)


def selecionar_data_inicial_livro(driver, dt_inicial):
    lancamento_excecao(inserir_data_inicial, driver, dt_inicial)


def inserir_num_livro(driver):
    driver.find_element(By.XPATH,
                        '//*[@id="txtLivroFiscalNumLivro"]').send_keys('1')


def selecionar_num_livro(driver):
    lancamento_excecao(inserir_num_livro, driver)


def inserir_pag_inicial(driver):
    driver.find_element(By.XPATH,
                        '//*[@id="txtLivroFiscalPagInicial"]').send_keys('1')


def selecionar_pag_inicial(driver):
    lancamento_excecao(inserir_pag_inicial, driver)


def inserir_pag_final(driver, dt_final):
    driver.find_element(By.XPATH,
                        '//*[@id="txtLivroFiscalDtFinal"]').send_keys(dt_final)


def selecionar_data_final_livro(driver, dt_final):
    lancamento_excecao(inserir_pag_final, driver, dt_final)


def clica_entrar_empresa(driver):
    driver.find_element(By.XPATH,
                        '//*[@id="lblNomeEmpresa"]').click()


def trocar_empresa(driver):
    lancamento_excecao(clica_entrar_empresa, driver)


def clicar_botao_imprimir(driver):
    driver.find_element(By.XPATH,
                        '//a[@id="btnGerar"]').click()


def carregar_tela_impressao():
    return pyautogui.locateOnScreen('reportManager.png')


def carregar_tela_salvar():
    return pyautogui.locateOnScreen('botao_salvar.png')


def gerar_livro_prestados(driver, IE, empresa, caminho, padrao, dt_inicial):

    mes = dt_inicial[3:5]
    ano = dt_inicial[6:10]
    nome_salvar = f'{PASTA_LIVRO_PRESTADOS}\\{empresa[4]} {mes}{ano}'

    if Cliente.primeiro:
        # nao salvar senha
        pyautogui.click(1172, 339)
        time.sleep(2)
        lancamento_excecao(clicar_botao_imprimir, driver)
        time.sleep(5)
        pyautogui.click(1137, 46)
        time.sleep(1)
        pyautogui.click(924, 149)
        time.sleep(1)
        pyautogui.click(1165, 233)
        time.sleep(2)
        Cliente.primeiro = False

    lancamento_excecao(clicar_botao_imprimir, driver)
    print('passei por aqui 2')
    lancamento_excecao_telas(carregar_tela_impressao)
    print('passei por aqui 3')

    pyautogui.hotkey('ctrl', 's')
    lancamento_excecao_telas(carregar_tela_salvar)
    time.sleep(2)
    pyautogui.write(nome_salvar)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    # lancamento_excecao_telas(carregar_tela_impressao)
    # time.sleep(0.2)
    pyautogui.click(x=1144, y=19)

    # pyautogui.hotkey('alt', 'f4')


def percorrer_menu_e_emitir_livro_sv_prestados(driver, IE, dt_inicial,
                                               dt_final, simples,
                                               empresa, caminho):
    seleciona_empresa(driver, IE)
    time.sleep(1)
    seleciona_menu(driver)
    time.sleep(1)
    seleciona_livro_fiscal(driver, IE, empresa)
    time.sleep(1)
    emitir_livro_fiscal(driver, simples, empresa)
    time.sleep(1)
    mudar_frame(driver)
    time.sleep(1)
    selecionar_tipo_livro(driver)
    time.sleep(1)
    selecionar_num_livro(driver)
    time.sleep(1)
    selecionar_pag_inicial(driver)
    time.sleep(1)
    selecionar_data_inicial_livro(driver, dt_inicial)
    time.sleep(1)
    selecionar_data_final_livro(driver, dt_final)
    time.sleep(1)
    gerar_livro_prestados(driver, IE, empresa, caminho,
                          'LIVRO ISSQN PRESTADOS', dt_inicial)


def empresa_do_simples(empresa):
    if empresa[5] == 'N':
        return False
    else:
        return True


def exportar_empresas_prestados(driver, dic_empresas, dt_inicial, dt_final):
    caminho = False
    for empresa in dic_empresas.values():
        Identificador = empresa[4]
        simples = empresa_do_simples(empresa)

        percorrer_menu_e_emitir_livro_sv_prestados(driver, Identificador,
                                                   dt_inicial,
                                                   dt_final, simples,
                                                   empresa, caminho)
        caminho = True

        # gerar segunda empresa em diante
        mudar_frame_principal(driver)
        trocar_empresa(driver)
        print('*' * 50)
        print('*' * 50)
        print(empresa)
        print('*' * 50)
        print('*' * 50)

    print('Finalizando......', end='')
    for _ in range(10):
        print('..............', end='')
        time.sleep(1)
    driver.close()
    driver.quit()
