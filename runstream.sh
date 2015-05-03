#!/bin/bash
#  stream video via http 
mjpg_streamer -i "/usr/local/lib/input_uvc.so -n -y -m -d  /dev/video0 -f 5 -r 800x600" -o "/usr/local/lib/output_http.so -w /usr/local/www - p 8080 -n"
