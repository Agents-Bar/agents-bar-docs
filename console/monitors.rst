Monitors
========

**tl;dr**: Monitor shows graphs for your agents metrics.

----

Agents' nature is to adapt to the environment and thus if the environment changes the agent changes as well.
These changes can be subtle and persistent so it won't be obvious that the agent is 
learning but having access to metrics makes it easier to notice these changes.

Monitor is a place where all graphs and metrics for agents are available.
The exact metrics are agent-dependent and you can find them in Agent's section.
All agents, however, have access to computed losses and network weights summaries.
Image below shows loss values for an particular agent.


.. image:: /_static/monitor.png
    :width: 600
    :alt: Monitor showing losses
