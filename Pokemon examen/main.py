import csv

from clases.pokemon import *
from clases.pokemon_agua import *
from clases.pokemon_aire import *
from clases.pokemon_electricidad import *
from clases.pokemon_tierra import *
from clases.tipo_ataque import Ataque


def crear_entrenador1(entrenador):
    try:
        with open('coach_1_pokemons.csv', newline='') as csv_file:
            lector= csv.reader('coach_1_pokemons.csv')
            info_entrenador_1=list(lector)
            for temp_pokemon_csv in info_entrenador_1:
                pokemon_csv_a_la_lista = pokemon(int(temp_pokemon_csv[0]),temp_pokemon_csv[1],Ataque.tipo_ataque(temp_pokemon_csv[2]),int(temp_pokemon_csv[3]),int(temp_pokemon_csv[4]),int(temp_pokemon_csv[5]))
                entrenador.append(pokemon_csv_a_la_lista)
    except(SyntaxError):
        print("Ha ocurrido un error dentro de la cadena de caracteres del csv")

    return entrenador

def crear_entrenador2(entrenador):
    try:
        with open('coach_2_pokemons.csv', newline='') as csv_file:
            lector= csv.reader('coach_1_pokemons.csv')
            info_entrenador_2=list(lector)
            for temp_pokemon_csv in info_entrenador_2:
                pokemon_csv_a_la_lista = pokemon(int(temp_pokemon_csv[0]),temp_pokemon_csv[1],Ataque.tipo_ataque(temp_pokemon_csv[2]),int(temp_pokemon_csv[3]),int(temp_pokemon_csv[4]),int(temp_pokemon_csv[5]))
                entrenador.append(pokemon_csv_a_la_lista)
    except(SyntaxError):
        print("Ha ocurrido un error dentro de la cadena de caracteres del csv")

    return entrenador

def main():
    #Creamos a los entrenadores
    coach1=[]
    coach2=[]
    crear_entrenador1(coach1)
    crear_entrenador2(coach2)
    print(coach1)



if __name__=='__main__':
    main()