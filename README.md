# NoGameNoLife_Victor_ESILV-4-A4-STD-CDOF4
The game of life implementation

# Overview
This project implements Conway's Game of Life, a cellular automaton simulation. The game consists of a grid of cells, each of which can be in one of two states: alive or dead. The game progresses in generations, with the state of each cell in a generation being determined by the states of its neighboring cells in the previous generation, following a set of rules.

# Rules of the Game
Any live cell with fewer than two live neighbors dies, as if by underpopulation.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by overpopulation.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

# Guide on How to Contribute
If you are interested in contributing to the Game of Life project, we welcome your contributions! Here is a guide to help you get started:

- Fork the project repository on GitHub.
- Clone your forked repository to your local machine.
- Create a new branch for your contribution: git checkout -b your-branch-name
- Make the necessary changes or additions to the codebase.
- Test your changes locally to ensure they work as expected.
- Commit your changes: git commit -m "Brief description of your changes"
- Push your changes to your forked repository: git push origin your-branch-name
- Create a pull request on the original repository from your forked repository.
- Provide a detailed description of your changes in the pull request.

# Acknowledgments
Hat tip to John Conway for inventing the Game of Life.
Inspiration from other open-source Game of Life implementations.
