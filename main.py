#!usr/bin/python
#use-python
import math

def is_prime(num: int) -> bool:

	i: int = 1	while i <= math.sqrt(num):

		if i > 1 and num % i == 0:

			return True

		i += 1

	return False

	

	

bil: int = int(input("Bilangan: "))

while bil < 1:

	bil = int(input("Maaf, masukan ulang bilangan dengan benar: "))

print(is_prime(bil))
