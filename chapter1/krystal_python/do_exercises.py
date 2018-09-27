import create_data_types as cdt 


def do_exercise_one():
	""" 
	Change to eventually accept file paths
	"""
	exercise_one = cdt.Stack()
	reading_file_object  = open("/Users/krystalflores/github/opendatastructures_solutions/chapter1/krystal_python/small.txt", "r") 


	for line in reading_file_object:
		exercise_one.push(line)

	with open("/Users/krystalflores/github/opendatastructures_solutions/chapter1/krystal_python/exercise_one.txt", "w") as writing_file_object:
		while not exercise_one.is_empty():
			backwards_line = exercise_one.pop()
			writing_file_object.write(backwards_line)