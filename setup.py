from setuptools import setup, find_packages

with open("READMe.md", "r") as f:
    long_description = f.read()

setup(
    name="giftubing",
    packages=find_packages(),
    version='0.0.1',
    description='frame-based vtubing, create then use avatar',
    url="https://github.com/CaptainBTeach/giftubing",
    author="CaptainBTeach",
    long_description=long_description,

    install_requires = [
        "keyboard>=0.13.5",
        "facenet_pytorch>=2.5.2",
        "hsemotion>=0.2",
        "opencv-python>=4.6.0.66",
        "Pillow>=9.3.0",
        "PySide6>=6.4.0.1",
        "mediapipe>=0.9.0.1",
        "gimpformats>=2022.0.1",
        "pywin32==305"
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Operating System :: Microsoft :: Windows",
        "Environment :: GPU :: NVIDIA CUDA",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License"
    ],
    license="MIT"
)