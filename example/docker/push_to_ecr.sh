aws ecr get-login-password --region <region> --profile profile-admin | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com
docker build -t test-inference-pytorch24  . --no-cache
docker tag test-inference-pytorch24 :latest <account-id>.dkr.ecr.<region>.amazonaws.com/test-inference-pytorch24 :latest
docker push <account-id>.dkr.ecr.<region>.amazonaws.com/test-inference-pytorch24 :latest
