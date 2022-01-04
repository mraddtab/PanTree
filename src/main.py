"""
Program Name: PanTree
Author: Ronald Chen
Date Created: 12/23/2021
Program Summary: PanTree is a program designed with college students in mind. The user can input what
                 ingredients they have at hand and be greeted with thousands of recipes. This software 
                 accesses a database of hundreds of thousands of recipes, ingredients, and ratings. 
Inputs: Ingredients
Outputs: Recipes
Additional Info: Data is from https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions 
"""

import sys
import os
import pickle
import csv
from tkinter.constants import N


aval_ingredients = [] #Aval ingredients
aval_recipes = []
recipes = {}     # {Recipe Ids:Recipe Object}
ingredients = {} # {Ingredient Ids: Ingredient Object}
class Recipe:
    def __init__(self,id, name, minutes, tags, nutrition, n_steps, steps, description, ingredients, n_ingredients):
        self.id = id
        self.name = name
        self.tags = tags
        self.nutrition = nutrition
        self.ingredients = ingredients
        self.description = description
        self.steps = steps
        self.minutes = minutes
        self.n_ingredients = n_ingredients
        self.n_steps = n_steps
class Ingredient:
    def __init__(self, raw_ingr, raw_words, processed, len_proc, replaced, count, id):
        self.raw_ingr = raw_ingr
        self.raw_words = raw_words
        self.proccessed = processed
        self.len_proc = len_proc
        self.replaced = replaced
        self.count = count
        self.id  = id
def name(recipe):
    return recipe.name
def raw_ingr(ingr):
    return ingr.raw_ingr
def replaced(ingr):
    return ingr.replaced
def proccessed(ingr):
    return ingr.proccessed
"""
Function Name: init_data()
Function Purpose: Scan "RAW_recipes.csv" to create recipe objects which
                  will be added to the list 'recipes', and "ingr_map.pkl"
                  to create Ingredient objects. 
Inputs: 'data/RAW_recipes.csv', 'data/ingr_map.pkl'
Outputs: recipes: List[Recipe] is filled with 231,637 Recipe objects.
         ingredients: List[Ingredient] is filled with 11659 Ingredients.
"""
def init_data():
    # Get recipes
    with open('data/RAW_recipes.csv', mode = 'r', encoding="utf8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for line in csv_reader:
            if line_count == 0:
                line_count += 1
            recipe_obj = Recipe(name = ' '.join(line['name'].split()).strip(),id = line['id'], minutes = line['minutes'], tags = line['tags'], nutrition= line['nutrition'], n_steps = line['n_steps'],
            steps = line['steps'], description= line['description'], ingredients= line['ingredients'], n_ingredients= line['n_ingredients'])
            #Remove special characters from recipe_obj.ingredients, and convert it to a list.
            specialChars ='[\']'
            for c in specialChars:
                recipe_obj.ingredients = recipe_obj.ingredients.replace(c,'')
            recipe_obj.ingredients = recipe_obj.ingredients.split(',')
            for i in range(0, len(recipe_obj.ingredients)):
                recipe_obj.ingredients[i] = recipe_obj.ingredients[i].strip()
            recipes[recipe_obj.id] = recipe_obj
        print("Recipes Collected: " + str(len(recipes)))
    #Get Ingredients
    with open('data/ingr_map.pkl', mode= 'rb') as pickle_file:
        data = pickle.load(pickle_file)
        for i in range(0, len(data['id'])):
            ingr_obj = Ingredient(raw_ingr= data['raw_ingr'][i], raw_words= data['raw_words'][i], processed= data['processed'][i],
            len_proc= data['len_proc'][i], replaced= data['replaced'][i], count = data['count'][i], id = data['id'][i])
            ingredients[ingr_obj.id] = ingr_obj
        print("Ingredients Collecte: " + str(len(ingredients)))


"""
Function Name: input_ingredients
Function Purpose: This function will allow display the ingredients to the user, and 
                  prompt them to input the ingredients they have. Not working on 
                  the GUI yet, so just allow inputs atm with numbers.
Inputs: ingredient objects.
Outputs: ingridents added to aval_ingredients.
"""
#def input_ingredients():
    #Display ingredients w/ Index
    #Organize by seasoning, herbs, protein, veggies
    #User input
    #Add to aval_ingredients

#MAIN
init_data()
