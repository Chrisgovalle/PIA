import requests
import json
import os
import statistics
import matplotlib.pyplot as plt
from collections import Counter

stored_data = {}

def pastel():
    habilidades = []

    for pokemon, data in stored_data.items():
        if "habilidades" in data:
            habilidades.extend(data["habilidades"])

    if habilidades:
        counter = Counter(habilidades)
        labels, sizes = zip(*counter.items())

        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightblue', 'lightgreen'])
        plt.title('Distribución de Habilidades de Pokémon')
        plt.show()
    else:
        print("No hay datos de habilidades para graficar el pastel.")

def barra():
    tipos = []

    for pokemon, data in stored_data.items():
        if "tipos" in data:
            tipos.extend(data["tipos"])

    if tipos:
        counter = Counter(tipos)
        tipos, frecuencias = zip(*counter.items())

        plt.bar(tipos, frecuencias, color='lightgreen')
        plt.title('Distribución de Tipos de Pokémon')
        plt.xlabel('Tipo')
        plt.ylabel('Cantidad')
        plt.show()
    else:
        print("No hay datos de tipos para graficar las barras.")



def histograma():
    alturas = []

    for pokemon, data in stored_data.items():
        if "altura" in data:
            alturas.extend(data["altura"])

    if alturas:
        plt.hist(alturas, bins=10, color='skyblue', edgecolor='black')
        plt.title('Histograma de Alturas de Pokémon')
        plt.xlabel('Altura')
        plt.ylabel('Frecuencia')
        plt.show()
    else:
        print("No hay datos de altura para graficar el histograma.")



def estadisticas():
    alturas = []

    # Recorre la información almacenada y extrae las alturas
    for pokemon, data in stored_data.items():
        if "altura" in data:
            alturas.extend(data["altura"])

    if alturas:
        print("\nAnálisis Estadístico de Alturas:")
        print(f"Promedio: {statistics.mean(alturas)}")
        print(f"Mínimo: {min(alturas)}")
        print(f"Máximo: {max(alturas)}")
        print(f"Moda: {statistics.mode(alturas) if len(alturas) > 1 else 'No hay moda (datos únicos)'}")
        # Puedes agregar más estadísticas según sea necesario.
    else:
        print("No hay datos de altura para realizar un análisis estadístico.")


def leer_datos():
        if os.path.isfile("datos.json"):
            with open("datos.json", "r") as archivo:
                data = json.load(archivo)
                return data
        else:
            print("No se encontró el archivo.")

def consultar_informacion():
    if not stored_data:
        print("No hay información almacenada.")
        return

    print("\nInformación almacenada:")
    for pokemon, data in stored_data.items():
        print(f"\n{pokemon.capitalize()}:")
        for key, value in data.items():
            print(f"  - {key.capitalize()}: {', '.join(map(str.capitalize, value))}")



def movimientos(nombre_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}/"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        movimientos = [movimiento["move"]["name"] for movimiento in datos["moves"]]

        print(f"Lista de movimientos de {nombre_pokemon.capitalize()}:")
        for movimiento in movimientos:
            print(f"- {movimiento.capitalize()}")

        # Ask the user if they want to store the information
        store_data = input("¿Desea almacenar la información de movimientos? (Sí/No): ").lower()
        if store_data == 'si':
            stored_data[nombre_pokemon] = {"movimientos": movimientos}
            print(f"Información de movimientos para {nombre_pokemon} almacenada.")
        else:
            print("Información no almacenada.")
    else:
        print(f"Error al obtener la información de movimientos")


def tipos():
    url_pokemon = "https://pokeapi.co/api/v2/pokemon/?limit=20"
    respuesta_pokemon = requests.get(url_pokemon)

    if respuesta_pokemon.status_code == 200:
        datos_pokemon = respuesta_pokemon.json()
        lista_pokemon = datos_pokemon["results"]

        print("Pokémon con sus tipos:")
        for pokemon in lista_pokemon:
            nombre_pokemon = pokemon["name"]
            url_detalle_pokemon = pokemon["url"]
            respuesta_detalle_pokemon = requests.get(url_detalle_pokemon)

            if respuesta_detalle_pokemon.status_code == 200:
                datos_detalle_pokemon = respuesta_detalle_pokemon.json()
                tipos_pokemon = [tipo["type"]["name"] for tipo in datos_detalle_pokemon["types"]]

                print(f"\n{nombre_pokemon.capitalize()}:")
                for tipo in tipos_pokemon:
                    print(f"  - {tipo.capitalize()}")
                
                # Ask the user if they want to store the information
                store_data = input(f"¿Desea almacenar la información de tipos para {nombre_pokemon}? (Sí/No): ").lower()
                if store_data == 'si':
                    stored_data[nombre_pokemon] = {"tipos": tipos_pokemon}
                    print(f"Información de tipos para {nombre_pokemon} almacenada.")
                else:
                    print("Información no almacenada.")
            else:
                print(f"Error al obtener la información del Pokémon. Código de estado: {respuesta_detalle_pokemon.status_code}")

    else:
        print(f"Error al obtener la lista de Pokémon. Código de estado: {respuesta_pokemon.status_code}")


def habilidades():
    url_pokemon = "https://pokeapi.co/api/v2/pokemon/?limit=20"
    respuesta_pokemon = requests.get(url_pokemon)

    if respuesta_pokemon.status_code == 200:
        datos_pokemon = respuesta_pokemon.json()
        lista_pokemon = datos_pokemon["results"]

        print("Pokémon con sus habilidades:")
        for pokemon in lista_pokemon:
            nombre_pokemon = pokemon["name"]
            url_detalle_pokemon = pokemon["url"]
            respuesta_detalle_pokemon = requests.get(url_detalle_pokemon)

            if respuesta_detalle_pokemon.status_code == 200:
                datos_detalle_pokemon = respuesta_detalle_pokemon.json()
                habilidades_pokemon = [habilidad["ability"]["name"] for habilidad in datos_detalle_pokemon["abilities"]]

                print(f"\n{nombre_pokemon.capitalize()}:")
                for habilidad in habilidades_pokemon:
                    print(f"  - {habilidad.capitalize()}")

                # Ask the user if they want to store the information
                store_data = input(f"¿Desea almacenar la información de habilidades para {nombre_pokemon}? (Sí/No): ").lower()
                if store_data == 'si':
                    stored_data[nombre_pokemon] = {"habilidades": habilidades_pokemon}
                    print(f"Información de habilidades para {nombre_pokemon} almacenada.")
                else:
                    print("Información no almacenada.")
            else:
                print(f"Error al obtener la información del Pokémon. Código de estado: {respuesta_detalle_pokemon.status_code}")

    else:
        print(f"Error al obtener la lista de Pokémon. Código de estado: {respuesta_pokemon.status_code}")


def lista_poke():
    url = "https://pokeapi.co/api/v2/pokemon/?limit=20"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        lista_pokemon = datos["results"]

        print("Lista de Pokémon:")
        for pokemon in lista_pokemon:
            print(f"- {pokemon['name'].capitalize()}")
    else:
        print(f"Error al obtener la lista de Pokémon. Código de estado: {respuesta.status_code}")


def funcion_1():
    while True:
        print("Informacion de la Api \n1-Lista de pokemones \n2-Habilidades \n3-Tipos \n4-Movimientos \n5-Salir")

        op = input("Selecciona una opcion: ")
        if op == '1':
            lista_poke()
        elif op == '2':
            habilidades()
        elif op == '3':
            tipos()
        elif op == '4':
            nombre_pokemon = input("Ingrese el nombre del Pokémon: ")
            movimientos(nombre_pokemon)
        elif op == '5':
            print("Saliendo......")
            break
        else:
            print("Selecciona una opción correcta")

        # Print the stored data at the end of each iteration
        print("\nInformación almacenada:")
        print(stored_data)



# menu
while True:
    print("Menu")
    print("1-Consulta de informacion de API's \n2-Lectura de archivos \n3-Escritura de archivos \n4-Analisis estadisticos \n5-Generacion de graficas \n6-Salir")

    opcion = input("Selecciona una opcion: ")

    if opcion == '1':
        funcion_1()
    elif opcion == '2':
        consultar_informacion()
    elif opcion == '3':
        leer_datos()
    elif opcion == '4':
        estadisticas()
    elif opcion == '5':
        while True:
            print("Escoge un tipo de grafica \n1-Grafica de histograma \n2-Grafica de barra \n3-Grafica de pastel \n4-Salir")
            po=input("Ingresa una opcion")
            if po == '1':
                histograma()
            elif po == '2':
                barra()
            elif po == '3':
                pastel()
            elif po == '4':
                print("Saliendo......")
                break
            else:
                print("Escoge una opcion valida")


    elif opcion == '6':
        print("Saliendo.....")
        break
    else:
        print("Opción incorrecta, favor de seleccionar una opción del 1-6")