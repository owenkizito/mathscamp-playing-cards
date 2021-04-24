# Title

Four Colours

# Metadata

## Type

Fun fact

# Main Version

## Statement

It takes at most four colours to colour every map such that no two adjacent regions (regions that share a border) are the same colour.

## Hint

Can you colour a map of Africa with five colours so that no two countries that touch are filled in with the same colour? Can you also succeed with four colours? How about three colours?

## Explanation

The four color theorem says that given any separation of a plane into contiguous regions, producing a figure called a map, no more than four colours are required to colour the regions of the map so that no two adjacent regions have the same colour. We can see why it is not possible with three colours by looking at the situation around Rwanda: 

![](Four%20Colours_images/image_0.png)

If we try using red, blue and green we can get this far:

![](Four%20Colours_images/image_1.png)

But we can't colour Rwanda using red (because it shares a border with Uganda and Burundi) green (because of Tanzania) or blue (Democratic Republic of Congo). We definitely need another colour. 

The proof that only four colours are needed is very tricky, but the extension will give you an insight into how it is done.

# Extension 1

## Statement

Can you draw a map with 12 countries such that every country has exactly five neighbours, and then colour it in using only 4 colours?

## Hint

Your map should essentially look like this:

![](Four%20Colours_images/image_2.png)

## Explanation

The idea of the proof of the four colour theorem is to find necessary conditions for being a minimal counterexample (this means a minimal non-4-colourable map) and thus to concentrate on maps with these necessary conditions. One of these many necessary conditions is to show that in a minimal counterexample with 12 countries, all countries must have exactly five neighbours. However this can be coloured in like this:

![](Four%20Colours_images/image_3.png)

The proof involves checking around 1500 maps like this!

# Additional information

## About

The proof of the four colour theorem was famously tricky, and comes from graph theory, where mathematicians investigate an equivalent problem of colouring vertices of a network so that no edge has endpoints the same colour. The original four-colour proof was attempted by[ ](https://en.wikipedia.org/wiki/Alfred_Kempe)Alfred Kempe in 1879, but unfortunately Percy John Heawood found an error 11 years later. However his work was not useless, as Percy was able to prove the five-colour theorem (that one can colour a map with no two adjacent regions the sample colour using at most 5 colours) based on Kempe's work. The four colour theorem was finally proved in 1976 by Kenneth Appel, Wolfgang Haken, and John Koch using a computer to check it. This was the first major theorem to be proved using a computer. They checked around 1500 configurations using about 1200 hours of computer time. Some people were sceptical about a proof using a computer but independent verification soon convinced everyone that the four colour theorem had finally been proved.

## References

* https://mathshistory.st-andrews.ac.uk/HistTopics/The_four_colour_theorem/

* https://www.mathsisfun.com/activity/coloring.html

