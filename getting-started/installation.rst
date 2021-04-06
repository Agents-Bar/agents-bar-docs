Installation
============

To connect your application to our agents you'll need to download a client.
We currently provide a Python client but feel free to let us know if you want a client in a different version.

Python client
-------------

The client is called `ai-traineree-client` and it is accessible through the `pypi <https://pypi.org/project/ai-traineree-client/>`_.
It's suggested to either add the package name to your dependency file, e.g. `requirements.txt`,
or download it direclty using pip,

.. code-block::
    :linenos:

    $ pip install ai-traineree-client

.. note::
    We recommend having a separate python environment per project so to avoid dependency issues.
    The easiest way is to create and activate python's virtual environment (venv)
    ::

        $ python -m venv .venv
        $ source .venv/bin/activate
        (.venv) $ pip install ai-traineree-client
