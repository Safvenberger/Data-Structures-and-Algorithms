# -*- coding: latin-1 -*-

#Written by Lena Kallin Westin <kallin@cs.umu.se>. Bug fixed 2012-08-24 by Johan Eliasson
#May be used in the course Datastrukturer och Algoritmer (Python) at Ume� University.
#Usage exept those listed above requires permission by the author.
# File has been changed 2020-02-18; the lookup method has been altered to implement a move-to-front algorithm.

from DirectedList import DirectedList

"""
Datatypen Tabell enligt definitionen p� sidan 117 i Lars-Erik Janlert,
Torbj�rn Wiberg Datatyper och algoritmer 2., [rev.] uppl.,Lund,
Studentlitteratur, 2000, x, 387 s. ISBN 91-44-01364-7

Variabler och funktioner som inleds med ett enkelt underscore "_" �r privata
f�r klassen och ska inte anv�ndas av de som anv�nder denna klass.

Denna klass implementerar tabell med hj�lp av en riktad lista
"""
class Table:

    def __init__(self):
        """
            Syfte: Skapar en tom tabell med hj�lp av en riktad lista
            Returv�rde: -
            Kommentarer: I boken heter denna funktion Empty. 

        """	        
        self._table = DirectedList()
      
    def insert(self, key, obj):
        """
            Syfte: ut�kar eller omdefinierar tabellen s� att nyckeln key kopplas 
                   till v�rdet obj
            Returv�rde: -
            Kommentarer: Det kr�vs att key �r en typ som kan j�mf�ras med 
                    likhet. Om det �r en egen klass m�ste man �verladda 
                    funktionen __eq__
        """
        if self.isempty():
            self._table.insert(self._table.first(), (key, obj))
        else:
            found = False
            pos = self._table.first()
            while (not found) and (not self._table.isEnd(pos)):
                (newKey, newObj) = self._table.inspect(pos)
                if newKey == key:
                    found = True
                    pos = self._table.remove(pos)
                    pos = self._table.insert(self._table.first(), (key, obj)) 
                pos = self._table.next(pos)
            if not found:
                self._table.insert(self._table.first(), (key, obj))
        
    def isempty(self):
        """
            Syfte: Testar om tabellen �r tom
            Returv�rde: Returnerar sant om tabellen �r tom, annars falsk
            Kommentarer: 
        """        
        return self._table.isempty()

    def lookup(self, key):
        """
            Syfte: Ser efter om tabellen inneh�ller nyckeln key och flyttar i s� fall
                   fram nyckeln till b�rjan av tabellen, och returnerar v�rdet 
                   som �r kopplat till nyckeln
            Returv�rde: Returnerar en tuppel (true, obj) d�r obj �r v�rdet som 
                   �r kopplat till nyckeln om nyckeln finns och annars (false, None)
            Kommentarer: Om k�n �r tom returneras (false, None).
                         Uppdaterad 2020-02-18.                         
        """
        pos = self._table.first()
        while not self._table.isEnd(pos):
            (newKey, newObj) = self._table.inspect(pos)
            if newKey == key:
                obj = self._table.inspect(pos)                      # New 20-02-18
                pos = self._table.remove(pos)                       # New 20-02-18 
                pos = self._table.insert(self._table.first(), obj)  # New 20-02-18
                return (True, newObj)
            pos = self._table.next(pos)
        return (False, None)
        
    def remove(self, key):
        """
            Syfte: Tar bort nyckeln key och dess sammankopplade v�rde.
            Returv�rde: -
            Kommentarer: Om nyckeln inte finns s� h�nder inget med tabellen
        """        
        if not self.isempty():
            found = False
            pos = self._table.first()
            while (not found) and (not self._table.isEnd(pos)):
                (newKey, newObj) = self._table.inspect(pos)
                if newKey == key:
                    found = True
                    pos = self._table.remove(pos)
                else:
                    pos = self._table.next(pos)   
