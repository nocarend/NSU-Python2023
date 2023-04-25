import math
import time

import bitarray


def sieve_of_Eratosthenes_list(N: int):
	numbers_list = list(range(N))
	for index in range(2, math.ceil(math.sqrt(N)) + 1):
		if numbers_list[index] > 0:
			for eratosthenesIndex in range(index * 2, N, index):
				numbers_list[eratosthenesIndex] = 0
	return list(filter(lambda x: x > 1, numbers_list))


def sieve_of_Eratosthenes_set(N: int):
	numbers_set = {number for number in range(2, N)}
	for number in range(2, math.ceil(math.sqrt(N)) + 1):
		if number in numbers_set:
			for deletion_number in range(number * 2, N, number):
				if deletion_number in numbers_set:
					numbers_set.remove(deletion_number)
	return numbers_set


def sieve_of_Eratosthenes_bitarray(N: int):
	numbers_bitarray = bitarray.bitarray('1' * N)
	numbers_bitarray[0:2] = 0
	for index in range(2, math.ceil(math.sqrt(N)) + 1):
		if numbers_bitarray[index]:
			numbers_bitarray[index * 2:N:index] = 0
	return numbers_bitarray.search(1)


if __name__ == '__main__':
	N: int = 100000000
	N += 1
	start_time: float = time.time()
	sieve_of_Eratosthenes_list(N)
	print(f'List: {(time.time() - start_time):.5f}s')
	start_time: float = time.time()
	sieve_of_Eratosthenes_bitarray(N)
	print(f'Bitarray: {(time.time() - start_time):.5f}s')
	start_time: float = time.time()
	sieve_of_Eratosthenes_set(N)
	print(f'Set: {(time.time() - start_time):.5f}s')
