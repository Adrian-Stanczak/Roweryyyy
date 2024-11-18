import json
import datetime
import smtplib
import os

rental_duration = float(input('Please, tell us how much time u will rent our bike (in hours): '))

def calculate_cost(rental_duration):
    if rental_duration > 1:
        counting = 10 + (5*(rental_duration - 1))
    elif rental_duration <= 1 and rental_duration > 0:
        counting = 10
    else: 
        print('Please, give me real time in hours !')
    
    print(counting)
calculate_cost(rental_duration)
