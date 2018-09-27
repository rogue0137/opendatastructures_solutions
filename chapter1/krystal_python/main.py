import sys
import do_exercises as de
import datetime  

exercise = sys.argv[1]
input_filename = sys.argv[2]
output_filename = ("/Users/krystalflores/github/opendatastructures_solutions/chapter1/krystal_python/exercise_" + exercise + ".txt")

""" TO DO:
Add logging instead of print?
"""

if exercise == '1':
	print(datetime.datetime.now())
	de.do_exercise_one(input_filename, output_filename)
	print(datetime.datetime.now())
else:
	print("That is not an option")



