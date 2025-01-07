import json

appointments = {}

file_path = "dane.txt"

'''Sprawdza czy podany numer telefonu zawiera 9 cyfr'''
def validate_phone_number(phone_number):
    if len(phone_number) == 9:
        return True
    else:
        return False




'''Sprawdcza czy plik istnieje ze ścieżki'''
def check_file_exists(file_path):
    if open(file_path):
        return True
    else:
        return False




'''Wczytuje i zwraca listę zapisanych wizyt z pliku'''
def get_appointments_from_file(file_path):
    if check_file_exists(file_path):
        file = open(file_path,"r")
        return json.load(file)
    else:
        return False
    



'''Sprawdza czy jest dostępny termin na podaną datę'''
def check_availability(appointments, date):
    if appointments.get(date):
        print(len(appointments[date]))
        if len(appointments[date]) < 8:
            return True
        else:
            appointments[date] = {}
            return False
    else:
        appointments[date] = {}
        return True
    



'''Zapisuje dane wizyty w pliku'''
def save_appointment(appointments, file_path, phone_number, date, time):
    if not validate_phone_number(phone_number):
        print("invalid phone")
        return False
    if not check_availability(appointments,date):
        return False

    appointments[date][time] = phone_number

    file = open(file_path,"w")
    json.dump(appointments,file)
    file.close()



'''Wyświetla listę dostępnych godzin wizyt na podaną datę'''
def show_available_hours(appointents, date):
    if appointments.get(date):
        print("Dostępne godziny:")
        for i in range(8,16):
            if appointents[date].get(str(i)):
                print(f"Godzina {i} jest zajęta przez nr telefonu {appointents[date][str(i)]}")
            else:
                print(f"Godzina {i} jest dostępna")
    else:
        print("Dostępne są wszystkie godziny 8-16")

def validate_time(time):
    if time.isnumeric() and int(time) >= 8 and int(time) <= 16:
        return True
    else:
        return False

appointments = get_appointments_from_file(file_path)
appointments = {}
print(appointments)
save_appointment(appointments, file_path,"123456789","1/1/2025","8")

def mainloop():
    print("System umawiania wizyt u dentysty")
    print("Program automatycznie wczytuje i zapisuje dane do pliku")
    print("Opcja 1: Dodaj wizytę")
    print("Opcja 2: Sprawdź listę dostępnych godzin")
    print("Opcja 3: Wyświetl wszystkie wizyty")
    print("Opcja 4: Wyjdz z programu")
    option = input("Wybierz opcję: \n -> ")
    if option == "1":
        print("OPCJA: Dodaj wizytę")
        date = input("Podaj datę na którą chcesz dodać wizytę: \nPrzykładowa data: 1/1/2025 \n -> ")
        time = input("Podaj godzinę na którą chcesz dodać wizytę (8-16): \nPrzykładowa godzina: 8 \n -> ")
        if not validate_time(time):
            print("BŁĄD: Podano nieprawidłową godzinę")
            return
        phone_number = input("Podaj nr. telefonu pacjenta: \nPrzykładowy numer tel.: 123456789 \n -> ")
        if not validate_phone_number(phone_number):
            print("BŁĄD: Podano nieprawidłowy nr. telefonu")
            return
        save_appointment(appointments,file_path,phone_number,date,time)
    elif option == "2":
        date = input("Podaj datę na której chcesz sprawdzić dostępne godziny: \nPrzykładowa data: 1/1/2025 \n -> ")
        show_available_hours(appointments,date)
    elif option == "3":
        print(appointments)
    elif option == "4":
        exit()
    else:
        print("BŁĄD: Podana opcja nie istnieje")

while True:
    mainloop()
    input("Naciśnij enter by kontynować...")
