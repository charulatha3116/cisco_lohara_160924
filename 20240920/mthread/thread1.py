'''import threading

def print_numbers():
    for i in range(5):
        print(i)
        

thread = threading.Thread(target=print_numbers)
thread.start()  # Start the thread
thread.join()   # Wait for the thread to finish
'''

"""import time
import threading

def print_numbers():
    thread_id = threading.get_ident()
    for i in range(5):
        print(f'@{thread_id}:{i}')
        time.sleep(1)



thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_numbers)
thread1.start()  # Start the thread
thread2.start()  # Start the thread
#thread1.join()   # Wait for the thread to finish
#thread2.join()   # Wait for the thread to finish
print_numbers()"""


'''import time
import threading

def print_numbers():
    for i in range(500):
        print(i)
        time.sleep(0.025)


thread = threading.Thread(target=print_numbers)
thread.start() 


print_numbers()'''


import time
import threading

def print_numbers():
    id = threading.get_ident()
    for i in range(5):
        print(f'{i}@{id}')
        #time.sleep(0.025)

threads=[]
for i in range (5):
    thread = threading.Thread(target=print_numbers)
    threads.append(thread)
    thread.start() 
for i in range(5):
    thread.join()

print_numbers()
