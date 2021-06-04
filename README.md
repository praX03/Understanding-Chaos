# Understanding Chaos

*This are all the projects from my study of Chaos Theory and Complex Systems*
</br>
## Nought.1 Plotting bifurcation diagram of a dynamical chaotic system

I have tried to simulate the logistic map in Python3 using MatPlotLib and NumPy.
The logistic map is a polynomial mapping (equivalently, recurrence relation) of degree 2, often cited as an archetypal example of how complex, chaotic behaviour can arise from very simple non-linear dynamical equations.

This notebook is created to play around with other non-linear discrete equations and to analyse their impacts and concurrences towards the logistic map.

I would arrange more equations in the notebook gradually, meanwhile I am finding a method to create dynamic graphs in Python

Comments and explanation needs to be added in the notebook as of 3/06/21

## Nought.2 Understanding Conway's Game of Life

The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. It is Turing complete and can simulate a universal constructor or any other Turing machine.

### Rules

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead, (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

* Any live cell with fewer than two live neighbours dies, as if by underpopulation.
* Any live cell with two or three live neighbours lives on to the next generation.
* Any live cell with more than three live neighbours dies, as if by overpopulation.
* Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
 
These rules, which compare the behavior of the automaton to real life, can be condensed into the following:

* Any live cell with two or three live neighbours survives.
* Any dead cell with three live neighbours becomes a live cell.
* All other live cells die in the next generation. Similarly, all other dead cells stay dead.
The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed, live or dead; births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick. Each generation is a pure function of the preceding one. The rules continue to be applied repeatedly to create further generations.

### How to play

You must have pygame and grid installed in your system.
This program is created in Python3.9 but would work with any Python3.x versions.
Just clone the repository on your device -> Open the "Game of Life" directory -> Run "python3 main.py"

* Adjust the width, height = xxxx, xxxx in the main.py according to your screen size.
