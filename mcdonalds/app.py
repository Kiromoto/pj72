import os
import redis

from dotenv import load_dotenv
from pathlib import Path


load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

red = redis.Redis(host='redis-11852.c250.eu-central-1-1.ec2.cloud.redislabs.com',
                  port=11852,
                  password=os.getenv('REDIS_PASSWORD'),
                  )