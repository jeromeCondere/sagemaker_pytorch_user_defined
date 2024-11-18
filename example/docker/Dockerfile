FROM 763104351884.dkr.ecr.us-east-1.amazonaws.com/pytorch-inference:2.4.0-gpu-py311-cu124-ubuntu22.04-sagemaker




ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE


COPY src/sagemaker_pytorch_serving_container_user_defined /usr/local/bin/sagemaker_pytorch_serving_container_user_defined

COPY example/docker/dockerd-entrypoint.py /usr/local/bin/dockerd-entrypoint.py


ENTRYPOINT ["python", "/usr/local/bin/dockerd-entrypoint.py"]
CMD ["torchserve", "--start", "--ts-config", "/home/model-server/config.properties", "--model-store", "/home/model-server/"]