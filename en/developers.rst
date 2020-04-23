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
_________________________________________________

Please refer to https://github.com/ecell/ecell4_base/blob/master/azure-pipelines.yml

:: 

   pip install setup.py install

Releasing :code:`ecell4`
---------------------------

GitHub
^^^^^^^

1. Update ecell4_base version in https://github.com/ecell/ecell4_base/blob/master/setup.py
1. Git tag push v\*.\*.\* to ecell4_base. GitHub Actions automatically create the new release. You do NOT need to create the release by yourself.
1. Write release note based on the **pull requests**.

PyPI
^^^^^

1. Update cmake and gsl versions in https://github.com/ecell/manylinux-dockerimage/blob/master/Dockerfile with the latest conda-forge
1. Update boost version in https://github.com/ecell/ecell4_base/blob/master/.circleci/config.yml with the latest conda-forge
1. Check :code:`pip install THE_CIRCLECI_ARTIFACT_PYTHONWHEEL` in Google Colab
1. twine upload the manylinux wheel

conda-forge
^^^^^^^^^^^^

1. Sync https://github.com/ecell/ecell4_base-feedstock with upstream.
1. Create new branch to https://github.com/ecell/ecell4_base-feedstock and checkout it.
1. Update meta.yaml
   - version
   - build:number: to 0.
   - sha256 checksum
4. `Rerender feedstocks <https://conda-forge.org/docs/maintainer/updating_pkgs.html#rerendering-feedstocks>`__.
5. Send pull request to https://github.com/conda-forge/ecell4_base-feedstock/blob/master/recipe/meta.yaml

How to release :code:`ecell4` (not :code:`ecell4_base`)
---------------------------------------------------------

GitHub
^^^^^^^

1. Update version in setup.py
1. Create release with GitHub releases

PyPI
^^^^^

1. pip install twine
1. python setup.py sdist
1. twine upload dist/*
