# Learning Algorithms

I recently started learning more about Algorithms from [Grokking Algorithms by Aditya Bhargava][1]. I was starting from scratch so though of making this repo to add the basic alorithm code samples & Own notes. I hope along with the code sample I would be able to add my own notes to this repo. :D 


## Search 

There are two types of search one is simple and another is binary. Suppose we want to find a guy named Eric in class of 200 students. Simple search would be like asking everyone in the class wheather he is Eric or not. where as Binary search would be 
more like sorting and then searching. Sorting as in since we know that Eric is a male we will only consider males students in class it's just an example

### Simple Search :
It is like linear search, iterating through each and every element. So worst time to search would be total number of elements.

### Binary search : 
It is like sorting and elemnating possibilities.


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
Recursion is used when it makes the solution clearer.  ere’s no performance bene t to using recursion; in fact, loops are sometimes better for performance. I like this quote by [Leigh Caldwell on Stack Overflow][2] “Loops may achieve a performance gain for your program. Recursion may achieve a performance gain for your programmer. Choose which is more important in your situation!”

### Recap
• Recursion is when a function calls itself.
• Every recursive function has two cases: the base case and the recursive case.
• A stack has two operations: push and pop.
• All function calls go onto the call stack.
• The call stack can get very large, which takes up a lot of memory.




[1]:https://www.amazon.com/Grokking-Algorithms-illustrated-programmers-curious/dp/1617292230
[2]: http://stackoverflow.com/a/72694/139117 
