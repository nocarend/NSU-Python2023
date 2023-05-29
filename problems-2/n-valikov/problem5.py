def solve(n: int) -> [int]:
	return [number for number in range(2, n + 1) if (number % 2 and all(
		[number % divisor for divisor in
		 range(3, int(number ** 0.5) + 1, 2)]) or number == 2)]


if __name__ == '__main__':
	print("Please, print a number.")
	from sys import stderr

	try:
		number = int(input())
	except ValueError:
		stderr.write("Ожидалось натуральное число. Например: 7")
		exit(1)
	except EOFError:
		stderr.write("Закончились входные данные.")
		exit(1)
	except Exception:
		stderr.write("Случилось что-то плохое.")
		exit(1)
	print(solve(number))
