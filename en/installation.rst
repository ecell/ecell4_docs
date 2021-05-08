Installation of the E-Cell System Version 4
=============================================

.. warning::

   E-Cell4 does NOT support Python **2** .

.. warning::

   E-Cell4 core binary package (called **ecell4_base**) for **Windows** (or **Mac**) is **NOT** distributed on PyPI. The package is distributed on **conda-forge**. Only (binary) package for **Linux** is distributed on PyPI.

Windows
--------

Install Miniforge3 from https://github.com/conda-forge/miniforge
and run the following command in **Miniforge Prompt** 
(On Windows, Start Menu -> Miniforge3 -> Miniforge Prompt (miniforge3)).

:: 

    conda install ecell4

Mac, Linux
-----------

Install Miniconda3 from https://github.com/conda-forge/miniforge
and run the following commands on your Terminal app.

:: 

    conda install ecell4

Linux environment where you can NOT use conda
----------------------------------------------

We provide `ecell4_base <https://github.com/ecell/ecell4_base>`__ **wheel** package only for Linux.
This is useful in environments like Google Colab where you can't use conda.
(On Linux) You can install (or upgrade) `ecell4_base <https://github.com/ecell/ecell4_base>`__ and `ecell4 <https://github.com/ecell/ecell4_base>`__ with

:: 

    python3 -m pip install ecell4

