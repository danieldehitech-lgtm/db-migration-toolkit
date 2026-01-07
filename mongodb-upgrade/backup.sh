#!/bin/bash

# Full MongoDB backup
mongodump --uri="$MONGO_URI" --out ./backup

echo "MongoDB backup completed"
