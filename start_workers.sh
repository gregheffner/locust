# This script starts multiple Locust worker processes to distribute load testing.
# 
# Variables:
#   NUM_WORKERS: The number of worker processes to start (default is 8).
#
# The script uses a for loop to start the specified number of worker processes.
# Each worker process is started in the background using the '&' operator.
# The workers connect to the Locust master running on localhost (127.0.0.1).
#!/bin/bash

NUM_WORKERS=8

for i in $(seq 1 $NUM_WORKERS); do
    locust -f locustfile.py --worker --master-host=127.0.0.1 &
done
