import requests
import json

def nombrePokemon(url,limit):
#Esta funcion se encarga de contar los pokemones que tienen en su nombre 'at' y poseen 2 'aa' en su nombre
	payload = {'limit': '2000'}
	res=requests.get(url,params=payload)
	contador=0
	listPK=[]
	if res.status_code==200:
		datos=res.json()
		results=datos.get('results',[])
		if results:
			for pokemon in results:
				contador+=1
				name=pokemon['name']
#Se comprueba que el nombre contenga la subcadena 'at'			
				if 'at' in name:
					contador=0
#Se recorre caracter por caracter y se cuenta el numero de 'a' del nombre del pokemon				
					for characters in name:
						if characters=='a':
							contador+=1

					if contador==2:
						listPK.append(name)
#Se imprime el tamaño de la lista que contiene los pokemones que cumplen las condiciones 						
		print(len(listPK))			
					

if __name__ == '__main__':
	url='https://pokeapi.co/api/v2/pokemon/'
	nombrePokemon(url,2000)

		
		