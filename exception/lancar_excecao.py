import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException


def lancamento_excecao(funcao, driver, *args, **kwargs):
    for _ in range(kwargs.get('segundos', 10)):
        try:
            funcao(driver, *args)
            break

        except ElementNotInteractableException as e:
            print('Retry in 1 second', e, funcao.__name__)
            time.sleep(1)

        except NoSuchElementException as e:
            print('Retry in 1 second', e, funcao.__name__)
            time.sleep(1)
        # except Exception as e:
        #     print('Retry in 1 second', e, funcao.__name__)
        #     time.sleep(1)


def lancamento_excecao_telas(funcao):
    i = 1

    while(not funcao()):
        print(f'Retry in {i} second')
        time.sleep(1)
        i = i + 1
