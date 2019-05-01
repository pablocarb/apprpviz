#!/usr/bin/env bash

# Run script from its folder
CWD=$PWD
# Define repository location
GITHUB=https://github.com/pablocarb
REPO=$GITHYB/doebase.git
# true for the cloud server, false for local installation
DEPLOY=true
if [ "$USER" == "pablo" ]; then
    DEPLOY=false
fi

# Stop and delete proxy containers
docker stop nginx-proxy
docker rm nginx-proxy

# Stop an delete selprom containers
docker stop doe
docker rm doe
docker rmi doe

# Update repository and change to production branch
rm -rf doebase
git clone $REPO doebase

# Build new image
docker build -t doe .

# Run container
if [ "$DEPLOY" == "true" ]; then
    docker run --name nginx-proxy -d -p 80:80 -v /var/run/docker.sock:/tmp/docker.sock:ro jwilder/nginx-proxy
    # Run container with user's uid to avoid permission issues when updating the repository
    docker run -u `id -u $USER` --name selprom -d -p 7700:7700 -e LD_LIBRARY_PATH='/opt/conda/bin/../lib' -e VIRTUAL_HOST=selprom.synbiochem.co.uk  -v $CWD/sbc-prom:/selprom selprom 
else
    # Run container with user's uid to avoid permission issues when updating the repository
    docker run -u `id -u $USER` --name doe -d -p 8989:8989 -e LD_LIBRARY_PATH='/opt/conda/bin/../lib' -v $CWD/appoptdes:/appoptdes doe 
fi

