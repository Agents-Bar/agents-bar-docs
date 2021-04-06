Agents
======

The main interaction with agents it through the `ai-traineree-client` python module.

Currently supported agent models:

.. autodata:: ai_traineree_client.SUPPORTED_MODELS

The main component that allows communication with the Agents Bar is the :py:class:`ai_traineree_client.RemoteClass`.
Its whole API is provided below. Note, however, that it is intentionally similar to all agents 
in the AI Traineree (`ai-traineree <htts://ai-traineree.readthedocs.com>`_) package.

.. autoclass:: ai_traineree_client.RemoteAgent
    :members:

