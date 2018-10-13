from setuptools import setup, find_packages

long_description = open("README.md").read()

setup(
    name="MEArec",
    version="0.1",
    author="Alessio Buccino",
    author_email="alessiob@ifi.uio.no",
    description="Fast and customizable simulation of extracellular recordings on Multi-Electrode-Arrays.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alejoe91/MEArec",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)  ",
        "Operating System :: OS Independent",
    ],
    # packages=['MEArec'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'numpy',
        'pyyaml',
        'matplotlib',
        'neo',
        'elephant',
        'h5py',
        'mpi4py',
        'LFPy'
    ],
    entry_points={'console_scripts': 'mearec=MEArec.cli:cli'}
)