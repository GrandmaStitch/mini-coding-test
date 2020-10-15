# /usr/local/bin/python3.7

# Mapping of each digit to letters
board = {
	1: ['1'], 2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'],
	4:['g', 'h', 'i'], 5:['j', 'k', 'l'], 6:['m', 'n', 'o'],
	7:['p', 'q', 'r', 's'], 8:['t', 'u', 'v'], 9:['w', 'x', 'y', 'z'],
	'*': ['*'], 0: ['0'], '#': ['#']
}


# Return a list that contains all letters mapped from input
def find_letters(input):
	temp_list = []
	for i in input:
		temp_list.append(board[i])
	return temp_list


# Lists combination, return all possible letter combinations from the input list
def combination(lists):
	try:
		import reduce
	except:
		from functools import reduce
	fn = lambda x: reduce(
		lambda x, y: [str(i) + str(j) for i in x for j in y], x)
	return fn(lists)


def styling(l):
	for it in l:
		print(it, end=" ")

if __name__ == "__main__":
	input = [2, 3]
	lists = find_letters(input)
	res = combination(lists)
	styling(res)




