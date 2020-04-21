Installation of the E-Cell System version 4
=============================================

Here shows how to install the E-Cell System version 4.

Installation
--------------

E-Cell4 does not support Python2.

E-Cell4 does not support :code:`pip install` on Windows and Mac.

Windows
^^^^^^^^

Install Miniconda with Python 3.7 for **64-bit** (from https://docs.conda.io/en/latest/miniconda.html)
and run this command on **Anaconda Prompt**.

:: 

    conda install -c ecell ecell4

Mac, Linux
^^^^^^^^^^^^

Install Miniconda with Python 3.7 for **64-bit** (from https://docs.conda.io/en/latest/miniconda.html)
and run these commands on your Terminal app.

:: 

    conda config --add channels conda-forge
    conda install -c ecell ecell4

Linux environment where you can NOT use conda
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:: 

    python3 -m pip install ecell4
