#!/bin/bash

# Start Flask app 1 in the background
python3 /usr/src/app/app.py &

# Start Flask app 2 in the background
python3 /usr/src/app/data.py &

# Start Nginx
nginx -g 'daemon off;'

