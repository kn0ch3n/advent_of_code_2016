input = "abba[mnop]qrst"



def is_abba(txt):
	# TODO: do this for strings of any length
	if txt[:2] == txt[:1:-1]:
		return True
	return False

