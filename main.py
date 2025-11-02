# This file is part of the game project "Tamagochi".
# Licensed under the GNU General Public License v3.0 or later.
# Copyright (C) 2025 Albertozj

print("importing resources")
import time as stime
import vrp
import os
vrp.runs + 1
print("done!")
stime.sleep(1)
vrp.name = vrp.name
vrp.alive = vrp.alive
zero = 0

print("###########################")
print("#        Tamagochi        #")
print("#          V.1.0          #")
print("# Albertozj Github GLP v3 #")
print("# tested for Python 3.13  #")
print("###########################")
#This project is licensed under the GLP v3. license
#This project is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.


def start():
    print("Welcome to Tamagochi!")
    stime.sleep(1)
    print("A game where you take care of a pet!")
    stime.sleep(1)
    print("You can feed it, play with it, and more!")
    stime.sleep(1)
    print("But be careful, if you don't take care of it, it might die...")
    stime.sleep(1)
    print("Good luck!")
    stime.sleep(2.8)


def savepet():
 with open("petd.dat", "w") as file:
    file.write(f"{vrp.name}\n")
    file.write(f"{vrp.hunger}\n")
    file.write(f"{vrp.happiness}\n")
    file.write(f"{vrp.energy}\n")
    file.write(f"{vrp.age}\n")
    file.write(f"{vrp.money}\n")
    file.write(f"{vrp.alive}\n")
    file.write(f"{vrp.runs}\n")
    file.write(f"{vrp.saves}\n")
    stime.sleep(1)
    print("Game needs to restart! Please press ctrl+c")
    stime.sleep(10000000000000000)
    print("game_saved!")

def new_game():
    print("Welcome! Type the name of your new pet :3!")
    name = input("Name your pet: ")
    stime.sleep(0.1)
    print(f"Your pet's name is {name}, right?")
    stime.sleep(0.7)
    right = input("? (y/n): ")
    if right == "y":
        vrp.name = name
        print(f"Great! Your pet's name is {vrp.name}!")
        print("saving Game...")
        savepet()
        print("Starting game...")
        stime.sleep(1.3)
        # HERE THE STORY DEF z.B.: K1()
        start()

def loadpet():
    if os.path.exists("petd.dat"):   # check ob Savefile existiert
        with open("petd.dat", "r") as file:
            lines = file.read().splitlines()
            # Daten zurück in vrp-Variablen schreiben
            vrp.name = lines[0]
            vrp.hunger = int(lines[1])
            vrp.happiness = int(lines[2])
            vrp.energy = int(lines[3])
            vrp.age = int(lines[4])
            vrp.money = int(lines[5])
            vrp.alive = (lines[6] == "True")
            vrp.runs = int(lines[7])
            vrp.save = True
            vrp.saves = int(lines[8])
            print("Savegame loaded!")
        return True
    else:
        new_game()
        return False

def check():
    loadpet()
    if vrp.saves == True:
     print("Your last pet died! Want to start a new life?")
     if os.path.exists("petd.dat"):
         os.remove("petd.dat")
     stime.sleep(1)
     new_game()

def check_resources():
    loadpet()

loadpet()

if vrp.name == "":
    check()

