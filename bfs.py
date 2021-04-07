from queue import Queue
def BFS(adj_list):
	visited = {}
	s="A"
	output=[]
	queue=Queue()
	for node in adj_list:
		visited[node]=False
	print(visited)
	queue.put(s)
	visited[s]=True
	print(visited)
	while not queue.empty():
		u=queue.get()
		output.append(u)
		for i in adj_list[u]:
			if not visited[i]:
				visited[i]=True
				queue.put(i)
	return output

adj_list={
	"A":["B","D"],
	"B":["A","C"],
	"C":["A","E","F"],
	"D":["A",'E',"F"],
	"E":["D","F","G"],
	"F":["D","E","H"],
	"G":["E","H"],
	"H":["G","F"],
}
print(BFS(adj_list))
