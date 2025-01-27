import datetime

with open(r'task.txt', 'a') as file:
    file.write(f'{datetime.datetime.now()} - the script run \n')