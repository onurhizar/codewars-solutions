## Binomial Expansion :pencil:

[source](https://www.codewars.com/kata/540d0fdd3b6532e5c3000b5b/python)


> The purpose of this kata is to write a program that can do some algebra. 
> Write a function expand that takes in an expression with a single, one character variable, and expands it. 
> The expression is in the form (ax+b)^n where a and b are integers which may be positive or negative, 
> x is any single character variable, and n is a natural number. 
> If a = 1, no coefficient will be placed in front of the variable. 
> If a = -1, a "-" will be placed in front of the variable.


> The expanded form should be returned as a string in the form ax^b+cx^d+ex^f... 
> where a, c, and e are the coefficients of the term, x is the original one character variable 
> that was passed in the original expression and b, d, and f, are the powers that x is being raised to 
> in each term and are in decreasing order. If the coefficient of a term is zero, the term should not be included. 
> If the coefficient of a term is one, the coefficient should not be included. If the coefficient of a term is -1, 
> only the "-" should be included. If the power of the term is 0, only the coefficient should be included. 
> If the power of the term is 1, the caret and power should be excluded.

example output of `expand("(2f+4)^6")` returns:
`"64f^6+768f^5+3840f^4+10240f^3+15360f^2+12288f+4096"`