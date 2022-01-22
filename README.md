Adjust documents for OCR from the comfort of Jupyter Lab.

## Setup
* `conda create --name photolab_env`
* `conda activate photolab_env`
* `conda install jupyterlab`
* `conda install -c conda-forge/label/gcc7 nodejs`
* `conda install -n base -c conda-forge jupyterlab_widgets`
* `conda install ipywidgets`
* `conda install -c anaconda pillow`

## pdf2image requirements (optional):
* `pip install pdf2image`

## Use
Use for individual and batch image cropping and levels adjusting.

Run ``test.py`` to confirm it's working. Use ``pdf_to_image.py`` to convert pdf to img > ``tesseract.sh`` to OCR > ``rename.sh`` to fix tesseract's naming convention. Drop files into ``collection`` for batch work. Modify ``Photolab.ipynb`` to your liking.
