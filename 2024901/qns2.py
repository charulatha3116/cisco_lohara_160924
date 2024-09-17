names_list=input("enter student names (seperated by space):").split()
names_set=set(names_list)
names_fset=frozenset(names_set)
names_dict={name:len(name) for name in names_fset}
print(f'Original list:{names_list}')
print(f'set (no duplicates):{names_set}')
print(f'frozenset:{names_fset}')
print(f'dictionary of name lengths: {names_dict}')
import json
with open('qns2_data.json','w') as file:
    json.dump(names_dict,file)
print('dictionary written to JSON file.')
with open('qns2_data.json','r') as file:
    names_dict2=json.load(file)
    print(f'Reading from JSON file....\n{names_dict2}')