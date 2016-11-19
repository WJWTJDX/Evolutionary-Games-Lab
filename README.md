# Evolutionary Games Lab
CS 670 Lab 2: Evoultionary Games

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

### Specifications
A complete version of the lab specifications can be found in the wiki:
- [Full Specifications](https://github.com/lwthatcher/Evolutionary-Games-Lab/wiki/Lab-Specs)
- [Written Report Grading Rubric](https://github.com/lwthatcher/Evolutionary-Games-Lab/wiki/Rubric)
