Installation
============

MEArec is a Python package and it can be easily installed using pip:

.. code-block:: python

    pip install MEArec


If you want to install from sources and be updated with the latest development you can install with:

.. code-block:: python

    git clone https://github.com/alejoe91/MEArec
    cd MEArec
    python setup.py install (or develop)

Requirements
------------

The following are the Python requirements, which are installed when running the pip installer.

- numpy
- click
- pyyaml
- matplotlib
- neo
- elephant
- h5py
- MEAutility (https://github.com/alejoe91/MEAutility)
- mpi4py
- LFPy

Installing NEURON
-----------------

The template generation requires NEURON. The code is tested using version 7.5,
that can be downloaded `here <https://neuron.yale.edu/ftp/neuron/versions/>`_. If you are running a Linux system
add:

.. code-block:: bash

    export PYTHONPATH="/usr/local/nrn/lib/python/:$PYTHONPATH"

to your .bashrc.

On Linux systems you also need install libncurses:

.. code-block:: bash

    sudo apt install lib32ncurses5-dev

Installing LFPy
---------------

LFPy is used to generate extracellular templates. It is not installed by default, but it can be easily installed with:

.. code-block:: bash

    pip install LFPy


Test the installation
---------------------

You can test that MEArec is correctly imported in python:

.. code-block:: python

    import MEArec as mr

And that the CLI is working. Open a terminal and run:

.. code-block:: bash

    mearec

You should get the list of available commands:

.. code-block:: bash

    Usage: mearec [OPTIONS] COMMAND [ARGS]...

        MEArec: Fast and customizable simulation of extracellular recordings on
        Multi-Electrode-Arrays

    Options:
      --help  Show this message and exit.

    Commands:
      default-config          Print default configurations
      gen-recordings          Generates recordings from TEMPLATES and...
      gen-templates           Generates EAP templates on multi-electrode arrays...
      recfromhdf5             Convert recordings from hdf5
      rectohdf5               Convert recordings to hdf5
      set-cell-models-folder  Set default cell_models folder
      set-recordings-folder   Set default recordings output folder
      set-recordings-params   Set default templates output folder
      set-templates-folder    Set default templates output folder
      set-templates-params    Set default templates output folder
      tempfromhdf5            Convert templates from hdf5
      temptohdf5              Convert templates to hdf5