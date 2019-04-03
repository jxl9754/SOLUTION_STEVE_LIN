Challenging #2 - Programming

How To Run
=
`python3 find-pair.py prices.txt 2200`
<BR><i>This test returns two and three gifts<BR></i>

`python3 find-pair.py prices.txt 1200`
<BR><i>This test returns two gifts and not possible for three gifts<BR></i>

`python3 find-pair.py prices.txt 1000`
<BR><i>This test returns not possible for two gifts<BR></i>

Questions
=
What is the big O notation for your program? 
<BR> I used itertools package's combinations function which has C(n,k) 
n is the number of available gifts and k is the number of selected gifts. 
<BR>`finding pair gifts complexity = O(C(n,2)) = n(n-1)/2 ≈ n^2`
> Ans: O(n^2) for finding pair gifts
           
`finding triple gifts complexity = O(C(n,3)) = n(n-1)(n-2)/(2*3) ≈ n^3`
> Ans: O(n^3) for finding triple gifts

Bonus
=
Bonus Question A:
> Ans: Implemented in the function - finding_closest_three

Bonus Question B:
> Ans: We can load only the prices as list of numbers and filter out any price larger 
than balance. Using the loaded list of numbers to find the closest pair numbers below 
balance. Then searching the input file with the given closest pair numbers to find the 
names of the items. It will be able to load a much bigger file
