board = {
	1: ['1'], 2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'],
	4:['g', 'h', 'i'], 5:['j', 'k', 'l'], 6:['m', 'n', 'o'],
	7:['p', 'q', 'r', 's'], 8:['t', 'u', 'v'], 9:['w', 'x', 'y', 'z'],
	'*': ['*'], 0: ['0'], '#': ['#']
}

# input = input('What digit(s) do you want convert? ').split(', ')
# input = [2, 3]


def find_letters(input):
	temp_list = []
	for i in input:
		temp_list.append(board[i])
	return temp_list


def combination(lists):
	try:
		import reduce
	except:
		from functools import reduce
	fn = lambda x: reduce(
		lambda x, y: [str(i) + str(j) for i in x for j in y], x)
	return fn(lists)


if __name__ == "__main__":
	input = [2, 6]

	lists = find_letters(input)

	res = combination(lists)

	for it in res:
		print(it, end=" ")



