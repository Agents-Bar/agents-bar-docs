Leagues
=======

In short, League orchestrates `Experiments <../console/experiments.html>` which in turn orchestrates interactions between agents and environments.
Its usefulness comes from the observation that agents learn faster when interacting with other agents on a similar level.
For a longer description please see the `League <../concepts/league.html>`_ concept.


Create league
-------------

League arranges matches between agents and environments,
and so, before you can create a League, make sure to have `Agents <../console/agents.html>`_ and `Environments <../console/environments.html>`_ active.
The number of environments limits the number of agents that can train at the same time.
Although having many environments is preferable to run League, using only a single multi agent environment is also beneficial.

To create a league go to the `League entity in console <https://agents.bar/console/console/leagues>`_ and press the *Create league* button.
This will take you to the form with the usual *name* and *description* fields as well as some league specific options.
Agents and environments selection is done through typing their names in autocomplete fields.
Note that only unique entities are allowed; to include the same environment multiple times you need to have many copies of it.

There are two parameters specific to the League:

* `parallel` (integer) value which denotes the number of simultaneous experiments. It has to be equal or greater than the number of available environments.
* `total experiments` (integer) value which refers to the total number of experiments that will be performed.


Start league
------------

Starting a league means to start creating and orchestrating experiments.
This can be done by going to the league of choice and pressing `Start` button in the top right corner.
A dialog will appear for confirmation and a text area where one can pass additional parameters to experiments.
These parameters are used when running each experiment, for example one might pass `max_episodes` or `seed` values.
