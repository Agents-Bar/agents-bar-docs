Agents
======

The main interaction with agents it through the `agents-bar-client-python <https://pypi.org/project/agents-bar/>`_ python module.

Currently supported agent models:

.. autodata:: agents_bar.SUPPORTED_MODELS

The main component that allows communication with the Agents Bar is the :py:class:`agents_bar.RemoteClass`.
Its whole API is provided below. Note, however, that it is intentionally similar to all agents 
in the AI Traineree (`ai-traineree <htts://ai-traineree.readthedocs.com>`_) package.

.. autoclass:: agents_bar.RemoteAgent
    :members:

