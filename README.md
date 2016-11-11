# Evolutionary Games Lab
CS 670 Lab 2: Evoultionary Games

## Purpose:
**The purposes of this lab are:**

- To let you experiment game theoretic concepts in an evolutionary setting.
- To teach you the relationship between repeated play and evolutionary stable strategies.
- To learn the differences between Nash Equilibria and evolutionary stable strategies.

## What you should learn:

When you complete this lab, you should understand the following:

- The effect that various kinds of interaction models have on which solutions are selected.
- The effects of various kinds of selection dynamics on which solutions evolve.
- The issues involved in designing a competitive agent (such as inter-agent modeling, anticipation, forgiveness, commitment, etc.).

## Description:
You will conduct a a series of experiments that determine which types of strategies are likely to evolve under various selection dynamics and interaction models for a couple of interesting games.

## Background:
In evolutionary games, the two main factors that contribute to what is learned are: The types of interactions that occur between the agents in a population. The rules that are applied to determine which strategies within the population are fit and therefore likely to be learned by the population. Descriptions of these concepts can be found in the lecture notes. For this lab, we will evaluate replicator dynamics using random pairings and imitator dynamics using neighborhood pairings on a lattice (and the N, NE, E, SE, S, SW, W, NW neighborhood definition).

## Lab Description:
You will conduct a large series of experiments to evaluate what types of strategies evolve in various games. You will perform experiments on the following games:

- Prisoner's Dilemma
- Stag Hunt
- Battle of the Sexes

Use cardinal values for the entries in the payoff matrices 
> (e.g., use T=5, R=3, P=2, and S=1).

You will consider two types of selection and interaction dynamics: (replicator dynamics, random pairings) (imitator dynamics, lattice pairings).
 
 Use 900 agents in all of your simulations (this translates to a 30 by 30 lattice).

Use agents that have a single state. In other words, *use agents that remember the previous action of the other agent and then use this action to determine their next action.*

Thus, the set of all agents are:

| Action of other player on previous round |Agent 1 (Always Cooperate) | Agent 2 (Always Defect) |	Agent 3 (TfT) |	Agent 4 (NotTfT) |
| --- |---| ---| --- | --- |
| **C** |	C |	D |	C |	D |
| **D** |	C |	D |	D |	C |

> Note that this precludes agents like Win Stay Lose Shift, since I can't have actions that depend on both your previous choice and my previous choice.

Assume that Agent 1 and Agent 3 play C on the first round, and that Agent 2 and Agent 4 play D on the first round.

You will consider iterated games for gamma = 0.95 and gamma = 0.99. For the iterated games, compute V(A|B) prior to running the games. This allows you to turn the iterated games into payoff matrices.

> For example, if agent 1 plays agent 2 in the iterated prisoner's dilemma, then the payoff to agent 1 is S / (1-gamma).

Begin with various mixes of agents.

## What to Turn in:
You will be conducting a very large experiment. There are two types of selection/interaction dynamics, three games, two types of game durations (gamma=0.99 and gamma = 0.95), and four types of agents. This means that you will be doing 2x3x2x4 experiments, and you will do these multiple times to account for variabilities in the initial populations. Turn in a summary of your data, and discuss the more interesting results. I suggest comparing and contrasting the effects of selection/interaction dynamics over the various games. I also suggest writing your code so that you can do hundreds of experiments with different initial populations and then show what evolves as a function of the balance between agents in the initial populations.

*Additionally, do something that you think will be cool, like add some mutations, add mixed strategies, or try a different interaction dynamic.*

Write a report on the experiments that you performed, but only report on interesting results. The rubric from the first lab will be used on this lab too.


