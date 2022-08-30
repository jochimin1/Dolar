#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from fastapi import FastAPI
from bs4 import BeautifulSoup

app = FastAPI()


url_dolar = "http://hoy.com.do"


response = requests.get(url_dolar)

html = BeautifulSoup(response.text, "html.parser")

dolar_compra = html.find_all('td')[1].text

dolar_venta = html.find_all('td')[2].text

#print(' $$$$Precio Dolar$$$$$')
#print('\nPrecio Compra->', dolar_compra)
#print('Precio Venta->', dolar_venta)


@app.get('/compra')
async def root():
    return {
        "Compra Dolar": dolar_compra,
        "Venta Dolar": dolar_venta
    }

