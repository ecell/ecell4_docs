For Developers
===============

Repositories
--------------

* https://github.com/ecell/ecell4
* https://github.com/conda-forge/ecell4-feedstock
* https://pypi.org/project/ecell4/

* https://github.com/ecell/ecell4_base
* https://github.com/conda-forge/ecell4_base-feedstock
* https://pypi.org/project/ecell4-base/

* https://github.com/ecell/ecell4_docs
* https://readthedocs.org/projects/ecell4-docs/

When you need to compile ecell4_base by yourself
--------------------------------------------------

Please refer to https://github.com/ecell/ecell4_base/blob/master/azure-pipelines.yml

:: 

   pip install setup.py install

Releasing :code:`ecell4`
---------------------------

GitHub
^^^^^^^

1. Update ecell4_base version in https://github.com/ecell/ecell4_base/blob/master/setup.py
#. Git tag push v\*.\*.\* to ecell4_base. GitHub Actions automatically create the new release. You do NOT need to create the release by yourself.
#. Write release note based on the **pull requests**.

PyPI
^^^^^

1. Update cmake and gsl versions in https://github.com/ecell/manylinux-dockerimage/blob/master/Dockerfile with the latest conda-forge
#. Update boost version in https://github.com/ecell/ecell4_base/blob/master/.circleci/config.yml with the latest conda-forge
#. Check :code:`pip install THE_CIRCLECI_ARTIFACT_PYTHONWHEEL` in Google Colab
#. twine upload the manylinux wheel

conda-forge
^^^^^^^^^^^^

1. Sync https://github.com/ecell/ecell4_base-feedstock with upstream.
#. Create new branch to https://github.com/ecell/ecell4_base-feedstock and checkout it.
#. Update meta.yaml
   - version
   - build:number: to 0.
   - sha256 checksum
#. `Rerender feedstocks <https://conda-forge.org/docs/maintainer/updating_pkgs.html#rerendering-feedstocks>`__.
#. Send pull request to https://github.com/conda-forge/ecell4_base-feedstock/blob/master/recipe/meta.yaml

How to release :code:`ecell4` (not :code:`ecell4_base`)
---------------------------------------------------------

GitHub
^^^^^^^

1. Update version in setup.py
#. Create release with GitHub releases

PyPI
^^^^^

1. pip install twine
#. python setup.py sdist
#. twine upload dist/*
