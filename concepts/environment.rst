Environment
===========

The environment is where the agent lives and interacts with.
The common example of the environment is a computer game where the agent, e.g. AI bot, can move
and interact with the environment as well as other agents.
It's the environment's responsibility to describe agent's whereabouts and its situation, i.e. the state.
The agent will be able to take some actions, in case of computer game that'd be moving, or shooting,
or using equipment, although essentially it's down to the environment whether proposed actions are valid.
That's because the environment understands and imposes all rules whereas the agent only knows what they've
seen so far. An example of invalid agent action would be when it's its first time trying to walk through the wall.
The environment knows that nothing can go through a wall, even a very determined agent.
So agent will try move forward, i.e. through wall, but the environment would know that that's invalid
action and it didn't change state.


Examples
--------

Computer game
    The environment would be a computer game with the game engine and physics built in.
    Agents, i.e. bots or human players, can interact with it by sending commands like
    "move forward", "shoot" or "open inventory" but it's up to the environment to decide
    what are the results of trying these actions. Common representation of the state in games
    is an image that the user will see on the screen. It's important to remember that some
    actions take more than one game frame and that "no action" is also an action.

Financial marketplace
    Although it might be potraied as abstract, since the majority of interaction are directly
    between agents, each marketplace has their own rules/laws that needs to be obeyed.
    The marketplace might also act as intermedary for interactions between agents.
    Instead of each agent trying to find others to exchange assets, they might directly ask
    the environment whether given action is valid and if so to perform it.
