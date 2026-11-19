import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
language= input("select language (english/japanese/chinese/french)")
def print_pokemon():
    for pokemon in data:
        if language in pokemon ['name']:
            print(pokemon['name'][language])
        else:
            print ("language not found")
            break
# print_pokemon()
# def pokemon_type():
#      find_type=input("what pokemon type you want to find?")
#      for pokemon in data:
#          if find_type in pokemon['type']:
#              print(pokemon['name'][language])
# pokemon_type()
def name_pokemon():
    find_pokemon= input("what Pokemon are you searching for?")
    for pokemon in data:
         if find_pokemon in pokemon['name']:
             print(pokemon['name'][language])
name_pokemon()
# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.(done)
# Add a language choice feature and print the pokemons name based on the user input (done)
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user(done)
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!
