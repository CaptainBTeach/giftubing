from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="giftubing",
    packages=find_packages(),
    version='0.0.2',
    description='frame-based vtubing, create then use avatar',
    url="https://github.com/CaptainBTeach/giftubing",
    author="CaptainBTeach",
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires = [
        "keyboard",
        "hsemotion",
        "opencv-python",
        "Pillow",
        "PySide6",
        "mediapipe",
        "gimpformats",
        "facenet-pytorch"
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