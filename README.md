# Giftubing

Giftubing allows the creation and use of a frame-based avatar.
It uses the webcam to get facial information for mouth and eyes limited animation.
Facial emotions are also detected, and if the model has corresponding emotions, it will match them (optional).

Currently in pre-alpha.

## Model

The model can be a GIMP project file (.xcf), or image files with alpha channel.
IMPORTANT: All images must have the same number of pixels in height and width.
Currently, the software knows which file does what through their name. A valid model could be:
```
body.png, mouth closed.png, mouth open.png, mouth wide.png, left eye closed.png, left eye open.png, right eye closed.png, right eye open.png 
```
The layers' stack order is: body, mouth, eye. 

## Installation

Details TBD
install Python, install Cuda, install pytorch matching cuda version, then pip install giftubing should finish setup.

## Usage

Inside a folder of your choice, create a .py file with the following lines:
```
from giftubing.main import start
start()
```
Then use console to run this file twice: first to create your avatar, second to launch it.
Two folders will be created next to the file: giftubing_sources inside which the model source files should be placed, and giftubing_avatars which will contain the created avatars.

Note: Once an avatar is created from a source, it will not appear as a choice for creation anymore.
If you wish to make another avatar from the same source (in a different resolution for exemple), 
go to giftubing_avatars folder and change the name of the previous one. The source will become
available for creation again.

## Citations

Giftubing uses an emotion recognition model from the following papers,
if you use these models please cite the following:

```BibTex
@inproceedings{savchenko2021facial,
  title={Facial expression and attributes recognition based on multi-task learning of lightweight neural networks},
  author={Savchenko, Andrey V.},
  booktitle={Proceedings of the 19th International Symposium on Intelligent Systems and Informatics (SISY)},
  pages={119--124},
  year={2021},
  organization={IEEE},
  url={https://arxiv.org/abs/2103.17107}
}
```

```BibTex
@inproceedings{Savchenko_2022_CVPRW,
  author    = {Savchenko, Andrey V.},
  title     = {Video-Based Frame-Level Facial Analysis of Affective Behavior on Mobile Devices Using EfficientNets},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Workshops},
  month     = {June},
  year      = {2022},
  pages     = {2359-2366},
  url={https://arxiv.org/abs/2103.17107}
}
```

```BibTex
@article{savchenko2022classifying,
  title={Classifying emotions and engagement in online learning based on a single facial expression recognition neural network},
  author={Savchenko, Andrey V and Savchenko, Lyudmila V and Makarov, Ilya},
  journal={IEEE Transactions on Affective Computing},
  year={2022},
  publisher={IEEE},
  url={https://ieeexplore.ieee.org/document/9815154}
}
```