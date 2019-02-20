def flex(*args):
	total = 0;
	for a in args:
		total+=a;
	return total;

b = flex(23,24,56,76,898)

print(b)