import json
patients=[
    {'id':1,'name':'rahul'},
    {'id':2,'name':'modiji'},
    {'id':3,'name':'cbn'}
]
patients_str= json.dumps(patients)
print(patients, patients_str)
with open ('patients_data.json','w') as patients_db:
    json.dump(patients,patients_db)
patients_list2=json.loads(patients_str)
print(patients_list2, type(patients_list2))
with open('patients_data.json','r') as patients_db:
    patients_list3=json.load(patients_db)
    print(patients_list3,type(patients_list3))