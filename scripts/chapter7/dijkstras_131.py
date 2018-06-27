# Implementing Dijkstras alogrithm in python
graph = {}

graph["start"] = {} 
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {} 
graph["a"]["n"] = 1
graph["b"] = {} 
graph["b"]["a"] = 3 
graph["b"]["n"] = 5
graph["n"] = {}


infinity =  float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["n"] = infinity

parents = {} 
parents["a"] = "start"
parents["b"] = "start"
parents["n"] = None

processed = []


def find_lowest_cost_node(costs):
	lowest_cost =  float("inf")
	lowest_cost_node = None
	for node in costs: #Go through each node.
		cost = costs[node]
		if cost < lowest_cost  and node not in processed: # if its the lowest cost so far and has not been processed yet ...
			lowest_cost = cost  #  set it as the new lowest-cost node.
			lowest_cost_node = node
	return lowest_cost_node


node =  find_lowest_cost_node(costs) # Find the lowest node that you have not processed yet.
while node is not None: #If you have processed all the nodes, this while loop is done. 
	cost = costs[node]
	neighbors = graph[node]
	for n in neighbors.keys():	 	  #Go through all the neighbors of this node
		new_cost = cost + neighbors[n] 
		if costs[n] > new_cost:       # If it is cheaper to get to this neighbor  by going through this node ...
			costs[n] = new_cost # update the cost for this node
			parents[n] = node
	processed.append(node)         #Mark the node as processed.
	node =  find_lowest_cost_node(costs) # Find the next node to process, and loop.


print node



