#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Install Node.js dependencies
npm install

# Run Flask app in the background
python app.py &

# Run SvelteKit app in the background
npm run dev &

# Wait for all background processes to finish
wait
