#!/usr/bin/env bash

# Run script from its folder
CWD=$PWD
# Define repository location
LOCALREPO=doebase
GITHUB=https://github.com/pablocarb
REPO=$GITHUB/${LOCALREPO}.git

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
if [ ! -d $LOCALREPO ]
then
    git clone $REPO $LOCALREPO
else
    cd $LOCALREPO
    git pull
    cd $CWD
fi

# Build new image
docker build -t doe .

# Run container
if [ "$DEPLOY" == "true" ]; then
    docker run --name nginx-proxy -d -p 80:80 -v /var/run/docker.sock:/tmp/docker.sock:ro jwilder/nginx-proxy
    docker run --name doe -d -p 8989:8989 -e LD_LIBRARY_PATH='/opt/conda/bin/../lib' -v $PWD:/appoptdes -e VIRTUAL_HOST=doe.synbiochem.co.uk doe
else
    docker run --name doe -p 8989:8989 -e LD_LIBRARY_PATH='/opt/conda/bin/../lib' -v $PWD:/appoptdes doe
fi

