import create_data_types as cdt 


def do_exercise_one(read_file, write_file):
	""" 
	Change to eventually accept file paths
	"""
	exercise_one = cdt.Stack()
	reading_file_object  = open(read_file, "r") 


	for line in reading_file_object:
		exercise_one.push(line)

	with open(write_file, "w") as writing_file_object:
		while not exercise_one.is_empty():
			backwards_line = exercise_one.pop()
			writing_file_object.write(backwards_line)