import json
patients={1:{'name':'rahul'},2:{'name':'modiji'}}
print(patients)
print(type(patients))
patients[3]={'name':'cbn'}
patients[4]={'name':'pk'}
print(f'after appending....\n{patients}')
if 4 in patients:del patients[4]
print(f'after removing\....n{patients}')
with open('qns2_patients.json','w') as file:
    json.dump(patients,file)
print('list of written to JSON file db.')
with open('qns2_patients.json','r') as file:
    patients2=json.load(file)
    print(f'patients....\n{patients2}')
