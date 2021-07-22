# worldCafe
A simple python script to allocate table orders for guests at a world cafe event.

During my tenure as the Potentia Scholar, we hosted a World Cafe Event. 

A world cafe event is a mixer with multiple tables, each with a question or topic of conversation.
Guests to the event must be assigned an order with which to visit the tables. 
Each guest visits one table in each 'round', should not visit the same table twice, and may or may not visit all the tables at the event.
In addition, the tables should be allocated in such a way to divide the guests evenly between tables for each round to avoid oversized or undersized groups.

I wrote this script to assist with table allocation. It utilises a brute-force approach, selecting random samples from the possible pool of permutations, then checking if the conditions are met for each round. 

There is probably a way to do this much more efficiently, but this served our purposes.
