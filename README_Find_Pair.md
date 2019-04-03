Challenge #2 - Programming

To run the second question
1. python3 find-pair.py prices.txt 1200


What is the big O notation for your program? 
complexity = O(C(n,2))
           O(n^2) for find pair
           
complexity = O(C(n,3))
           O(n^3) for find triple

Bonus Question A:
Implemented in the function - finding_closet_three

Bonus Question B:
Ans: We can load only the price as number and filter out any price larger 
than balance. Using the loaded numbers to find the pair numbers. Then 
searching the file with the given number to find the name of the item. 
It will be able to load a very big file
