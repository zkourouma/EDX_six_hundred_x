The office supply store sells your favorite types of pens in packages of 5, 8 or 24 pens. Thus, it is possible, for example, to buy exactly 13 pens (with one package of 5 and a second package of 8), but it is not possible to buy exactly 11 pens, since no non-negative integer combination of 5's, 8's and 24's add up to 11. To determine if it is possible to buy exactly n pens, one has to find non-negative integer values of a, b, and c such that

5a+8b+24c=n

Write a function, called numPens that takes one argument, n, and returns True if it is possible to buy a combination of 5, 8 and 24 pack units such that the total number of pens equals exactly n, and otherwise returns False.