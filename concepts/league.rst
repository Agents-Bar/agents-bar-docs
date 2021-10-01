League
======

The League refers to a way of orchestrating experiments with multi agent environments.
It draws the name from sporting events where teams are competing to determine the best.
When starting a new league with new teams/agents there isn't any indication teams/agents performance,
so they are matched randomly.
However, after some matches are completed, we can tell something about relative performance.
Such comparison then can be transformed into ranking and in turn suggest how to assign matches to make them more interesting.
In both cases, sport teams and reinforcement learning agents, interesting means nothing that it easily predictable like a guaranteed winner.

Self-play
---------

It's difficult to prove whether the League approach is the best but there has been many observations that it definitely helps.
For one, when referring to multiple agents we might actually refer to the same agent but with a different state.
Playing against oneself feels beneficial since you are trying to win but you'll definitely lose (and win).
In fact, playing against yourself might be the most difficult game that one can play and still have chance to win.
You know exactly what you want to do and what the opponent will do.
The likely scenario of winning if you learn/discover something new, that you didn't know a few seconds ago.
That's learning.

Strategies
----------

Considering environments that have a clear definition of winning, e.g. chess match or StarCraft.
Although eventually we can tell which player won this won't be obvious during the game.
(If it's obvious and there's a way for an optimal game then we have an algorithm and we're done.)
There are many paths to the same goal, and these paths are often referred to as strategies.
It's possible to emphasize and develope specific strategies but this requires knowing what each path represents.
This means optimizing the league not just on wins (goal) but also on the path.
More specifically, each player and environment needs to monitor their progress and expose additional metrics.
