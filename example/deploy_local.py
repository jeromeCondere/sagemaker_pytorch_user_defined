import sagemaker
import boto3
import botocore
from sagemaker.huggingface import HuggingFaceModel
import json
from sagemaker.local import LocalSession
import os
import pathlib




with open('config_inference.json') as f:
    data = json.load(f)
    region = data['region']
    aws_access_key_id=data['aws_access_key_id']
    aws_secret_access_key=data['aws_secret_access_key']
    aws_session_token=data['aws_session_token']
    endpoint_name=data['endpoint_name']
    role = data['role']

os.environ['AWS_DEFAULT_REGION'] = region

os.environ['AWS_ACCESS_KEY_ID']=aws_access_key_id
os.environ['AWS_SECRET_ACCESS_KEY']=aws_secret_access_key
os.environ['AWS_SESSION_TOKEN']=aws_session_token


local_sagemaker_session = LocalSession()
local_sagemaker_session.config = {'local': {'local_code': True}}




ecr_image="test-inference-pytorch24"

model_path = "file://" + str(pathlib.Path(__file__).parent.joinpath("model.tar.gz"))


env = {
'SAGEMAKER_TS_STARTUP_TIMEOUT': '143', #value to increase
}


huggingface_model = HuggingFaceModel(
    model_data=model_path,
    role=role,
    transformers_version="4.26.0",
    pytorch_version="1.13.1",          
    py_version="py39",
    entry_point = 'inference.py',
    source_dir = 'code',
    image_uri=ecr_image,
    env = env,
    sagemaker_session=local_sagemaker_session  
)



predictor = huggingface_model.deploy(
    initial_instance_count=1, 
    instance_type="local_gpu",  
    endpoint_name=endpoint_name
)



print('Deploying...\n\n')


