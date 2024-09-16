patients=[]

'''1-add
    2-remove'''

def patient_add(patient):
    global patients
    patients.append(patient)

def patient_remove(patient):
    global patients
    try:
        patients.remove(patient)
    except ValueError as err:
        print('no such patient')
def menu():
    choice = int(input('''1- add
        2- remove
        3- end 
        your choice '''))
    if choice == 1:
        patient=input('enter patient')
        patient_add(patient)
        print(patient)

    elif choice == 2:
        patient=input('enter patient')
        patient_remove(patient)
        print(patient)
        
def menus():
    choice=menu()
    while choice!=3:
        choice=menu()
    print('app end')
menus()
