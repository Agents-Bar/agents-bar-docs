Agents
======

Here you will find all your running agents and be able to create a new one.
When entering you will see a list of agents that you have previously created with some quick overview.

A bit more specifically, you'll see information like:

* **Name** of the agent
* **Type** of the agent, e.g. DQN, PPO or C51
* **Is Active** which indicates whether agent can be accessed
* **Description** of the agent which you gave
* **Configuration** of the agent

Your agents are shown in a table which has a limit of view. By default that's five agents per page.
To navigate between pages use arrows in the bottom right corner, or use the **search** option just above the table.


Create agent
------------

Manual creation
```````````````

When you click "Create Agent" it will take you to the agent creation page.
To create an agent the following are expected:

.. list-table:: Agent Create options
    :widths: 25 75
    :header-rows: 1

    * - Option
      - Description
    * - Name
      - Name of your agent. It has to be unique per user.
    * - Model
      - Type of the agent, for example DQN or DDPG.
    * - Description
      - Text indicating something specific about this agent.
    * - Is Active
      - Checkbox whether to create an active agent.
    * - Observation space
      - Definition of the observation space.
    * - Action space
      - Definition of the action space.
    * - Agent Configuration
      - JSON configuration of the agent.

.. Note::

    We understand that providing a JSON into configuration might not be the best user interface and so we will promise an improvement.
    For now, however, please see :ref:`Agent Configuration <console/agents:Agent Configuration>` for details on each agent.
    Feel free to reach out and let us know about your preferences. We are prioritizing work based on demand.

When selecting ``CUSTOM`` as the agent Model an ``image name`` field will appear.
This field is required for custom agents and it should contain docker (or alternative) image name for 
publicly accessible image.
For example, to use an agent with random actions, i.e. dummy agent, one would use ``laszukdawid/dummy-agent`` from `docker hub repository <https://hub.docker.com/repository/docker/laszukdawid/dummy-agent>`_.

From a Snapshot
```````````````

Another option to create an agent is through uploading a Snapshot.
This is a preferred method when you have already a Snapshot of a trained agent.
Snapshots can be obtained be either sharing them with other users, or downloading a snapshot from one of your agents.

To create an agent from a Snapshot go to `Agents <https://agents.bar/console/console/agents>`_ and click on the **From Snapshot** button.
This will take you to a form where you'll be able to type new agent's name and select where your snapshot file is located.
Once both options are properly filled the **Save** button should be available.
After submitting the form you should see the agent on the Agents view page.

Custom agent
------------

Agents Bar allows adding and using custom agents.
By *custom agents* we refer to all agents that aren't officially supported.
These agents need to in form of a Docker (or alternative) image and stored in an public (read) repository.

Communication with these containers is through http so the custom agent needs to expose port 80.
Specifications on required APIs is provided in out open github repository `RL API Definitions <https://github.com/Agents-Bar/rl-api-definitions>`_.

Agent Configuration
-------------------

Although most agents are created the same way, their configuration will have a slightly different impact.
Below are all available options to pass to each agent, their default values and their descriptions.

DQN
```

All values relate to the ones in the `AI Traineree DQN <https://ai-traineree.readthedocs.io/en/latest/agents.html#dqn>`_.

.. list-table:: DQN agent configuration
    :widths: 20 20 10 30
    :header-rows: 1

    * - Key
      - Default
      - Type
      - Description
    * - hidden_layers
      - (64, 64)
      - tuple of ints
      - Tuple defining hidden dimensions in fully connected nets.
    * - lr
      - 3e-(4
      - float
      - Learning rate
    * - gamma
      - 0.99
      - float
      - discount factor
    * - tau
      - 0.002
      - float
      - soft-copy factor
    * - update_freq
      - 1
      - int
      - Number of steps between each learning.
    * - batch_size
      - 64
      - int
      - Number of samples to use in learning.
    * - buffer_size
      - 1e5
      - int
      - Size of the experience buffer.
    * - warm_up
      - 0
      - int
      - How many samples to wait before performing learning.
    * - number_updates
      - 1
      - int
      - Per learning, how many times to compute error and update agent.
    * - max_grad_norm
      - 10
      - float
      - Maximum at which the gradient is capped.
    * - using_double_q
      - true
      - bool
      - Whether to use double Q value
    * - n_steps
      - 1
      - int
      - N steps reward lookahead

PPO
```

All values relate to the ones in the `AI Traineree PPO <https://ai-traineree.readthedocs.io/en/latest/agents.html#ppo>`_.

.. list-table:: PPO agent configuration
    :widths: 20 20 10 30
    :header-rows: 1

    * - Key
      - Default
      - Type
      - Description
    * - hidden_layers
      - (100, 100)
      - tuple of ints
      - Tuple defining hidden dimensions in fully connected nets.
    * - is_discrete
      - False
      - bool
      - Whether return discrete action.
    * - kl_div
      - False
      - bool
      - Whether to use KL divergence in loss.
    * - using_gae
      - True
      - bool
      - Whether to use General Advantage Estimator.
    * - gae_lambda
      - 0.96
      - float
      - Value of lambda in GAE.
    * - actor_lr
      - 0.0003
      - float
      - Learning rate for the actor (policy).
    * - critic_lr
      - 0.001
      - float
      - Learning rate for the critic (value function).
    * - actor_betas
      - (0.9, 0.999)
      - tuple of floats
      - Adam’s betas for actor optimizer.
    * - critic_betas
      - (0.9, 0.999)
      - tulple of floats
      - Adam’s betas for critic optimizer.
    * - gamma
      - 0.99
      - float
      - Discount value.
    * - ppo_ratio_clip
      - 0.25
      - float
      - Policy ratio clipping value.
    * - num_epochs
      - 1
      - int
      - Number of time to learn from samples.
    * - rollout_length
      - 48
      - int
      - Number of actions to take before update.
    * - batch_size
      - rollout_length
      - int
      - Number of samples used in learning.
    * - actor_number_updates
      - 10
      - int
      - Number of times policy losses are propagated.
    * - critic_number_updates
      - 10
      - int
      - Number of times value losses are propagated.
    * - entropy_weight
      - 0.005
      - float
      - Weight of the entropy term in the loss.
    * - value_loss_weight
      - 0.005
      - float
      - Weight of the entropy term in the loss.

DDPG
````

All values relate to the ones in the `AI Traineree DDPG <https://ai-traineree.readthedocs.io/en/latest/agents.html#ddpg>`_.

.. list-table:: DDPG agent configuration
    :widths: 20 20 10 30
    :header-rows: 1

    * - Key
      - Default
      - Type
      - Description
    * - hidden_layers 
      - (128, 128)
      - tuple of ints
      - Tuple defining hidden dimensions in fully connected nets.
    * - actor_lr
      - 3e-4
      - float
      - Actor specific learning rate
    * - critic_lr
      - 3e-4
      - float
      - Critic specific learning rate
    * - gamma
      - 0.99
      - float
      - discount factor
    * - tau 
      - 0.002
      - float
      - soft-copy factor
    * - update_freq 
      - 1
      - int
      - Number of steps between each learning.
    * - batch_size
      - 64
      - int
      - Number of samples to use in learning.
    * - buffer_size
      - 1e5
      - int
      - Size of the experience buffer.
    * - warm_up
      - 0
      - int
      - How many samples to wait before performing learning.
    * - number_updates
      - 1
      - int
      - Per learning, how many times to compute error and update agent.
    * - max_grad_norm_actor
      - 10
      - float
      - Maximum at which critic's gradient is capped.
    * - max_grad_norm_critic
      - 10
      - float
      - Maximum at which actor's gradient is capped.
    * - action_min
      - -1
      - float
      - Minimum returned action value
    * - action_max
      - 1
      - float
      - Maximum returned action value
    * - action_scale
      - 1
      - float
      - How much to scale action value (std var in action distribution)

Rainbow
```````

All values relate to the ones in the `AI Traineree Rainbow <https://ai-traineree.readthedocs.io/en/latest/agents.html#rainbow>`_.

.. list-table:: Rainbow agent configuration
    :widths: 20 20 10 30
    :header-rows: 1

    * - Key
      - Default
      - Type
      - Description
    * - hidden_layers
      - (100, 100)
      - tuple of ints
      - Shape and sizes of fully connected networks used. 
    * - lr
      - 1e-3
      - float
      - Learning rate value.
    * - gamma
      - 0.99
      - float
      - Discount factor. 
    * - tau
      - 0.002
      - float
      - Soft-copy factor. 
    * - update_freq
      - 1
      - int
      - Number of steps between each learning step. 
    * - batch_size
      - 80
      - int
      - Number of samples to use at each learning step. 
    * - buffer_size
      - 1e5
      - int
      - Number of most recent samples to keep in memory for learning. 
    * - warm_up
      - 0
      - int
      - Number of samples to observe before starting any learning step. 
    * - number_updates
      - 1
      - int
      - How many times to use learning step in the learning phase. 
    * - max_grad_norm
      - 10
      - float
      - Maximum norm of the gradient used in learning. 
    * - using_double_q
      - True
      - bool
      - Whether to use Double Q Learning network. 
    * - n_steps
      - 3
      - int
      - Number of lookahead steps when estimating reward.
    * - v_min
      - -10
      - float
      - Lower bound for distributional value V. 
    * - v_max
      - 10
      - float
      - Upper bound for distributional value V. 
    * - num_atoms
      - 21
      - int
      - Number of atoms (discrete states) in the value V distribution. 

