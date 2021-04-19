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
    * - Agent Configuration
      - JSON configuration of the agent. It has to contain at least "state_size" and "action_size".

.. Note::

    We understand that providing a JSON into configuration might not be the best user interface and so we will promise an improvement.
    For now, however, please see :ref:`Agent Configuration <console/agents:Agent Configuration>` for details on each agent.

Agent Configuration
```````````````````

Although most agents are created the same way, their configuration will have a slightly different impact.
Below are all available options to pass to each agent, their default values and their descriptions.

DQN
###

All values relate to the ones in the `AI Traineree DQN <https://ai-traineree.readthedocs.io/en/latest/agents.html#dqn>`_.

.. list-table:: Agent configuration
    :widths: 20 20 30
    :header-rows: 1

    * - Key
      - Default
      - Description
    * - state_size
      - N/A
      - Number of values to expect from observations.
    * - action_size
      - N/A
      - For discrete problem, that's a number of potential values. For continuous, that' number of values.
    * - hidden_layers
      - (64, 64)
      - Tuple defining hidden dimensions in fully connected nets.
    * - lr
      - 3e-4
      - Learning rate
    * - gamma
      - 0.99
      - discount factor
    * - tau
      - 0.002
      - soft-copy factor
    * - update_freq
      - 1
      - Number of steps between each learning.
    * - batch_size
      - 64
      - Number of samples to use in learning.
    * - buffer_size
      - 1e5
      - Size of the experience buffer.
    * - warm_up
      - 0
      - How many samples to wait before performing learning.
    * - number_updates
      - 1
      - Per learning, how many times to compute error and update agent.
    * - max_grad_norm
      - 10
      - Maximum at which the gradient is capped.
    * - using_double_q
      - true
      - Whether to use double Q value
    * - n_steps 
      - 1
      - N steps reward lookahead

PPO
###

All values relate to the ones in the `AI Traineree PPO <https://ai-traineree.readthedocs.io/en/latest/agents.html#ppo>`_.

.. list-table:: Agent configuration
    :widths: 20 20 30
    :header-rows: 1

    * - Key
      - Default
      - Description
    * - state_size
      - N/A
      - Number of values to expect from observations.
    * - action_size
      - N/A
      - For discrete problem, that's a number of potential values. For continuous, that' number of values.
    * - hidden_layers
      - (100, 100)
      - Tuple defining hidden dimensions in fully connected nets.
    * - is_discrete
      - False
      - Whether return discrete action.
    * - kl_div
      - False
      - Whether to use KL divergence in loss.
    * - using_gae
      - True
      - Whether to use General Advantage Estimator.
    * - gae_lambda
      - 0.96
      - Value of lambda in GAE.
    * - actor_lr
      - 0.0003
      - Learning rate for the actor (policy).
    * - critic_lr
      - 0.001
      - Learning rate for the critic (value function).
    * - actor_betas
      - (0.9, 0.999
      - Adam’s betas for actor optimizer.
    * - critic_betas
      - (0.9, 0.999
      - Adam’s betas for critic optimizer.
    * - gamma
      - 0.99
      - Discount value.
    * - ppo_ratio_clip
      - 0.25
      - Policy ratio clipping value.
    * - num_epochs
      - 1
      - Number of time to learn from samples.
    * - rollout_length
      - 48
      - Number of actions to take before update.
    * - batch_size
      - rollout_length
      - Number of samples used in learning.
    * - actor_number_updates
      - 10
      - Number of times policy losses are propagated.
    * - critic_number_updates
      - 10
      - Number of times value losses are propagated.
    * - entropy_weight
      - 0.005
      - Weight of the entropy term in the loss.
    * - value_loss_weight
      - 0.005
      - Weight of the entropy term in the loss.

DDPG
####

All values relate to the ones in the `AI Traineree DDPG <https://ai-traineree.readthedocs.io/en/latest/agents.html#ddpg>`_.

.. list-table:: Agent configuration
    :widths: 20 20 30
    :header-rows: 1

    * - Key
      - Default
      - Description
    * - state_size
      - N/A
      - Number of values to expect from observations.
    * - action_size
      - N/A
      - For discrete problem, that's a number of potential values. For continuous, that' number of values.
    * - hidden_layers
      - (128, 128)
      - Tuple defining hidden dimensions in fully connected nets.
    * - actor_lr
      - 3e-4
      - Actor specific learning rate
    * - critic_lr
      - 3e-4
      - Critic specific learning rate
    * - gamma
      - 0.99
      - discount factor
    * - tau
      - 0.002
      - soft-copy factor
    * - update_freq
      - 1
      - Number of steps between each learning.
    * - batch_size
      - 64
      - Number of samples to use in learning.
    * - buffer_size
      - 1e5
      - Size of the experience buffer.
    * - warm_up
      - 0
      - How many samples to wait before performing learning.
    * - number_updates
      - 1
      - Per learning, how many times to compute error and update agent.
    * - max_grad_norm_actor
      - 10
      - Maximum at which critic's gradient is capped.
    * - max_grad_norm_critic
      - 10
      - Maximum at which actor's gradient is capped.
    * - action_min
      - -1
      - Minimum returned action value
    * - action_max
      - 1
      - Maximum returned action value
    * - action_scale
      - 1
      - How much to scale action value (std var in action distribution)
