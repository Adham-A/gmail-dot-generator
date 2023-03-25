import csv
import time
from sympy.utilities.iterables import multiset_permutations
import numpy as np

email = input("Write your email here without the domain (@gmail.com) : \n")
DOMAIN = "@gmail.com"

to_permute = np.empty(len(email)-1, dtype='U1')
filename = f"emails_{time.strftime('%Y-%m-%dT%H-%M-%S')}.csv"  # generate unique filename with timestamp

with open(filename, 'w', newline='', encoding='UTF-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['email'])

    for i in range(len(email)):
        to_permute[:i] = np.full(i, '.', dtype='U1')

        for p in multiset_permutations(to_permute):
            dotted_email = ''.join(map(''.join, zip(email, p)))
            writer.writerow([f"{dotted_email}{email[-1]}{DOMAIN}"])
