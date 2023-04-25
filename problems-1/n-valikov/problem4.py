def common_print_first(to_print: str) -> None:
	print(
		2 * f"{to_print.capitalize()} green bottle"
		    f"{'' if to_print == 'one' else 's'} hanging on the wall,"
		    f"\n",
		end='')


def common_print_second(to_print: str) -> None:
	print(
		f"There'll be {to_print} green bottle"
		f"{'' if to_print == 'one' else 's'} hanging on the wall.")


def solve() -> None:
	words = ['ten', 'nine', 'eight', 'seven', 'six', 'five', 'four', 'three',
	         'two', 'one', 'no']
	for i in range(len(words) - 2):
		common_print_first(words[i])
		print("And if one green bottle should accidentally fall,")
		common_print_second(words[i + 1])
	common_print_first(words[-2])
	print("If that one green bottle should accidentally fall")
	common_print_second(words[-1])


if __name__ == '__main__':
	solve()
