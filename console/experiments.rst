Experiments
===========

Experiment orchistrates interaction between agents and the environment.
This allows you to train your agents much faster than if you were to communicate between them via APIs.

Create experiment
-----------------

To create experment you need to have first an `Agent <../Agent>`_ and an `Environment <../Environment>`_.
Make sure they exist and are active.
Experiment supports all compatible agents and environments, however,
you need to make sure that connected agent and environment are compatible.
This mainly means that the observation and action sizes match and that action is expected in discrete/continious format.

You can create an experiment through the console in the `Experiment <https://agents.bar/console/console/environments>`_ page.
The form should guide you, including allowing to select only available agents and environments.

Experiment, and all other entities, are expected to have unique name per user. This means that you can only have one "MyTestAgent" agent.
In case you want to perform multiple experiments between the same pair of agent and environment, we suggest adding some numerical suffix.
Good names include "StarCraft2-CustomDQN-001" and "Pong_Test1".
