#!/bin/bash

NUM_WORKERS=8

for i in $(seq 1 $NUM_WORKERS); do
    locust -f locustfile.py --worker --master-host=127.0.0.1 &
done
