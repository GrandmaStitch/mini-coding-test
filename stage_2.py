# /usr/local/bin/python3.7

import code

# Transform two-digit number into a two elements list
# Return a list that generates all digits from input and makes each digit as
# single digit
def break_digits(input):
	alist = []
	for i in input:
		if len(str(i)) != 1:
			alist.append([int(j) for j in str(i)])
		else:
			alist.append(i)
	return alist

# Return a list that stores all mapping letters
def letter_combinations(l):
	combination_list = []
	for i in l:
		# Two-digit number combinations
		if isinstance(i, list):
			alist = code.find_letters(i)
			combination_list.append(code.combination(alist))
		else:
			blist = []
			blist.append(i)
			combination_list.append(code.combination(code.find_letters(blist)))
	return combination_list


if __name__ == "__main__":
	input = [23, 23]
	lists = letter_combinations(break_digits(input))
	res = code.combination(lists)
	for it in res:
		print(it, end=" ")

