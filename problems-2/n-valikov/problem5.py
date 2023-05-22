def solve(n: int) -> [int]:
	result = [2] if n > 1 else []
	result.extend(
		[number for number in range(3, n + 1, 2) if number % 2 and all(
			[number % divisor for divisor in
			 range(3, int(number ** 0.5) + 1, 2)])])
	return result


if __name__ == '__main__':
	print("Please, print a number.")
	print(solve(int(input())))
