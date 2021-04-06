Agents
======

Agents are entities that can interact with an environment_ and become better at something.
This is somehow vague because agents can do many things depending on the task. 
To avoid being too philosophical or technical, let's just say that agents are optimizing
doing a task but that task is sensitive to any changes.
That is still quite broad but manybe `examples <Examples>`_ would give some colouring.

In very technical terms when refering to agents we mean an implementation of the deep reinforcement learning agent.

Examples
--------

AI bots in computer games.
    Each bot can interact with the game and with other players.
    Depending on the type of game, these bots can hide from you, chase you, shoot you, or try to talk to you.
    Although they might not want to "win" the game, since they were programmed that way, they have a specific
    task which usually revolves around other players. Their state is current game situation and their actions
    change the game a bit.

Optimizing financial portfolio performance.
    In this case agents are investors. Their states are timestamp portfolio values and their task is maximize
    returns. Their actions are noted be either selling some of their assets or buying different.
    Even though their action have limited impact on the whole market, unless they have a lot of assets,
    their environment changes because their future buying/sellings depend on their liquidity.

Retail business inventory.
    You can sell what you have and what you have is what you've ordered. Agents states are your inventory
    states and your actions are what to do with your inventory. The environment changes because you
    cannot sell what you don't have and prices changes every day. Everything has their own shelf life;
    some items are perishable and some will go out of fashion. The goal is to get profits, or at least
    not to go out of business.



Source code
-----------

Currently, all our agents are from the open source project `AI Traineree Docs`_.
You can see their source code at the github page with the same name, i.e. `ai-traineree`_. 

Why AI Traineree? Is has the most suitable API for the job. We will, however, start adding different agents.
Either by onboarding different open source packages or implementing recent popular advances in Deep Reinforcement Learning research.


.. _AI Traineree Docs: https://ai-traineree.readthedocs.io
.. _ai-traineree: https://github.com/laszukdawid/ai-traineree
