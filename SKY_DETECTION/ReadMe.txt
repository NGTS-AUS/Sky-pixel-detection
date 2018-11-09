Environment requirement: Anaconda Jupyter, Python 3.6
python package requirements: PIL, tensorflow, cv2, pymeanshift

File list:
checkpoint: Open it with NOTEPAD and change two paths to the corresponding paths in the environment to load model.ckpt
K&HSLcomb.ipynb: Main part of classification and sky detection (this is the only file needs execution) 
model.ckpt.data-00000-of-00001: classification model files
model.ckpt.index: classification model files
model.ckpt.meta: classification model files
Pymeanshiftcomb.py: Pymeanshift algorithm (called in K&HSLcomb.ipynb)

Folder list:
temp: temporarily used for storing classification. normally empty 
mark_output: storing all sky mark output of images 

Before start:
1.Open “checkpoint” with NOTEPAD and change two paths to the corresponding paths in the environment to load model.ckpt
2. Open K&HSLcomb.ipynb with jupyter and change “path1” & “path2” to corresponding local env path

Test Image Input:
1. Panorama images ended with “.png” and have word “panorama” in the filename 
2. If manual marking is provided, name the picture as the same name as the original pic but change the ‘.png’ to ‘ - Copy.png’
    	for example 1.png's manual marking is called 1 - Copy.png

Execution Steps:
1. Copy all the input pictures into the same folder
2. Run K&HSLcomb.ipynb with Jupyter (evaluation output shown if manual marking provided)
3. all outputs will be generated in the same folder and sky marking copies are also generated in folder “/mark_output”
