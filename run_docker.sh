#!/bin/bash
docker rm -f messycode-container  
docker build -t messycode-app .  
docker run --name messycode-container -it messycode-app