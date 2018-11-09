Environment requirement: Anaconda Jupyter, Python 3.6
python package requirements: PIL, tensorflow,

File list:

CNN v2.3.ipynb: Main code of CNN classification.
*.npz: Including BigBuilding.npz, skycloudcontrast.npz, Treetop.npz, Buildingtop.npz. They are the pixel data which converted from the orginal images. Used for CNN training.

Folder list:
Image Processing: Over 480 images used for training and testing. There is a file named "Image processing.ipynb" in this folder. It is the code of converting the image to data.

Training output:
The output is the trained model which has four files. They are: 'model.ckpt.data-00000-of-00001', 'model.ckpt.index', 'model.ckpt.meta', 'checkpoint which are moved to the 
SKY_DETECTION folder as the input used for doing classification.