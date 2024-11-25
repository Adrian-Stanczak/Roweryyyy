import json , smtplib, os
from datetime import datetime

rental_duration = float(input('Please, tell us how much time u will rent our bike (in hours): '))

file_path = "data/rentals.json"

def rent_bike(customer_name, rental_duration):
    cost = calculate_cost()
    rental = { 
        'custommer_name':customer_name,
        'rental_duration':rental_duration,
        'cost':cost
        'rental_time':datetime.now().strftime('')
    }
    save_rental(rental)
    return f'Save_rental {rental}'
    
    pass

def calculate_cost(rental_duration:int) -> int:
    '''Calculate the cost of bike rental'''
    if rental_duration > 1:
        counting = 10 + (5*(rental_duration - 1))
    elif rental_duration <= 1 and rental_duration > 0:
        counting = 10
    else: 
        print('Please, give me real time in hours !')
    print(counting)
calculate_cost(rental_duration)

def save_rental(rental:dict):
    '''Save rental to rentals.json'''
    rentals = []
            #openning a file
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            rentals = json.load(file)
    rentals.append(rental)
            #saving in file rentals and adding indexing
    with open(file_path, 'w') as file:
        json.dump(rentals, file, index = 4)