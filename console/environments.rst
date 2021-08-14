Environments
============

Environment is where the agent lives and what they learn.
A common example of an environment is a game with agents being their AI.
Game provides states and rewards for AI interacting with it in particular way.


Create environment
------------------

Manual creation
```````````````

Currently predefined environments are those provided by the OpenAI gym.
More options for creating environment, including updating your own, will come shortly.

To create an environment you need to go to the `Environment Create <https://agents.bar/console/console/environments/new>`_ page.
The form asks for the name and description.
These are mainly for you to refer to your environment and remember its purpose.
Then, there is **Gym name** and **Environment image** either of which needs to be filled for the form to be valid.
In case you want to use popular OpenAI gym's environment then use gym's name, e.g. ``CartPole-v1`` in the **Gym name**.
The **Environment image** allows to use all other environments, referred to as :ref:`Custom environments <console/environments:Custom environment>`.
If you have access to custom environment then here you use its name.
For example, one would use ``laszukdawid/small-env`` to access environment stored at `laszukdawid/small-env docker hub <https://hub.docker.com/repository/docker/laszukdawid/small-env>`_.


Custom environment
------------------

Agents Bar allows adding and using custom environments.
This means that you can add and solve your own environment rather than using officially provided.
We expect custom environments to be as a Docker (or alternative) image and stored in an public (read) repository.

To make sure we can communicate with the container, you need to expose some APIs through http (port 80).
Specifications on required APIs is provided in out open github repository `RL API Definitions <https://github.com/Agents-Bar/rl-api-definitions>`_.

