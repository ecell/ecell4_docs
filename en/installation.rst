Installation of the E-Cell System Version 4
=============================================

Here shows how to install the E-Cell System version 4.

.. warning::

   E-Cell4 does NOT support Python2 and Python3 32-bit.

.. warning::

   E-Cell4 (`ecell4_base <https://github.com/ecell/ecell4_base>`__) package does NOT support :code:`pip install` on Windows and Mac. Please use :code:`conda` instead.

Windows
--------

Install Miniconda with Python 3.7 for **64-bit** (from https://docs.conda.io/en/latest/miniconda.html)
and run this command on **Anaconda Prompt** 
(On Windows, Start Menu -> Anaconda3 (64-bit) -> Anaconda Prompt or Anaconda Powershell Prompt).

:: 

    conda install -c ecell ecell4

Mac, Linux
-----------

Install Miniconda with Python 3.7 for **64-bit** (from https://docs.conda.io/en/latest/miniconda.html).
and run these commands on your Terminal app.

:: 

    conda config --add channels conda-forge
    conda install -c ecell ecell4

Linux environment where you can NOT use conda
----------------------------------------------

We provide `ecell4_base <https://github.com/ecell/ecell4_base>`__ **wheel** package only for Linux.

(On Linux) You can install (or upgrade) `ecell4_base <https://github.com/ecell/ecell4_base>`__ and `ecell4 <https://github.com/ecell/ecell4_base>`__ with

:: 

    python3 -m pip install ecell4

