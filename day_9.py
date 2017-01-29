input = """
ADVENT
A(1x5)BC
(3x3)XYZ
A(2x2)BCD(2x2)EFG
(6x1)(1x3)A
X(8x2)(3x3)ABCY
""".strip()

import re


def decode(s):
	print("s", s)
	# TODO: can't use split here, because having two consecutive markers
	# should treat the second marker as normal data
	tokens = [x for x in re.split(r'[\(\)]', s)
	          if x != ""]

	result, expand = "", False
	for token in tokens:

		m = re.match(r'(\d+)x(\d+)', token)

		if expand:
			if m:  # handle edge case
				token = "(" + m.group(0) + ")"
			expanded = token[:letters] * times
			token = expanded + token[letters:]

		if m and not expand:
			letters, times = int(m.group(1)), int(m.group(2))
			expand = True
			continue

		expand = False
		result += token

	return result

for s in input.split('\n'):
	print("result", decode(s))
	print()
