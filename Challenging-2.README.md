Challenging #2 - Programming

To run the second challenging test command
> python3 find-pair.py prices.txt 2200
`This test returns two and three gifts`

> python3 find-pair.py prices.txt 1200
`This test returns two gifts and not possible for three gifts`

> python3 find-pair.py prices.txt 1000
`This test returns not possible for two gifts`

What is the big O notation for your program? 
complexity = O(C(n,2))
> Ans: O(n^2) for find pair gifts
           
complexity = O(C(n,3))
> Ans: O(n^3) for find triple gifts

Bonus Question A:
> Ans: Implemented in the function - finding_closest_three

Bonus Question B:
> Ans: We can load only the price as number and filter out any price larger 
than balance. Using the loaded numbers to find the pair numbers. Then 
searching the file with the given number to find the name of the item. 
It will be able to load a very big file
