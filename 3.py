from queue import PriorityQueue


class State(object):
    def __init__(self, value, parent,
                     start = 0,goal = 0):
        self.children = []
        self.parent = parent
        self.value = value
        self.dist = 0
        if parent:
            self.path =parent.path [:]
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal 
            
        else:
            self.path = [value]
            self.start = start
            self.goal = goal
           
    def GetDist(self):
        pass
    def CreateChildren(self):
        pass
class State_String(State):

    def __init__(self,value,parent,
                start = 0,goal = 0):
        super(State_String,self).__init__(value, parent,start,goal)
        self.dist = self.GetDist()
    def GetDist(self):
            if self.value == self.goal:
                return 0
            dist = 0
            for i in range(len(self.goal)):
                letter = self.goal[i]
                dist += abs(i-self.value.index(letter))
                return dist
    def CreateChildren(self):
        if not  self.children:
            for i in range(len(self.goal)-1):
                val = self.value
                val = val[:i] + val[i+1] + val[i] + val[i+2:]
                child = State_String(val, self)
                self.children.append(child)
class AStar_Solver:
    def __init__(self,start,goal):
        self.path = []
        self.visitedQueue = []
        self.PriorityQueue =  PriorityQueue()
        self.start = start
        self.goal = goal
    def Solve(self):
        StartState = State_String(self.start,0,self.start,self.goal)
        count = 0
        self.PriorityQueue.put((0,count,StartState))
        while(not self.path and self.PriorityQueue.qsize()):
            closestChild = self.PriorityQueue.get()[2]
            closestChild.CreateChildren()
            self.visitedQueue.append(closestChild.value)
            for child in closestChild.children:
                if child.value not in self.visitedQueue:
                    count+=1
                    if not child.dist:
                        self.path= child.path
                        break
                    self.PriorityQueue.put((child.dist,count,child)) 
        if not self.path:
            print ("Goal of" + self.goal + " is not Possible")
            return self.path
if __name__ == "__main__":
    start1 = "abcde"
    goal1 = "eacdb"
    print("Starting>>>")
    a = AStar_Solver(start1, goal1)
    a.Solve()
    for i in range(len(a.path)):
        print("%d)"%i+a.path[i])
def aStarAlgo(start_node, stop_node):
    open_set = set(start_node)
    closed_set = set()
    g = {}
    parents = {}
    g[start_node] = 0
    parents[start_node] = start_node
    while len(open_set) > 0:
        n = None
        #node with lowest f() is found
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        if n == stop_node or Graph_nodes[n] == None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        if n == None:
            print('Path does not exist!')
            return None

        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path found: {}'.format(path))
            return path
        # remove n from the open_list, and add it to closed_list
        open_set.remove(n)
        closed_set.add(n)
    print('Path does not exist!')
    return None

#define fuction to return neighbor and its distance from the passed node
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

def heuristic(n):
    H_dist = {'A': 11,'B': 6,'C': 5,'D': 7,'E': 3,
        'F': 6,'G': 5,'H': 3,'I': 1,'J': 0}
    return H_dist[n]

#graph
Graph_nodes = {
    'A': [('B', 6), ('F', 3)],
    'B': [('A', 6), ('C', 3), ('D', 2)],
    'C': [('B', 3), ('D', 1), ('E', 5)],
    'D': [('B', 2), ('C', 1), ('E', 8)],
    'E': [('C', 5), ('D', 8), ('I', 5), ('J', 5)],
    'F': [('A', 3), ('G', 1), ('H', 7)],
    'G': [('F', 1), ('I', 3)],
    'H': [('F', 7), ('I', 2)],
    'I': [('E', 5), ('G', 3), ('H', 2), ('J', 3)],
}

aStarAlgo('A', 'J')
