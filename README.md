# Desafio - Stone Pagamentos

O desafio consiste em desenvolver testes automatizados com cenários positivos e negativos para o form no link: https://stonepayments.typeform.com/to/yl5PKW.

## Getting Started

Os testes foram desenvolvidos utilizando Selenium WebDriver com a linguagem python e os testes são executados no navegador Chrome.

### Requisitos

Necessário baixar e instalar o python.

```
LINK: https://www.python.org/downloads/release/python-354/
```

### Instalações

Chrome driver

`MAC`

Download no link: https://chromedriver.storage.googleapis.com/index.html?path=74.0.3729.6/

Após extração, user o comando: `mv chromedriver /usr/local/bin`

`Windows`

Download no link: https://chromedriver.storage.googleapis.com/index.html?path=74.0.3729.6/

Apos extração, mover para pasta: `C:\Pyhton35-32\Scripts`


Instalação do Selenium:

```
pip3 install selenium
```

Instalação do Behave:

```
pip3 install behave
```

## Executar testes

Após acessar raiz do projeto pelo terminal/cmd, executar o comando: 

```
behave -t @positive1
```
```
TAGs Testes positivos:
positive1
positive2
positive3
positive4
positive5
```
```
TAGs Testes negativos:
negative1
negative2
negative3
```

## Versão

1.0.0

## Autor

* **Jonathan Eleutério** 





