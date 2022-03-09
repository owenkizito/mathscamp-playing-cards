# Title

Colouring

# Metadata

## Type

counting

# Main Version

## Statement

How many possible three-stripe flags similar to the one below are there if only 5 colours are available and two touching stripes must NOT have the same colour?

![](Colouring_images/image_0.png)

## Correct Answer

80

## Hint

Think about how many different colours could go in the first section, then the second ...

## Explanation

There is a choice of 5 colours for the first section. Once a colour has been chosen, the second section cannot be the same. So there are only four colours to choose from for the second section. For the third section, there are four colours to choose from, as it cannot be the same colour as the second one yet it can be the same colour as the first one. Thus, the number of tricolour flags with 5 colours to choose from are 5×4×4 = 80.

# Extension 1

## Statement

In how many different ways can I paint the five walls of a pentagonal room using red, blue and green paint so that no two neighbouring walls are the same colour?

![](Colouring_images/image_1.png)

## Hint

Fix one colour, say start with the top wall red, and try to list all the different options for the other walls.  

## Correct Answer

30

## Explanation

First of all you start with either red, blue or green and use one of the other colours for the second side and so on around the pentagon. When you get to the last side it cannot be the same as the fourth side or the first one.

We can represent the choices of colours in a tree diagram, At the top (known as the root of the tree) we paint the first side. Here we choose red). The first split is the choice of either green or blue for the second side. The next split is the choice for the third side which depends on your choice of the second side. Any path from the root to end of the tree (known as a leaf) gives you a choice for all of the five edges. We see if we started with red, we have 10 different colourings. 

As we can make similar diagrams if we had chosen green or blue in the first position, we have a total of 3×10 = 30 different colourings. 

![](Colouring_images/image_2.png)

# Additional information

## About

In a room with an even number of walls, two colors are always enough. For rooms with an odd number of walls, you will need three colors.

## References

* https://nrich.maths.org/600

