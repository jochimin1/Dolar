#!/usr/bin/env python
# -*- coding: utf-8 -*-

# imports 
import requests
from fastapi import FastAPI
from bs4 import BeautifulSoup

# instance FastAPI
app = FastAPI()


# url to scrape
url_dolar = "http://hoy.com.do"

# request to url
response = requests.get(url_dolar)

# parse all the html
html = BeautifulSoup(response.text, "html.parser")


# scrape a specific section of html
dolar_compra = html.find_all('td')[1].text
dolar_venta = html.find_all('td')[2].text

#print(' $$$$Precio Dolar$$$$$')
#print('\nPrecio Compra->', dolar_compra)
#print('Precio Venta->', dolar_venta)

# Route to show results
@app.get('/dolar')
async def root():
    return {
        "Compra Dolar": dolar_compra,
        "Venta Dolar": dolar_venta
    }

