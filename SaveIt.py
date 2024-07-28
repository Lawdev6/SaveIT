##########################################################
#                                                        #
#   https://t.me/EPANAFR  https://discord.gg/D3rFRxAS3H  #
#             https://github.com/Lawdev6                 #
#                                                        #
#                                                        #
##########################################################
#[Copyright] Law.dev | Little program SaveIT !           #
##########################################################

import os
import sqlite3
import time
from colorama import Fore

os.system("title SaveIT/[By Law]")
user = os.getenv("USERNAME")

conn2 = sqlite3.connect(f'SaveIT-{user}.db')
cursor2 = conn2.cursor()

cursor2.execute('''CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')

def verifier_utilisateur(username2, password2):
    cursor2.execute('''SELECT * FROM user WHERE username = ? AND password = ?''', (username2, password2))
    utilisateur = cursor2.fetchone()
    if utilisateur:
        return True
    else:
        return False

def ajouter_utilisateur(username2, password2):
    cursor2.execute('''INSERT INTO user (username, password) VALUES (?, ?)''', (username2, password2))
    conn2.commit()
    print(f"{Fore.LIGHTGREEN_EX}Utilisateur ajouté avec succès")
    os.system("cls")

Vice = input(f'''{Fore.LIGHTGREEN_EX}                    
             
             
             
             [1] = Enregistreur de données sécurisée | [2] = Voir mes données sécurisée 
                                
              
                                            (SaveIT/{user}) | ''').lower()
if Vice == '1':
    os.system("cls")
    username2 = input(f"{Fore.LIGHTGREEN_EX}Indiquez votre nom d'utilisateur : ")
    password2 = input(f"{Fore.LIGHTGREEN_EX}Indiquez votre mot de pass : ")
    ajouter_utilisateur(username2, password2)
    os.system("cls")
    print(f'''{Fore.LIGHTGREEN_EX}Vos données sont sécurisée et chifrées !''')
    time.sleep(3)


if Vice == '2':
    os.system("cls")
    conn2 = sqlite3.connect(f'SaveIT-{user}.db')
    cursor2 = conn2.cursor()

    cursor2.execute("SELECT * FROM user")
    rows1 = cursor2.fetchall()
    print('''
          
______Mes données sécurisée________
''')
           
    for row1 in rows1:
       print(row1)

    conn2.close()
    print('''
___________________________________
          
''')
time.sleep(10)


