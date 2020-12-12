import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gnn2",
    version="1.0",
    author="Niccolo' Pancino, Pietro Bongini",
    author_email="niccolo.pancino@unifi.it",
    description="Graph Neural Network Tensorflow 2.x implementation",
    long_description=long_description,
    url="https://github.com/NickDrake117/GNN_tf_2.x",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)