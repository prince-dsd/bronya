#!/bin/bash
set -eu
# poetry shell

# Run database migrations
# poetry run alembic upgrade head

# Start PM2 processes defined in the configuration file
pm2-runtime pm2.config.js

# Save the PM2 process list
#pm2 save

# Generate and configure the PM2 startup script
# pm2 startup | tail -n 1 | xargs sudo

# Display the status of PM2 processes
#pm2 status