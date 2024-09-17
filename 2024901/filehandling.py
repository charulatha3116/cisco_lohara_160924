console_list=input('enter the word')
list=console_list.split()
tuple=()
for i in list:
    tuple+=(i,)
print(list)
print(tuple)

with open("newline.txt","w") as file:
    file.write(f'list: {list}\n')
    file.write(f'tuple: {tuple}\n')

lines=["first line\n","second line\n","third line\n"]
with open("newline.txt","r") as file:
    file.writelines(lines)
    print(file)
