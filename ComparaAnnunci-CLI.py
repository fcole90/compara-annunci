#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ComparaAnnunci-CLI.py
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

def listaDiAnnunci(fileDiAnnunci):
    #crea la lista degli annunci
    lista = separaAnnunci(fileDiAnnunci)
    listaDiListe = []
    iterator1 = 0
    
    while iterator1 < len(lista):
        listaAnnuncio = []
        annuncio = lista[iterator1]
        
        # separa virgole e punti nel file
        simboliDaSeparare = [",",".",":","(",")","!","?"]
        for simbolo in simboliDaSeparare:
            annuncio = separaSimboli(annuncio,simbolo)
        
        listaDiParole = listaPeroleAnnuncio(annuncio)
        if len(listaDiParole) > 5:
            listaDiListe.append(listaDiParole)
        
        iterator1 += 1
    
    return listaDiListe
    
def iteraConfronto(ref_listaDiListe1,ref_listaDiListe2,mode=0):
    listaDiListe1 = ref_listaDiListe1[:]
    listaDiListe2 = ref_listaDiListe2[:]
    i1=0
    i2=0
    listaIndiciAnnunciVecchi = []
    listaAnnunciDaRimuovere = []
    while i2 < len(listaDiListe2):
        while i1 < len(listaDiListe1):
            if sonoSimili(listaDiListe2[i2],listaDiListe1[i1]) and listaDiListe2[i2]!=[] and listaDiListe1[i1]!=[]:
                listaIndiciAnnunciVecchi.append(i2)
                listaAnnunciDaRimuovere.append(listaDiListe2[i2])
                listaDiListe1[i1] = []
                break
            i1+=1
        i1=0
        i2+=1    
    
    if mode == 0:    
        return listaIndiciAnnunciVecchi
    else:
        return listaAnnunciDaRimuovere

def ricomponi(ref_lista):
    lista = ref_lista[:]
    full_text=""
    full_text+="*--------------------------------------------------*\n"
    full_text+="|             ANNUNCI DA RIMUOVERE                 |\n"
    full_text+="*--------------------------------------------------*\n\n"
    for annuncio in lista:
        testo = ""
        for item in annuncio:
            if testo != "" and item not in (",",".",":","(",")","!","?"):
                item = " " + item
            testo += item
        full_text+= testo + "\n\n"
    
    return full_text

def salva(nomeFile,content):
    f = open(nomeFile, "w")
    f.write("")
    f.write(content)
    f.close

def scegli(lista,i=0):
    ref_lista = lista[:]
    scelta = raw_input("Opera una scelta in base alle opzioni proposte: ")
    
    if scelta == "1":
        
        print ricomponi(ref_lista)
    
    elif scelta == "2":
        while True:
            nomeFile = raw_input("Come intendi chiamare il file? ")
            
            try:
                f = open(nomeFile, "r")
                f.close
                sovrascrivere = raw_input("Il file esiste già, desideri sovrascriverlo? (Predefinito=NO)")
                if sovrascrivere.lower() not in ("s","si","y","yes","ok"):
                    continue
                else:
                    salva(nomeFile,ricomponi(ref_lista))
                    break
            except: 
                salva(nomeFile,ricomponi(ref_lista))
                break
    
        print "File salvato con successo!"
    else:
        if i<2:
            print"Riprova, la tua scelta non è valida."
            i+=1
            scegli(lista,i)
    
        elif i==2:
            print "Non ci siamo proprio, per te nessuna sorpresa speciale!"
            i+=1
            scegli(lista,i)
        elif i==3:
            print "Adesso voglio proprio capire se lo stai facendo apposta!"
            i+=1
            scegli(lista,i)
        elif i>3:
            print "EASTER EGG UNLOCKED:\n\n\n"
            print "*-----------------------*"
            print "|MAGICARP usa SPLASH:   |"
            print "|ma non succede nulla.. |"
            print "*-----------------------*"
            i+=1
            scegli(lista,i)
    
    
    
    return
        


def main():

    print "SardegnaAnnunci ComparaAnnunci-CLI\n\n\n"
    #~ file1 = contenuto("annuncioA.txt") #debug
    #~ file2 = contenuto("annuncioNuovo.txt") #debug
    ##########Prende i nomi dei file########################
    nfile1= raw_input("Inserisci il nome del file vecchio: ")
    file1 = contenuto(nfile1)
    nfile2= raw_input("Inserisci il nome del fine nuovo: ")
    file2 = contenuto(nfile2)
    ########################################################
    
    listaAnnunciDaRimuovere = iteraConfronto(listaDiAnnunci(file1),listaDiAnnunci(file2),1)
    
    print "\n\nDesideri visualizzare gli annunci oppure salvarli in un file?"
    print "1) VISUALIZZA"
    print "2) SALVA"
    
    scegli(listaAnnunciDaRimuovere)
    
    goodbye = raw_input("\nPremi il tasto INVIO per uscire!")
    
    return 0

if __name__ == '__main__':
    
    from ComparaAnnunci import *
    import sys
    main()

