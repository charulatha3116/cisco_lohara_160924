import json
patients=[{'id':1,'name':'rahul'},{'id':2,'name':'modiji'}]
print(patients)
patients.append({'id':3,'name':'cbn'})
patients.append({'id':4,'name':'pk'})
print(f'after appending....\n{patients}')
patients=[patient for patient in patients if patient['id']!=3]
print(f'after removing\....n{patients}')
with open('qns2_patients.json','w') as file:
    json.dump(patients,file)
print('list of written to JSON file db.')
with open('qns2_patients.json','r') as file:
    patients2=json.load(file)
    print(f'patients....\n{patients2}')
