# -*- coding: utf-8 -*-
"""Projet scrabble.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1s-tFA57wgefq_vgK2J1xpMVYlmyI552G

Projet Scrabble Python
"""

import random
"""
Cyril Mathé
Arthur Boutry
"""
easy = ["soleil","wifi", "page","livre","lune","plage"]
medium = ["toran","kayak","bizarre","insolite","subtil"]
hard = ["parapluie","television","labyrinthe","innovant","nostalgie"]

def choose_words(n):
  words_choosen_easy = random.sample(easy, n)
  words_choosen_medium = random.sample(medium, n)
  words_choosen_hard = random.sample(hard, n)
  return words_choosen_easy,words_choosen_medium,words_choosen_hard

def regroup_words(m1,m2,m3):
  rm1 = "".join(m1)
  rm2 = "".join(m2)
  rm3 = "".join(m3)
  return rm1,rm2,rm3

def shuffle_words(shuffle_rm1,shuffle_rm2,shuffle_rm3):
  l_rm1 = random.sample(shuffle_rm1,len(shuffle_rm1))
  l_rm2 = random.sample(shuffle_rm2,len(shuffle_rm2))
  l_rm3 = random.sample(shuffle_rm3,len(shuffle_rm3))
  return l_rm1,l_rm2,l_rm3

def supp_double1(shuffled_words):
  nw_rm1 = ""
  for caractere in shuffled_words:
    if caractere not in nw_rm1:
        nw_rm1 = nw_rm1 + caractere
  return nw_rm1

def jouer():
  wordsEasy,wordsMedium,wordsHard = choose_words(3)
  mot1E,mot2E,mot3E = wordsEasy
  mot1M,mot2M,mot3M = wordsMedium
  mot1H,mot2H,mot3H = wordsHard
  # Appel regroupe_words avec le résultat de choose_wors
  regrouped_easy, regrouped_medium, regrouped_hard = regroup_words(wordsEasy,wordsMedium,wordsHard)
  # Appel shuffle_words avec le résultat de regroupe_words
  shuffled_easy, shuffled_medium, shuffled_hard = shuffle_words(regrouped_easy, regrouped_medium, regrouped_hard)
  # Appel supp_double avec le résultat de shuffle_words
  shuffle_words_easy,shuffle_words_medium,shuffle_words_hard = supp_double1(shuffled_easy),supp_double1(shuffled_medium),supp_double1(shuffled_hard)
  print("Bienvenu dans le jeu du scrabble !")

  liste = [mot1E,mot2E,mot3E,mot1M,mot2M,mot3M,mot1H,mot2H,mot3H]
  i = 0
  p = 0
  j = 9
  print("Manche 1")

  while i < 3:
    print("Liste de lettres disponible :",shuffle_words_easy)
    print("Entrer un mot !")
    mot = input()
    if mot == "quit":
      print("Manche suivante")
      i = i + 3
    elif mot != mot1E and mot != mot2E and mot != mot3E:
      print("Faux")
    elif mot == mot1E or mot == mot2E or mot == mot3E:
      liste.remove(mot)
      print("Bon")
      p = p + 1
      print(p,"/",j)
      i = i + 1

  i = 0
  print("Manche 2")
  while i < 3:
    print("Liste de lettres disponible :",shuffle_words_medium)
    print("Entrer un mot !")
    mot = input()
    if mot == "quit":
      print("Manche suivante")
      i = i + 3
    elif mot != mot1M and mot != mot2M and mot != mot3M:
      print("Faux")
    elif mot == mot1M or mot == mot2M or mot == mot3M:
      liste.remove(mot)
      print("Bon")
      p = p + 1
      print(p,"/",j)
      i = i + 1
  i = 0
  print("Manche 3")
  while i < 3:
    print("Liste de lettres disponible :",shuffle_words_hard)
    print("Entrer un mot !")
    mot = input()
    if mot == "quit":
      print("Résultat")
      i = i + 3
    elif mot != mot1H and mot != mot2H and mot != mot3H:
      print("Faux")
    elif mot == mot1H or mot == mot2H or mot == mot3H:
      liste.remove(mot)
      print("Bon")
      p = p + 1
      print(p,"/",j)
      i = i + 1
  print("Bien joué tu as",p,"point sur",j)
jouer()