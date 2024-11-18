# sagemaker_pytorch_user_defined

This is just a modified version of https://github.com/aws/sagemaker-pytorch-inference-toolkit with only the sagemaker_pytorch_serving_container changed.  
The idea is to change the module by adding the parameter for startup timeout.

## What does it do?
An example have been provided, it will run a local sagemaker session using the user gpu, the inference script will wait 140 seconds
which is way more than the classic 60 seconds timeout where as the startup timeout have been set up to 143 seconds, that way you can see 
that the startup timeout is working, if you put it below the 140 seconds of waiting time it will produce a timeout error

## The requirements
1. An account with sso
2. aws sagemaker modules installed
3. A gpu with cuda toolkit installed

## How do I run it?

1. go into the docker folder and run the build.sh script
2. in config_inference.json change the value of  aws_access_key_id, aws_secret_access_key and aws_session_token
3. run the python script deploy_local.py, after a while it should print 'We waited 140 sec'
