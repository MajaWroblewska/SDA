from time import sleep
import random
from sender2 import Sender
from sorting_facility import SortingFacility

number_of_days = 3  #

senders = (Sender("Jan Kowalski", "Tczew"),) #, by sender był iterowalny jako tupla
           # Sender("Maria Rutkowska", "Rumia"),
           # Sender("Jerzy Brzuszek", "Wejherowo"))

facility = SortingFacility()    #inicjalizacja klasy z plikiu sorting.py

for _ in range(number_of_days):
    for sender in senders:
        parcels = sender.prepare_parcels(random.randint(2, 10)) #dostajemy paczki
        facility.take_parcels_from_sender(parcels)# przekazyjemy do sortowni
        # facility.long_parcels() #zad 32
        print(facility.parcels_sorted_by_destination) # -> {'Gdansk': [lista paczek...],

    sleep(1)