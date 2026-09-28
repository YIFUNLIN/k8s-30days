import time
import os
import redis
from fastapi import FastAPI

app = FastAPI()

REDIS_HOST = os.getenv(
    "REDIS_HOST",
    "redis"
)

redis_client = redis.Redis(
    host = REDIS_HOST,
    port = 6379,
    decode_responses = True
)

@app.get('/')
def root():
    
    visits = redis_client.incr("visits")
    
    return {
      "message":"Hello from GitOps!",
      "visits": visits
    }

@app.get('/health/live')
def live():
    return {
      "status":"alive" 
   } 

@app.get('/work')
def work():
  end_time = time.time()+0.2
  counter = 0
  while time.time() < end_time:
    counter += 1
  return {
    "iterations": counter
}







