Use ipywidgets to crop and adjust threshold values in a Jupyter notebook.

![](https://media.giphy.com/media/CWf6hu7Le6R9OwNasb/giphy.gif)

## Conda
* `conda create --name photolab_env`
* `conda activate photolab_env`
* `conda install jupyterlab`
* `conda install -c conda-forge/label/gcc7 nodejs`
* `conda install -n base -c conda-forge jupyterlab_widgets`
* `conda install ipywidgets`
* `conda install -c anaconda pillow`

## Pip:
* `pip install pdf2image`
* `pip install -U git+https://github.com/madmaze/pytesseract.git`

## Use
Use for individual and batch image cropping and levels adjusting.

Run ``test.py`` to confirm it's working. Use ``pdf_to_image.py`` to convert pdf to img > ``tesseract.sh`` to OCR > ``rename.sh`` to fix tesseract's naming convention. Drop files into ``collection`` for batch work. Modify ``Photolab.ipynb`` to your liking. ``convert.py`` can simply convert a pdf to text or a folder full of .png files to text.

## Docker
* `docker build -t photolab:latest .`
* `docker run --rm -it -p 8888:8888 photolab:latest`
