API Workflow
============

To learn about specific API calls please see either https://agents.bar/redoc, or https://agents.bar/doc.
This page describes the high level workflow of using these APIs.

Additionally, you might prefer to use one of our clients in which case you might find more information on the client's page.

Prerequisite
------------

Before using our APIs you need to have an account.
To create an account please see `Register <../getting-started/register>`_ page.
You'll use these credentials to authenticate your client and obtain necessary token.

Workflow
--------

Agents Bar exposes API through ``https://agent.bar/api``.
Some APIs are publicly accessible and can be queried by anyone, e.g. logging into the service, and some require authentication token.
To obtain the token, the user must first send a query to ``https://agents.bar/api/v1/login/access-token``.
The query will return OAuth2 token that needs to be added as a header to all private APIs.

Clients
-------

.. Note::

    Please reach out if you like to see a client for a specific language. We have in JavaScript and Golang clients.

Our clients will simplify this procedure for you.
To see usage example of our Python client please check Google Collabs at `Doc's quick start <https://docs.agents.bar/getting-started/quick-start.html>`_.

Python client at https://github.com/agents-bar/agents-bar-client-python.

