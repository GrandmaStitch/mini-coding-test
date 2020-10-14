import code

input = [23, 23]

alist = []

for i in input:
	if len(str(i)) != 1:
		alist.append([int(j) for j in str(i)])
	else:
		alist.append(i)

print(alist)

store = []
for i in alist:
	if isinstance(i, list):
		new_list = code.find_letters(i)
		store.append(code.combination(new_list))
	else:
		blist = []
		blist.append(i)
		store.append(code.combination(code.find_letters(blist)))


res = code.combination(store)

for it in res:
	print(it, end=" ")