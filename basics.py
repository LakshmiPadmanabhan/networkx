import networkx as nx
import matplotlib.pyplot as plt
g=nx.Graph() #Create graph1
G=nx.Graph() #Creatw graph2
#Build Graph1
#Add nodes
g.add_node('1')
g.add_node('2')
g.add_node('3')
g.add_node('4')
g.add_node('5')
g.add_node('6')
g.add_node('7')
g.add_node('8')
#Add Edges
g.add_edge('1','2')
g.add_edge('1','4')
g.add_edge('3','2')
g.add_edge('3','4')
g.add_edge('5','6')
g.add_edge('5','8')
g.add_edge('7','8')
g.add_edge('7','6')
g.add_edge('1','5')
g.add_edge('2','6')
g.add_edge('7','3')
g.add_edge('4','8')
#Build Graph2
#Add nodes
G.add_node('a')
G.add_node('b')
G.add_node('c')
G.add_node('d')
G.add_node('g')
G.add_node('h')
#Add Edges
G.add_edge('a','g')
G.add_edge('a','h')
G.add_edge('a','i')
G.add_edge('b','g')
G.add_edge('b','h')
G.add_edge('b','j')
G.add_edge('c','g')
G.add_edge('c','j')
G.add_edge('c','i')
G.add_edge('d','h')
G.add_edge('d','j')
G.add_edge('d','i')
nx.draw(g,with_labels=1)
plt.show()
nx.draw(G,with_labels=1)
plt.show()
#Write Edge Information of 2 graphs into 2 different files
nx.write_edgelist(g,'edgeList1.txt');
nx.write_edgelist(G,'edgeList2.txt');
#Check whether the Graphs are Eulerian
print('Euler Graphs:')
print('g: ',nx.is_eulerian(g))
print('G: ',nx.is_eulerian(G))
#Check whether the graphs are isomorphic
print('Isomorphic:',nx.is_isomorphic(g,G))
