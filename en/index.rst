.. image:: ./ecell-logo-with-title.png

########################
E-Cell System version 4
########################

The E-Cell System is a software platform for modeling, simulation and analysis of complex, heterogeneous and multi-scale systems like the cell.
Its latest version, E-Cell4, accepts multi-algorithms, multi-timescales and multi-spatial-representations as its central feature.
E-Cell4 is a free and open-source software licensed under the GNU General Public License version 3. The source code is available on GitHub (`ecell4 <https://github.com/ecell/ecell4>`__ and `ecell4_base <https://github.com/ecell/ecell4_base>`__).

*************
Installation
*************

.. toctree::
   :maxdepth: 2

   installation

*********
Features
*********

- Single particle simulations, i.e. `The enhanced Green's Function Reaction Dynamics (eGFRD) method <http://gfrd.org>`__, `Spatiocyte <http://spatiocyte.org>`__ (a lattice-based method), and the Reaction Brownian Dynamics (RBD) method
- Ordinary differential equations, Gillespie algorithm (the direct method), and spatial Gillespie algorithm (the next subvolume method)
- Rule-based modeling
- Python programmable

**********
Tutorials
**********

.. toctree::
   :maxdepth: 2

   top
   tutorials/index

*******
Models
*******

.. toctree::
   :maxdepth: 2

   examples/index
   tests/index

***************
For Developers
***************

.. toctree::
   :maxdepth: 2

   developers

*********
Citation
*********

If this package contributes to a project which leads to a scientific publication, I would appreciate a citation.

.. image:: https://zenodo.org/badge/6348303.svg
   :target: https://zenodo.org/badge/latestdoi/6348303

****************
Licensing terms
****************

This product is licensed under the terms of the `GNU General Public License v3 <https://github.com/ecell/ecell4_base/blob/master/LICENSE>`__. 
See also `LICENSE <https://github.com/ecell/ecell4_base/blob/master/LICENSE>`__ for the software included in this product

- Copyright (c) 2010-, RIKEN

All rights reserved.

****
API
****

.. toctree::
   :maxdepth: 2

   api/ecell4
   api/ecell4_base
   api/index
