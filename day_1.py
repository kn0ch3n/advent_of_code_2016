# http://adventofcode.com/2016/day/1#
path_str = """
L4, R2, R4, L5, L3, L1, R4, R5, R1, R3, L3, L2, L2, R5, R1, L1, L2, R2, R2, L5, R5, R5, L2, R1, R2, L2, L4, L1, R5, R2, R1, R1, L2, L3, R2, L5, L186, L5, L3, R3, L5, R4, R2, L5, R1, R4, L1, L3, R3, R1, L1, R4, R2, L1, L4, R5, L1, R50, L4, R3, R78, R4, R2, L4, R3, L4, R4, L1, R5, L4, R1, L2, R3, L2, R5, R5, L4, L1, L2, R185, L5, R2, R1, L3, R4, L5, R2, R4, L3, R4, L2, L5, R1, R2, L2, L1, L2, R2, L2, R1, L5, L3, L4, L3, L4, L2, L5, L5, R2, L3, L4, R4, R4, R5, L4, L2, R4, L5, R3, R1, L1, R3, L2, R2, R1, R5, L4, R5, L3, R2, R3, R1, R4, L4, R1, R3, L5, L1, L3, R2, R1, R4, L4, R3, L3, R3, R2, L3, L3, R4, L2, R4, L3, L4, R5, R1, L1, R5, R3, R1, R3, R4, L1, R4, R3, R1, L5, L5, L4, R4, R3, L2, R1, R5, L3, R4, R5, L4, L5, R2
""".strip()
path = path_str.split(", ")

get_direction = {
	("U", "L"): "L",
	("D", "L"): "R",
	("L", "L"): "D",
	("R", "L"): "U",
	("U", "R"): "R",
	("D", "R"): "L",
	("L", "R"): "U",
	("R", "R"): "D",
}


def walk(path, position=None, direction="U"):
	if position is None:
		position = [0, 0]
	visited, first_twice = [], None

	for command in path:
		turn, steps = (command[0], int(command[1:]))
		direction = get_direction[(direction, turn)]

		for i in range(steps):  # walk one step at a time
			if direction == 'L':
				position[0] -= 1
			if direction == 'R':
				position[0] += 1
			if direction == 'U':
				position[1] -= 1
			if direction == 'D':
				position[1] += 1

			if position in visited and first_twice is None:
				first_twice = position[:]
			visited.append(position[:])

	return (position, first_twice)


def distance(position):
	try:
		return abs(position[0]) + abs(position[1])
	except TypeError:
		print("position {} does not have valid values.".format(position))


end_position, first_twice = walk(path)
print("End position distance to [0, 0]: {}".format(distance(end_position)))
print("First position visited twice: {}".format(first_twice))
print("First position visited twice distance to [0, 0]: {}".format(distance(first_twice)))
