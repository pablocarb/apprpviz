# Docker file that installs docker container for Selprom
#
# build with: "sudo deocker build -t Dockerfile ."

# Install basic image
FROM continuumio/anaconda3

# Install additional tools
RUN conda install -c conda-forge flask-restful=0.3.6
RUN conda install -c sbmlteam python-libsbml
RUN conda install -c anaconda networkx
RUN conda install -c anaconda beautifulsoup4
RUN conda install -c rdkit rdkit

# Start the server
ENTRYPOINT ["python"] 
CMD ["/apprpviz/rpvizServe.py"]

# Open server port
EXPOSE 8998
