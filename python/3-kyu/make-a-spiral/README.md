## Make a spiral :snake:

[source](https://www.codewars.com/kata/534e01fbbb17187c7e0000c6/python)


> Your task, is to create a NxN spiral with a given size.
> For example, spiral with size 5 should look like this:
> 00000
> ....0
> 000.0
> 0...0
> 00000
> Return value should contain array of arrays, of 0 and 1, for example for given size 5 result should be:


`[[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]`

In the code, `eC` and `fC` stand for emptyCell and filledCell characters. 
Example output, where `eC,fC = " ","*"`
`printSpiral(spiralize(11))`:

```
* * * * * * * * * * * 
                    * 
* * * * * * * * *   * 
*               *   * 
*   * * * * *   *   * 
*   *       *   *   * 
*   *   * * *   *   * 
*   *           *   * 
*   * * * * * * *   * 
*                   * 
* * * * * * * * * * * 
```
