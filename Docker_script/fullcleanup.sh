#!/bin/bash

echo "Stopping all running containers..."
docker stop $(docker ps -aq) 2>/dev/null

echo "Removing all containers..."
docker rm $(docker ps -aq) 2>/dev/null

echo "Removing all images..."
docker rmi $(docker images -q) -f 2>/dev/null

echo "Removing unused Docker volumes..."
docker volume prune -f

echo "Removing unused Docker networks..."
docker network prune -f

echo "Removing unused Docker build cache..."
docker builder prune -f

echo "✅ Full cleanup complete!"