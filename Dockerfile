FROM continuumio/miniconda3

# Upgrade PIP
RUN pip install --upgrade pip

# Install pdf2image
RUN pip install pdf2image

# Install conda libraries
RUN conda install jupyterlab
RUN conda install -c conda-forge/label/gcc7 nodejs
RUN conda install -n base -c conda-forge jupyterlab_widgets
RUN conda install ipywidgets
RUN conda install -c anaconda pillow

# Download the latest Photolab files
RUN git clone https://github.com/jopvivi/ocr_photolab.git

# Set active working directory
WORKDIR /ocr_photolab

# Run when the build is complete
CMD ["jupyter-lab","--ip=0.0.0.0","--no-browser","--allow-root"]
