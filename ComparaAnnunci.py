#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ComparaAnnunci.py
#  
#  Copyright 2013 fabio <fabio@fabio-EasyNote-TS11HR>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

def contenuto(filename):    #prova ad aprire un file e ne restituisce il contenuto sottoforma di stringa
    try:
        f = open(filename, "r")
        text = f.read()
        f.close
        return text
    except:
        print "Non è stato possibile aprire il file " + filename
        contenuto(nomeFile())
    
def nomeFile(): #chiede il nome del file da aprire
    return raw_input("Inserisci il nome del file che vuoi aprire: ")
    
def listaPeroleAnnuncio(annuncio):  #divide ogni stringa in una lista di parole
    return annuncio.split()
    
def separaSimboli(annuncio,simbolo):    #allontana i simboli dalle parole aggiungendo spazi
    lista = annuncio.split(simbolo)
    annuncioModificato = lista[0] + " "
    iterator = 1
    while iterator < len(lista):
        annuncioModificato += " " + simbolo + " " + lista[iterator]
        iterator += 1
    
    return annuncioModificato
    
def sonoSimili(cop_lista1,cop_lista2,uguaglianzaNecessaria=80):    #calcola la somiglianza tra gli elementi di due liste
    lunghezzaLista1 = len(cop_lista1)
    lunghezzaLista2 = len(cop_lista2)
    indiceDiUguaglianza = (lunghezzaLista1 + lunghezzaLista2)/2.0
    ugualiTrovati = 0
    #copia le liste in modo da non modificare quelle originali
    lista1 = cop_lista1[:]
    lista2 = cop_lista2[:]
    #attraversa le liste confrontando i loro elementi
    iterator1 = 0
    iterator2 = 0
    #ciclo 1
    while iterator1 < lunghezzaLista1:
        #ciclo 2
        while iterator2 < lunghezzaLista2:
            
         
            #print iterator1, iterator2, lista1[iterator1], lista2[iterator2], #debug
            #quando c'è l'ultimo elemento di ciclo 2 ed è diverso, allora toglie un'uguaglianza
            if (iterator2 == (lunghezzaLista2 - 1)) and (lista1[iterator1]!=lista2[iterator2]) and (lista2[iterator2]!="EMPTY"):
                ugualiTrovati -= 1
                #print "fine ciclo, -1" #debug
                break
            #quando due elementi sono uguali aggiunge un punto di uguaglianza
            elif lista1[iterator1]==lista2[iterator2]:
                ugualiTrovati += 1 #aggiuge un punto quando trova un'uguaglianza
                #print "sono uguali", "\n" #debug
                lista2[iterator2] = "EMPTY"
                #esce dal ciclo 2 quando sono uguali in modo da non creare ripetizioni
                break
            #else:
                #print "diversi" #debug
            
            #print "\n"   #debug
            
            iterator2 += 1
            #print "CICLO2 resume"  #debug
            
            #fine ciclo 2 
        #print "CICLO1 resume"  #debug
        iterator2 = 0
        iterator1 += 1
        #fine ciclo 1
        
    #formula per trasformare i dati in percentuale
    if ugualiTrovati:
        percUguaglianza = (ugualiTrovati*100)/indiceDiUguaglianza
    else:
        percUguaglianza = 0
        
    if percUguaglianza>=uguaglianzaNecessaria:
        return True
    else:
        return False
           
def separaAnnunci(stringaDiAnnunci):    #scompone il file in una lista di annunci
    listaAnnunci = []
    #~ string = ""
    #~ for item in stringaDiAnnunci.split("\n"):
        #~ if item != "":
            #~ if string:
                #~ string += item 
            #~ else:
                #~ string = item
        #~ 
    #~ if string != "":
        #~ listaAnnunci.append(string)
        #~ string = ""
        
    for item in stringaDiAnnunci.split("\n"):
        if item != "":
            listaAnnunci.append(item)

    return listaAnnunci



if __name__ == '__main__':
    
    print separaAnnunci(contenuto("annuncioA.txt"))
