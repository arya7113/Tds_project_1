#!/bin/bash

IMAGE_NAME="arya7113/tdsproj1"

echo "Building Docker image: $IMAGE_NAME..."
docker build -t $IMAGE_NAME .

if [ $? -eq 0 ]; then
    echo "✅ Build successful!"
else
    echo "❌ Build failed!"
fi