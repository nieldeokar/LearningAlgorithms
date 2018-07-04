# Learning Algorithms

I recently started learning more about Algorithms from [Grokking Algorithms by Aditya Bhargava][1]. Since I was starting from scratch so though of making this repo to add the basic algorithm code samples here. I hope along with the code sample I would be able to add my own notes to this repo. :D


## Chapter 1 - Introduction to algorithms :
An algorithm is a set of instructions for accomplishing a task. Suppose we want to accomplish task of going to school in the morning so algorithm for same would be something like :
1. Wake up & Get out of bed
2. Get fresh & Wear clothes
3. Have breakfast and take school bus
4. Reach school

In programming term every piece of code could be called as an algorithm.

### Search :

There are two types of search one is simple and another is binary. Suppose we want to find a guy named Eric in class of 200 students. Simple search would be like asking everyone in the class whether he is Eric or not. where as Binary search would be
more like sorting and then searching. Sorting as in since we know that Eric is a male we will only consider males students and then the students starting with name `E`.

### Simple Search & Binary Search :
Suppose I’m thinking of a number between 1 and 100. You have to try to guess my number in the fewest tries possible. With every guess, I’ll tell you if your guess is too low, too high, or correct. Suppose you start guessing like this: 1, 2, 3, 4 .... with every search you are trying to eliminate only one number. If my number was 99, it could take you 99 guesses to get there!

**A better way to search**  
Here’s a better technique. Start with 50 and my response is *too low*, but you just eliminated half the numbers! Now you know that 1–50 are all too low. Next guess: 75. *Too high*, but again you cut down half the remaining numbers! With binary search, you guess the middle number and eliminate half the remaining numbers every time. Next is 63 (halfway between 50 and 75). This is binary search.  

Whatever number I’m thinking of, you can guess in a maximum of *seven* guesses—because you eliminate so many numbers with every guess!

Binary search In general, for any list of n, will take `log<sub>2</sub> n` steps to run in the worst case, whereas simple search will take `n` steps.

### Logarithms
You may not remember what logarithms are, but you probably know what exponentials are. `log<sub>10</sub> 100` is like asking, “How many 10s do we multiply together to get 100?”  The answer is 2: 10 × 10. So `log<sub>10</sub> 100` = 2. Logs are the flip of exponentials.

### Complexity of Simple & Binary search :
When you search for an element using simple search, in the worst case you might have to look at every single element. So for a list of 8 numbers, you’d have to check 8 numbers at most.

For binary search, you have to check `log<sub>2</sub> n` elements in the worst case. For a list of 8 elements, `log<sub>2</sub> 8` == 3, because `2<sup>3</sup>` == 8. So for a list of 8 numbers, you would have to check 3 numbers at most. For a list of 1,024 elements, `log<sub>2</sub> 1,024` = 10, because 210 == 1,024. So for a list of 1,024 numbers, you’d have to check 10 numbers at most.

### Recap  
• Binary search is a lot faster than simple search.  
• O(log n) is faster than O(n), but it gets a lot faster once the list of items you’re searching through grows.  
• Algorithm speed isn’t measured in seconds.  
• Algorithm times are measured in terms of growth of an algorithm.  
• Algorithm times are written in Big O notation.  

## Chapter 2 - Arrays and Lists :
Computer memory is like block of drawers. When you visit swimming pool you ask for drawer, guy over there gives you drawer number and key to the drawer then you go to the drawer room find your drawer open it and keep inside whatever you want. Same way when program is executing you need to store some variables somewhere, the place where it gets stored in memory. Now there are different ways in which we can store data into computer memory like array or list.

### Arrays :
Arrays are like continues block of drawers together aligned side by side or one below another with fixed size. If we are using array we need to specify size in advance. If we need to increase the size of an array computer might have to copy array to new location to get the required size in continuation which is a costly operation.

### Linked Lists :
Linked Lists are dynamic in size. They can grow in size as and when required. Linked lists are like treasure hunt game where you go to first address and it says "Your next address is 123", Then you go to the 123 and then it says "Your next address is 456". Each memory block of linked list stores the address to the next block because of which they are dynamic in size.

### Selection sort :
Suppose we have a list of songs and for each artist we have play count and we want to sort list according to the play count what can we do ? Let's talk in terms of algorithm.
1. Create a empty list where we will put our items in descending order.  
2. Find the max played item from the original list.  
3. Put that item into new list.  
4. Now repeat from step 2 till our original list is empty.

To  find the artist with the highest play count, we have to check each item in the list, this takes O(n) time (Step 2). So we have an operation that takes O(n) time, and we have to do that n times. Which makes it `O(n × n)` time.  

This is what the **Selection sort** is.

### Recap
• Your computer’s memory is like a giant set of drawers.  
• When you want to store multiple elements, use an array or a list.  
• With an array, all your elements are stored right next to each other.  
• With a list, elements are strewn all over, and one element stores the address of the next one.  
• Arrays allow fast reads.  
• Linked lists allow fast inserts and deletes.  
• All elements in the array should be the same type (all ints, all doubles, and so on).  


## Chapter 3 - Recursion :
Recursion is function calling to itself. Suppose we want to print countdown like 3..2..1..0
Simple python script would look like :
```python
def countdown(i):
    print i
    countdown(i-1)
```
It will print something like : 3...2...1...0...-1...-2... which is unexpected since we only want to print till 0. So we need to break the program somewhere and that breaking case is called as Base case.

```python
def countdown(i):
	print i
	if i < 0 : # Base case
		return
	else: # Recursive case
		countdown(i-1)
print(countdown(5))
```

This snipped will stop printing once we reach `i < 0`.

### Conclusion :  
Recursion is used when it makes the solution clearer.  ere’s no performance bene t to using recursion; in fact, loops are sometimes better for performance. I like this quote by [Leigh Caldwell on Stack Overflow][2]
>Loops may achieve a performance gain for your program. Recursion may achieve a >performance gain for your programmer. Choose >which is more important in your >situation!

### Recap  
• Recursion is when a function calls itself.  
• Every recursive function has two cases: the base case and the recursive case.  
• A stack has two operations: push and pop.  
• All function calls go onto the call stack.  
• The call stack can get very large, which takes up a lot of memory.  

## Chapter 4 - QuickSort :

#### Divide & conquer
It's a strategy of breaking down a problem to it's lowest state and then working on it again. Here is how D&C works:  
1. Figure out a simple case as the base case.
2. Figure out how to reduce your problem and get to the base case.
D&C isn’t a simple algorithm that you can apply to a problem. Instead, it’s a way to think about a problem. Let’s do one more example.

#### Euclid's algorithms   
“If you find the biggest box that will work for this size, that will be the biggest box that will work for the entire farm.” Khan academy has a good explanation here on [Euclid's algorithm][3]:

#### Inductive proofs
Inductive proofs are one way to prove that your algorithm works. Each inductive proof has two steps: the **base case** and the **inductive case**. Sound familiar? For example, suppose I want to prove that I can climb to the top of a ladder. In the inductive case, if my legs are on a rung, I can put my legs on the next rung. So if I’m on rung 2, I can climb to rung 3.  at’s the inductive case. For the base case, I’ll say that my legs are on rung 1.  Therefore, I can climb the entire ladder, going up one rung at a time.

#### Big O notation revisited
Quicksort is unique because its speed depends on the pivot you choose. Before I talk about quicksort, let’s look at the most common Big O run times again.  

• Simple search : **O(n)**  
• Binary search : **O(log n)**  
• Quick sort : **O(n log n)**  
• Selection sort : **O(n2)**  
• Traveling salesman : **O(n!)**  

#### Average case vs. worst case
If you always choose a random element in the array as the pivot, quicksort will complete in O(n log n) time on average.

In the worst case, there are O(n) levels, so the algorithm will take O(n) * O(n) = O(n2) time.


### Recap
• D&C works by breaking a problem down into smaller and smaller pieces. If you’re using D&C on a list, the base case is probably an empty array or an array with one element.
• If you’re implementing quicksort, choose a random element as the pivot.  e average runtime of quicksort is O(n log n)!
• The constant in Big O notation can matter sometimes.  at’s why quicksort is faster than merge sort.
• The constant almost never matters for simple search versus binary search, because O(log n) is so much faster than O(n) when your list gets big.

## Chapter 5 - HashTable :

#### Hash function:
In technical terminology, we’d say that a hash function “maps strings to numbers.” You might think there’s no discernable pattern to what number you get out when you put a string in. But there are some requirements for a hash function:
• It needs to be consistent. For example, suppose you put in “apple” and get back “4”. Every time you put in “apple”, you should get “4” back. Without this, your hash table won’t work.
• It should map different words to different numbers. For example, a hash function is no good if it always returns “1” for any word you put in. In the best case, every different word should map to a different number.

#### Use cases :
1. Using hash tables for lookups : Phonebook example  
2. Preventing duplicate entries : Voting booth example  
3. Using hash tables as a cache : Fb Server / Niece asking mars distance example

Recap
To recap, hashes are good for  
• Modelling relationships from one thing to another thing  
• Filtering out duplicates  
• Caching/memorising data instead of making your server do work  

#### Collisions

When a hash function assigns two keys to the same slot *Collision* occurs. Suppose we have a hash function which assigns the 1 slots alphabetically. We start assigning them with 0 = apple,1 = banana, Problem occurs when we want to assign slot to avocado since  a == 0 = apple. That slot it already assigned.
Simplest workaround is : if multiple keys map to the same slot, start a linked list at that slot.


There are two lessons here:
• Your hash function is really important. Your hash function mapped all the keys to a single slot. Ideally, your hash function would map keys evenly all over the hash.  
• If those linked lists get long, it slows down your hash table a lot. But they won’t get long if you use a good hash function!
Hash functions are important. A good hash function will give you very few collisions.  
• Hash tables use an array for storage

#### Performance

In the average case, hash tables take O(1) for everything. O(1) is called constant time. In the worst case, a hash table takes O(n)—linear time. To avoid worst case we need :

• A low load factor  
• A good hash function  

##### Load Factor
               No of items of hash table
              ____________________________
loadFactor =      Total no of slots

Having a load factor greater than 1 means you have more items than slots in your array. Once the load factor starts to grow, you need to add more slots to your hash table. This is called resizing.  
With a lower load factor, you’ll have fewer collisions, and your table will perform better. A good rule of thumb is, resize when your load factor is greater than 0.7.

##### A good hash function
A good hash function distributes values in the array evenly.  
A bad hash function groups values together and produces a lot of collisions.  

#### Recap
• You can make a hash table by combining a hash function with an array.  
• Collisions are bad. You need a hash function that minimizes collisions.  
• Hash tables have really fast search, insert, and delete.  
• Hash tables are good for modeling relationships from one item to another item.  
• Once your load factor is greater than .07, it’s time to resize your hash table.  
• Hash tables are used for caching data (for example, with a web server).  
• Hash tables are great for catching duplicates.  

## Chapter 6 - Breadth first search :

 The algorithm to solve a shortest-path problem is called breadth- first search. A graph models a set of connections. For example, suppose you and your friends are playing poker, and you want to model who owes whom money. Here’s how you could say, “Alex owes Rama money.”

 --------           --------  
 | ALEX | --------> | Rama |  
 --------           --------  
Graphs are made up of nodes and edges. A node can be directly connected to many other nodes. Those nodes are called its neighbours. In this graph, Rama is Alex’s neighbour.

### Finding the shortest path
These are the two questions that breadth- first search can answer for you:
• Question type 1: Is there a path from node A to node B? (Is there a mango seller in your network?)
• Question type 2: What is the shortest path from node A to node B? (Who is the closest mango seller?)

Another way to see this is, first-degree connections are added to the search list before second-degree connections.
You just go down the list and check people to see whether each one is a mango seller. The first-degree connections will be searched before the second- degree connections, so you’ll find the mango seller closest to you. Breadth-first search *not only  finds a path from A to B*, it also *finds the shortest path*.

#### Queues : B-F search uses queue


The algorithm will keep going until either  
• A mango seller is found, or  
• The queue becomes empty, in which case there is no mango seller.  

### Exercises :
6.1 : Length of shortest path from *start* to *finish* is **2**.
6.2 : Length of shortest path from *cab* to *bat* is **2**. cab - cat - bat
6.3 : **A**
1. Wake up.   
2. Shower.  
3. Eat breakfast.  
4. Brush teeth.  
Ans : **Invalid** Can not eat before brush.  

**B**
1. Wake up.   
2. Brush teeth.  
3. Eat breakfast.  
4. Shower.  
Ans : **Valid**

**C**
1. Shower.   
2. Wake up.  
3. Brush teeth.  
4. Eat breakfast.  
Ans : **Invalid** Can not take shower before waking up.

6.5 : **A & C** both graphs are also trees.

### Recap
• Breadth-first search tells you if there’s a path from A to B.  
• If there’s a path, breadth- first search will find the shortest path.  
• If you have a problem like “Find the shortest X,” try modelling your problem as a graph, and use breadth-first search to solve.  
• A directed graph has arrows, and the relationship follows the direction of the arrow (rama -> adit means “rama owes adit money”).  
• Undirected graphs don’t have arrows, and the relationship goes both ways (ross - rachel means “ross dated rachel and rachel dated ross”).  
• Queues are FIFO (First In, First Out).  
• Stacks are LIFO (Last In, First Out).  
• You need to check people in the order they were added to the search list, so the search list needs to be a queue. Otherwise, you won’t get the shortest path.  
• Once you check someone, make sure you don’t check them again. Otherwise, you might end up in an infnite loop.  


## Chapter 7 - Dijkstra's Algorithm :
Breadth first gives us the shortest path from **A** to **B** however it is not necessary that shortest path would be a *fastest* path. With use of **Dijkstra's Algorithm** we can find out the fastest path.

Steps to Dijkstra’s algorithm:
1. Find the **cheapest** node. This is the node you can get to in the least amount of time.  
2. Update the costs of the neighbors of this node.  
3. Repeat until you’ve done this for every node in the graph.  
4. Calculate the final path.  

##### Weighted & Unweighted graph :
A graph having weight associated with it's edges is called as **Weighted graph** and the one which does not has any weight associated with it's edges is called as **Unweighted graph**.  

To calculate the shortest path in an unweighted graph, use *breadth-first search*. To calculate the shortest path in a weighted graph, use *Dijkstra’s algorithm*.   

*Cycle* in graph means to nodes are pointing at each other. same as *directed graph* from chapter 6. *Dijkstra’s algorithm* will never give shortest path if we follow cycle in graph. It only works with **directed acyclic graphs**, called DAGs for short.  


##### Negative-weight edges :
Dijkstra’s algorithm assumed that because you were processing the poster node, there was no faster way to get to that node.  at assumption only works if you have no negative-weight edges. So you can’t use **negative-weight** edges with Dijkstra’s algorithm. If you want to find the shortest path in a graph that has negative-weight edges, there’s an algorithm for that! It’s called the *Bellman-Ford* algorithm.

### Recap
• Breadth-first search is used to calculate the shortest path for an unweighted graph.  
• Dijkstra’s algorithm is used to calculate the shortest path for a weighted graph.  
• Dijkstra’s algorithm works when all the weights are positive.  
• If you have negative weights, use the Bellman-Ford algorithm.  

## Chapter 8 - Greedy Algorithm :
In technical terms: at each step you pick the *locally optimal solution*, and in the end you’re left with the *globally optimal* solution.

- Overlapping class examples  
- The knapsack problem. Greedy thief.  


- The Radio set-covering problem   
When calculating the exact solution will take too much time, an approximation algorithm will work. Approximation algorithms are judged by
• How fast they are
• How close they are to the optimal solution
Greedy algorithms are a good choice because not only are they simple to come up with, but that simplicity means they usually run fast.

To recap:
• Sets are like lists, except sets can’t have duplicates.
• You can do some interesting operations on sets, like union, intersection, and difference.

#### Traveling salesman problem :
Suppose salesman has to visit 4 cities find the shortest path that will take him to all the cities.

1. Start with 2 cities :-  
  - Assume Start at A then visit B
  - Assume Start at B then visit A  
  That means **2 Cities = 2 ways**
2. Now consider 3 cities :-  
  - Assume starting at A : you have 2 possible routes (visit B first then C or visit C first then B).   
  - Assume starting at B : you have 2 possible routes (visit A first then C or visit C first then A).   
  - Assume starting at C : you have 2 possible routes (visit A first then B or visit B first then A).   
  That means **3 Cities = 6 ways**
3. Now consider 4 cities :-  
  - Assume starting at A : 6 possible routes (As calculated in **2**)   
  - Assume starting at B : 6 possible routes (As calculated in **2**)   
  - Assume starting at C : 6 possible routes (As calculated in **2**)   
  - Assume starting at D : 6 possible routes (As calculated in **2**)   
  That means Four possible start cities, with six possible routes for each start city  = 4 * 6 = **4 Cities = 24 ways**.  

##### Pattern :

1 ---> **1 Route**  
2 ---> 2 Start cities * **1 Route** for each city = **2 total routes**  
3 ---> 3 Start cities * **2 Routes** = **6 total routes**  
4 ---> 4 Start cities * **6 Routes** = **24 total routes**  
5 ---> 5 Start cities * **24 Routes** = **120 total routes**  
and so on...
This is called as *factorial function*. Suppose we have 10 cities. How many possible routes are there? *10! = 3,628,800*. As we can see number of routes becomes big very fast. That is why it’s impossible to compute the "correct" solution for the traveling-salesperson problem if you have a large number of cities.


##### Approximating  
What’s a good approximation algorithm for the traveling salesperson? Something simple that finds a short path. See if you can come up with an answer before reading on.
Here’s how I would do it: arbitrarily pick a start city.  en, each time the salesperson has to pick the next city to visit, they pick the closest unvisited city.  


### Recap
• Greedy algorithms optimize locally, hoping to end up with a global optimum.  
• NP-complete problems have no known fast solution.  
• If you have an NP-complete problem, your best bet is to use an approximation algorithm.  
• Greedy algorithms are easy to write and fast to run, so they make good approximation algorithms.  

### Exercises
8.1 You work for a furniture company, and you have to ship furniture all over the country. You need to pack your truck with boxes. All the boxes are of different sizes, and you’re trying to maximise the space you use in each truck. How would you pick boxes to maximise space? Come up with a greedy strategy. Will that give you the optimal solution?
**Ans** : Find the largest possible box which will fit and then repeat same.

8.2 You’re going to Europe, and you have seven days to see everything you can. You assign a point value to each item (how much you want to see it) and estimate how long it takes. How can you maximize the point total (seeing all the things you really want to see) during your stay? Come up with a greedy strategy. Will that give you the optimal solution?
**Ans** : Find the items with highest point of value which will fit into timeframe and repeat same.

For each of these algorithms, say whether it’s a greedy algorithm or not.
8.3 Quicksort : **NO**  
8.4 Breadth- first search : **YES**  
8.5 Dijkstra’s algorithm : **YES**  

8.6 A postman needs to deliver to 20 homes. He needs to find the shortest route that goes to all 20 homes. Is this an NP-complete problem?  
**Answer: Yes**  
8.7 Finding the largest clique in a set of people (a clique is a set of people who all know each other). Is this an NP-complete problem?  
**Answer: Yes**  
8.8 You’re making a map of the USA, and you need to color adjacent states with different colors. You have to find the minimum number of colors you need so that no two adjacent states are the same color. Is this an NP-complete problem?  
**Answer: Yes**  

## Chapter 9 - Dynamic Programming :

#### The knapsack problem :
Suppose you are a thief and want to steal items so that you get maximum money's worth goods? You can only carry 4lbs.
- Stereo 3000$ - 4 lbs
- Laptop 2000$ - 4 lbs
- Guitar 1500$ - 1 lbs

List of all the possibilities :
1. No items : 0$  
2. Guitar : 1500$  
3. Stereo : 3000$  
4. Laptop : 2000$  
5. Guitar + Stereo : 3500$ but **Doesn't fit** weight 5lbs  
6. Guitar + Laptop : 3500$  
7. Stereo + Laptop : 5000$ but **Doesn't fit** weight 8lbs  
8. Guitar + Stereo + Laptop : 6500$ but **Doesn't fit** weight 9lbs   

This works, but it’s really slow. For 3 items, you have to calculate 8 possible sets. For 4 items, you have to calculate 16 sets. With every item you add, the number of sets you have to calculate doubles! This algorithm takes **O(2^n)** time, which is very, very slow.

• Dynamic programming is useful when you’re trying to optimize something given a constraint. In the knapsack problem, you had to maximize the value of the goods you stole, constrained by the size of the knapsack.  
• You can use dynamic programming when the problem can be broken into discrete subproblems, and they don’t depend on each other.  

##### Some general tips follow :
• Every dynamic-programming solution involves a grid.  
• The values in the cells are usually what you’re trying to optimize. For the knapsack problem, the values were the value of the goods.  
• Each cell is a subproblem, so think about how you can divide your problem into subproblems. That will help you  figure out what the axes are.  

##### Making the grid :
What does the grid for this problem look like? We need to answer these questions:  
• What are the values of the cells?  
• How do you divide this problem into subproblems?  
• What are the axes of the grid?  

### Recap
• Dynamic programming is useful when you’re trying to optimize something given a constraint.  
• You can use dynamic programming when the problem can be broken into discrete subproblems.  
• Every dynamic-programming solution involves a grid.  
• The values in the cells are usually what you’re trying to optimize.  
• Each cell is a subproblem, so think about how you can divide your problem into subproblems.  
• There’s no single formula for calculating a dynamic-programming solution.


## Chapter 10 k-nearest neighbours
It is used in classification, If we put two fruits grapefruit and orange on graph with x axis as SIZE and y axis as COLOUR. Then to classify items on the graph we might take neighbouring items and compare them. More neighbors are orange means it is orange.   

Same happens with the netflix recommendation system. Users with same choice of movies are placed together on graph and then ask them to rate the movies. Based on their ratings movies are recommended to other users.

##### Regression
It is like taking an average.
These are the two basic things you’ll do with KNN—classification and regression:  
• Classification = categorization into a group  
• Regression = predicting a response (like a number)  
**Bakery** example

##### Cosine similarity
Cosine similarity doesn’t measure the distance between two vectors. Instead, it compares the angles of the two vectors. Suppose when two users like the movie but one prefers to rate 5 star to best of best movies and another prefers to rate 5 to all of the movies which he likes. So in this case even if they both like same movie by using old distance formula we won't be able to plot them as neighbors even if they have similar movie choice.

##### Picking good features
When you’re working with KNN, it’s really important to pick the right features to compare against. Picking the right features means  
• Features that directly correlate to the movies you’re trying to recommend  
• Features that don’t have a bias (for example, if you ask the users to only rate comedy movies, that doesn’t tell you whether they like action movies)  


### Recap
• KNN is used for classification and regression and involves looking at the k-nearest neighbors.  
• Classification = categorization into a group.  
• Regression = predicting a response (like a number).  
• Feature extraction means converting an item (like a fruit or a user)
into a list of numbers that can be compared.  
• Picking good features is an important part of a successful KNN algorithm.  



[1]: https://www.amazon.com/Grokking-Algorithms-illustrated-programmers-curious/dp/1617292230
[2]: http://stackoverflow.com/a/72694/139117
[3]: https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
