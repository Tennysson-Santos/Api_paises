import json

import requests


URL = 'https://restcountries.eu/rest/v2/all'


def mostrar_paises():
	resposta = requests.get(URL)
	paises = json.loads(resposta.text)
	for pais in paises:
		print('País:',pais['name'],'Código:',pais['alpha2Code'])
		print('Moeda:',pais['currencies'][0]['name'],'-',pais['currencies'][0]['code'],'\n')
		

mostrar_paises()


