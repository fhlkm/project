import sys
import operator
def main():
	if len(sys.argv)!=2:
		print "#################################################"
		print "Please input 'Python create.py arg1(EGO NODE ID)'"
		# return
	egonode=str(0)
	#print egonode
	network=dict()

	network[egonode]=[]
	f=open("facebook_combined.txt","r")
	for this_line in f:
		if egonode==this_line[:len(egonode)]:
			this_node=this_line.split()[1]
			network[this_node]=[]
			network[egonode].append(this_node)
	f.close()
	print "This network has",len(network),"'s nodes."
	f=open(egonode+".edges","r")
	for this_line in f:
		this_node=this_line.split()[0]
		if this_node not in network:
			network[this_node]=[]
		network[this_node].append(this_line.split()[1])
	f.close()
	print "Find all the neighbors of each node"
	nodes=dict()
	for node in network:
		nodes[node]=len(network[node])+1
	sorted_nodes=sorted(nodes.items(),key=operator.itemgetter(1))
	print sorted_nodes
	total = len(sorted_nodes)
	f=open(egonode+".feat","r")
	c=open(egonode+"1.csv","w")
	for this_line in f:
         i=0
		# for node in sorted_nodes:
		# 	if node[0]==this_line.split()[0]:
		# 		if i<total/3:
		# 			c.write(this_line[:-2]+this_line.split()[len(this_line.split())-1]+" 1\n")
		# 		elif i<total/3*2:
		# 			c.write(this_line[:-2]+this_line.split()[len(this_line.split())-1]+" 2\n")
		# 		else:
		# 			c.write(this_line[:-2]+this_line.split()[len(this_line.split())-1]+" 3\n")
		# 	i=i+1
         for node in sorted_nodes:
			if node[0]==this_line.split()[0]:
				if i<1*total/9:
					c.write(this_line[:-2]+this_line.split()[len(this_line.split())-1]+" c1\n")
				else:
					c.write(this_line[:-2]+this_line.split()[len(this_line.split())-1]+" c2\n")
			i=i+1
	f.close()
	e=open(egonode+".egofeat","r")
	this_line=e.readline()
	c.write(egonode+" "+this_line[:-2]+this_line.split()[len(this_line.split())-1]+" c2\n")
	c.close()
	print "Created file:",egonode,"1.csv"
def main2():
	if len(sys.argv)!=2:
		print "#################################################"
		print "Please input 'Python create.py arg1(EGO NODE ID)'"
		# return
	egonode=str(0)
	#print egonode
	network=dict()

	network[egonode]=[]
	f=open("facebook_combined.txt","r")
	for this_line in f:
		if egonode==this_line[:len(egonode)]:
			this_node=this_line.split()[1]
			network[this_node]=[]
			network[egonode].append(this_node)
	f.close()
	print "This network has",len(network),"'s nodes."
	f=open(egonode+".edges","r")
	for this_line in f:
		this_node=this_line.split()[0]
		if this_node not in network:
			network[this_node]=[]
		network[this_node].append(this_line.split()[1])
	f.close()
	print "Find all the neighbors of each node"
	nodes=dict()
	for node in network:
		nodes[node]=len(network[node])+1
	sorted_nodes=sorted(nodes.items(),key=operator.itemgetter(1))
	print sorted_nodes
	total = len(sorted_nodes)
	f=open(egonode+".feat","r")
	c=open(egonode+"2.csv","w")
	for this_line in f:
         i=0
		# for node in sorted_nodes:
		# 	if node[0]==this_line.split()[0]:
		# 		if i<total/3:
		# 			c.write(this_line[:-2]+this_line.split()[len(this_line.split())-1]+" 1\n")
		# 		elif i<total/3*2:
		# 			c.write(this_line[:-2]+this_line.split()[len(this_line.split())-1]+" 2\n")
		# 		else:
		# 			c.write(this_line[:-2]+this_line.split()[len(this_line.split())-1]+" 3\n")
		# 	i=i+1
         for node in sorted_nodes:
			if node[0]==this_line.split()[0]:
				if i<2*total/9:
					c.write(this_line[:-2]+this_line.split()[len(this_line.split())-1]+" c1\n")
				else:
					c.write(this_line[:-2]+this_line.split()[len(this_line.split())-1]+" c2\n")
			i=i+1
	f.close()
	e=open(egonode+".egofeat","r")
	this_line=e.readline()
	c.write(egonode+" "+this_line[:-2]+this_line.split()[len(this_line.split())-1]+" c2\n")
	c.close()
	print "Created file:",egonode,"2.csv"

main()
main2()



