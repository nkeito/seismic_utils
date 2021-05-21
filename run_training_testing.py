import os
import argparse
parser = argparse.ArgumentParser()

#-db DATABSE -u USERNAME -p PASSWORD -size 20
parser.add_argument("-e", "--train", help="Training argument")
parser.add_argument("-p", "--test",  help="Testing argument")


args = parser.parse_args()

valid_flag = True
filename = ""
executable = ""

if args.train is not None:
	print("\t\tTraining")
	filename = args.train
	executable = "tf_predictor.py"

elif args.test  is not None:
	print( "\t\tTesting" )
	filename = args.test
	executable = "loadresults.py"
else:
	print( "\t\tPlease provide a valid flag!\n" )
	print( "\t\t-e <filename> for training " )
	print( "\t\t-p <filename> for testing\n\n" )
	valid_flag = False 

if valid_flag:
	path = os.path.abspath("/".join( filename.split("/")[:-1] ))
	filename = filename.split("/")[-1]

	command = "docker run --rm -it  \
	-v {0}/DNNRegressors:/home/regresor_python/DNNRegressors  \
	-v {0}:/tmp \
	-w /home/regresor_python aneria/seismic_utils:latest  \
	python3  {1} /tmp/{2}".format( path, executable ,filename   )

	os.system(command)

