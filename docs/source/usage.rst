Usage
=====

Command-line interface
----------------------

The CLI is available through the ``ng20lda`` command with subcommands.

Fetch documents
~~~~~~~~~~~~~~~

.. code-block:: bash

   ng20lda fetch comp.graphics 5 output_data

Train an LDA model
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   ng20lda train output_data/comp_graphics models/lda.pkl --n-topics 10

Describe a document
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   ng20lda describe output_data/comp_graphics/0.txt models/lda.pkl --n-topics 3 --n-words 5

Count lines in a file
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   ng20lda count output_data/comp_graphics/0.txt

HTTP API
--------

Run the API with:

.. code-block:: bash

   uvicorn ng20lda.api:app --reload

Endpoints:

- ``POST /describe`` with JSON body ``{"document_path": "...", "model_path": "..."}``.
- ``POST /visualize`` with JSON body ``{"document_path": "...", "model_path": "..."}``.
