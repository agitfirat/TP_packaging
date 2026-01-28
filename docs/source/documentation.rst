Documentation
=============

Generate API docs from the package docstrings with ``sphinx-apidoc`` and then
build the HTML documentation.

.. code-block:: bash

   sphinx-apidoc -o docs/source/api ng20lda
   cd docs
   make html

The generated HTML output is available in ``docs/build/html``.
