photolab requirements:

conda create --name photolab_env
conda activate photolab_env
conda install jupyterlab
conda install -c conda-forge/label/gcc7 nodejs
conda install -n base -c conda-forge jupyterlab_widgets
conda install ipywidgets
conda install -c anaconda pillow

pdf2image requirements (optional):
pip install pdf2image