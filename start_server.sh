#!/usr/bin/env bash

# Run script from its folder
CWD=$PWD
# Define repository location
LOCALREPO=rpviz
GITHUB=https://github.com/pablocarb
REPO=$GITHUB/${LOCALREPO}.git

# true for the cloud server, false for local installation
DEPLOY=true
if [ "$USER" == "pablo" ]; then
    DEPLOY=false
fi


# Stop an delete doe containers
docker stop $LOCALREPO
docker rm $LOCALREPO
docker rmi $LOCALREPO

# Update repository and change to production branch
if [ ! -d $LOCALREPO ]
then
    git clone $REPO $LOCALREPO
else
    cd $LOCALREPO
    git pull
    cd $CWD
fi

wget https://www.metanetx.org/cgi-bin/mnxget/mnxref/chem_prop.tsv -O rpviz/chem_prop.tsv

# Build new image
docker build -t $LOCALREPO .

# Stop and delete proxy containers
docker stop nginx-proxy
docker rm nginx-proxy

# Build new proxy image
docker build -t sbc/nginx-proxy -f ProxyDockerfile .

# Run container
if [ "$DEPLOY" == "true" ]; then
    docker run --name nginx-proxy -d -p 80:80 -v /var/run/docker.sock:/tmp/docker.sock:ro sbc/nginx-proxy
    docker run --name $LOCALREPO -d -p 8998:8998 -e LD_LIBRARY_PATH='/opt/conda/bin/../lib' -v $PWD:/apprpviz -e VIRTUAL_HOST=rpviz.synbiochem.co.uk $LOCALREPO
else
    docker run --name $LOCALREPO -p 8998:8998 -e LD_LIBRARY_PATH='/opt/conda/bin/../lib' -v $PWD:/apprpviz $LOCALREPO
fi

