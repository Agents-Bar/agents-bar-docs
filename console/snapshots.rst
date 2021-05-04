Snapshots
=========

Snapshots allow for agent's full reconstruction.
They contain everything about the agent and what is needed to reproduce the agent at a particular point in time.
If you think of a save button on an agent, a snapshot is what you'd save.

Creating a snapshot
-------------------

Each agent, by default, has enabled automatic snapshot creation.
A new snapshot is created every 10 minutes. Changing the frequency is available through the *Agent*'s configuration panel. 

.. Note::
    We are working on adding conditional snapshot creations and allowing more than one snapshot per agent.
    If that's something you're interested in please reach out. We prioritize work based on demand.


Download snapshot
-----------------

To download the most recent snapshot go to the agent's view and click on the **Download** button.
Use the prompt to select destination for the json file.

Upload snapshot
---------------

Currently, upload snapshot is only possible if an agent already exists.
In such a case, spanshot upload means reverting an agent back to a previously seen state.
To upload the snapshot, go to Agent's Edit panel and click the **Upload** button.
When prompted select the snapshot for the same agent.
