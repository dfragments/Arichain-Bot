#!/bin/bash

while true; do
    echo "Checking for existing bot processes..."
    
    # Kill any running bot processes
    pkill -f "python3 bot.py"
    sleep 5  # Give time for termination

    echo "Starting bot..."
    
    # Automatically select option 3 (Run Without Proxy)
    echo "3" | python3 bot.py

    echo "Bot process completed. Waiting 12 hours before restarting..."
    
    # Wait 12 hours before restarting
    sleep 43200  
done

