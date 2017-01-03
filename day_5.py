id = "ffykfhsq"

import hashlib

index = 0

password = "........"
l = list(password)

while '.' in password:
	to_hash = (id + str(index)).encode('utf-8')
	digest = hashlib.md5(to_hash).hexdigest()
	index += 1
	
	if digest[:5] == "00000":
		try:
			position = int(digest[5])
		except:
			continue
		char = digest[6]
		if 0 <= position <= 7:
			if l[position] == '.':
				l[position] = char
				password = ''.join(l)
				print(password)


print(password)