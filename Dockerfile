# Docker file that installs docker container for Selprom
#
# build with: "sudo docker build -t Dockerfile ."

# Install basic image
FROM continuumio/miniconda3

# Install additional tools
RUN conda install -c conda-forge flask-restful=0.3.6
RUN conda install -c sbmlteam python-libsbml
RUN conda install -c anaconda networkx
RUN conda install -c anaconda beautifulsoup4
RUN conda install -c conda-forge xorg-libxrender
RUN conda install -c anaconda lxml
RUN conda install -c anaconda ipython
RUN conda install -c conda-forge py2cytoscape 
RUN conda install -c rdkit rdkit
RUN conda install -c mcs07 cirpy 
RUN conda install -c bioconda pubchempy

# Start the server
ENTRYPOINT ["python"] 
CMD ["/apprpviz/rpvizServe.py"]

# Open server port
EXPOSE 8998
