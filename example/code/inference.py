import json
from os import listdir
from os.path import isfile, join
import os
from time import sleep

def model_fn(model_dir, context=None):
	# Load the model and tokenizer from the model directory
	onlyfiles = [f for f in listdir(model_dir) if isfile(join(model_dir, f))]
	print(f'Loading blank model in {model_dir}')
	print('files:')
	print(onlyfiles)

	time_to_wait = 140
	startup_timeout = int(os.environ.get('SAGEMAKER_TS_STARTUP_TIMEOUT', 60))  
	print(f'We\'ll be waiting {time_to_wait} sec and the startup timeout is  {startup_timeout}')

	sleep(time_to_wait)


	print(f'We waited {time_to_wait} sec')
	model = None

	tokenizer = None
	return model, tokenizer

def input_fn(request_body, request_content_type):
	# Preprocess input data for the model
	return None

def predict_fn(input_data, model_and_tokenizer, context=None):
	# Perform prediction

	prediction = {'response': 'Hello word'}
	return prediction

def output_fn(prediction, content_type, context=None):
	print('returning results')
	print('prediction is: ')
	print(prediction)
	return json.dumps(prediction)
