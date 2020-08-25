import os

check = True
while check:
    with open('present.txt') as file:
        m, n = [int(i) for i in file.readline().split()]

    if n <=363:
        os.system('python "to_vm for_large_scale v2.py"')
    else:
        check=False
