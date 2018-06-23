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

## Chapter 3 - QuickSort :

#### Divide & conquer
It's a strategy of breaking down a problem to it's lowest state and then working on it again. Here is how D&C works:  
1. Figure out a simple case as the base case.
2. Figure out how to reduce your problem and get to the base case.
D&C isn’t a simple algorithm that you can apply to a problem. Instead, it’s a way to think about a problem. Let’s do one more example.

#### Euclid's algorithms   
“If you find the biggest box that will work for this size, that will be the biggest box that will work for the entire farm.” Khan academy has a good explanation here on [Euclid's algorithm][3]:

#### Inductive proofs
#### Big O notation revisited
#### Average case vs. worst case

### Recap
• D&C works by breaking a problem down into smaller and smaller pieces. If you’re using D&C on a list, the base case is probably an empty array or an array with one element.
• If you’re implementing quicksort, choose a random element as the pivot.  e average runtime of quicksort is O(n log n)!
•  e constant in Big O notation can matter sometimes.  at’s why quicksort is faster than merge sort.
•  e constant almost never matters for simple search versus binary search, because O(log n) is so much faster than O(n) when your list gets big.




[1]: https://www.amazon.com/Grokking-Algorithms-illustrated-programmers-curious/dp/1617292230
[2]: http://stackoverflow.com/a/72694/139117
[3]: https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
