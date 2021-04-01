import math

class Node:
    def __init__(self, name, xCor, yCor):
        self.name = name
        self.xCor = xCor
        self.yCor = yCor
        self.neighbors = []
        self.neighborsDistance = []
        self.prevNodeIndex = -1
        self.prevNodeDistance = 0
        self.gValue = 0
        self.hValue = 0
        self.fValue = 0

class OpenList(object): #Modified for Node with fValue as priority
    def __init__(self):
        self.queue = []
  
    def isEmpty(self):
        return len(self.queue) == 0
    
    def isExist(self, name):
        for node in self.queue:
            if node.name == name:
                return True
        return False 
  
    def push(self, data):
        self.queue.append(data)
  
    def pop(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i].fValue > self.queue[max].fValue:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()

def Heuristic(currentNode, targetNode):
    return round(math.sqrt(pow((currentNode.xCor - targetNode.xCor), 2) + pow((currentNode.xCor - targetNode.xCor), 2)))

def FindNodeInList(nodeList, nodeName):
    for index in range(len(nodeList)):
        if nodeList[index].name == nodeName:
            return index
    return -1

def CalculateG(currentNode, index):
    gValue = currentNode.neighborsDistance[index]

    tempNode = currentNode
    while(tempNode.prevNodeIndex != -1):
        gValue += tempNode.prevNodeDistance
        tempNode = tempNode.neighbors[tempNode.prevNodeIndex]
    
    return gValue
        

def AStarSearch(nodes, startNode, endNode):
    openList = OpenList()
    closeList = []

    startNode.hValue = Heuristic(startNode, endNode)
    startNode.fValue = startNode.gValue + startNode.hValue

    currentNode = startNode

    while(currentNode.name != endNode.name):
        for index in range(len(currentNode.neighbors)):
            if (FindNodeInList(closeList, currentNode.neighbors[index].name) == -1 and not openList.isExist(currentNode.neighbors[index].name)):

                neighbor = currentNode.neighbors[index]

                # currentNode.neighbors[index].gValue = CalculateG(currentNode, index)
                neighbor.hValue = Heuristic(neighbor, endNode)
                # currentNode.neighbors[index].fValue = currentNode.neighbors[index].gValue + currentNode.neighbors[index].hValue
                tempG = CalculateG(currentNode, index)
                tempF = tempG + neighbor.hValue

                if(neighbor.fValue == 0 or tempF < neighbor.fValue):
                    neighbor.gValue = tempG
                    neighbor.fValue = tempF
                    neighbor.prevNodeIndex = FindNodeInList(neighbor.neighbors, currentNode.name)
                    neighbor.prevNodeDistance = neighbor.neighborsDistance[neighbor.prevNodeIndex]


                openList.push(neighbor)

        closeList.append(currentNode)
        currentNode = openList.pop()

nodes = [
    Node('A', 0, 0),
    Node('B', 5, 0),
    Node('C', 2, 2),
    Node('D', 3, 4),
    Node('E', 5, 5)
]

# #A
# nodes[0].neighbors = [nodes[1], nodes[3]]
# nodes[0].neighborsDistance = [7, 6]

# #B
# nodes[1].neighbors = [nodes[0], nodes[2], nodes[4]]
# nodes[1].neighborsDistance = [7, 5, 10]

# #C
# nodes[2].neighbors = [nodes[1], nodes[4]]
# nodes[2].neighborsDistance = [5, 5]

# #D
# nodes[3].neighbors = [nodes[0], nodes[4]]
# nodes[3].neighborsDistance = [6, 4]

# #E
# nodes[4].neighbors = [nodes[2], nodes[3]]
# nodes[4].neighborsDistance = [5, 4]

# AStarSearch(nodes, nodes[0], nodes[2])

# nodesAmount = int(input("Enter node amount: "))

# while(nodesAmount > 0):
#     nodesAmount -= 1
#     nodeName = input("Enter node name: ")
#     xCor, yCor = map(int, input("Enter x and y coordinate (seperate by space): ").split())

#     nodes.append(Node(nodeName, xCor, yCor))


# rulesAmount = input("Enter rules amount: ")
# while(rulesAmount > 0):
#     rulesAmount = input("Enter ")

def Result(nodes, startNode, endNode):
    routeList = []
    route = ""
    totalCost = endNode.gValue
    currentNode = endNode
    while (currentNode.prevNodeIndex != -1):
        routeList.append(currentNode.name)
        currentNode = currentNode.neighbors[currentNode.prevNodeIndex]
    routeList.append(currentNode.name)

    routeList.reverse()

    for nodeName in routeList:
        route += nodeName
        route += '-'
    
    route = route[:-1]
    
    print("Optimal route: " + route)
    print("Total cost: "  + str(totalCost))

nodes = []

with open('Nodes.txt') as fileInput:
    nodesAmount = int(fileInput.readline())
    while(nodesAmount > 0):
        nodesAmount -= 1
        line = fileInput.readline().split(" ")
        line[1] = line[1].replace('\n', '')
        line[1] = line[1].replace('(', '')
        line[1] = line[1].replace(')', '')
        line[1] = line[1].split(',')
        nodes.append(Node(line[0], int(line[1][0]), int(line[1][1])))
    rulesAmount = int(fileInput.readline())
    while(rulesAmount > 0):
        rulesAmount -= 1
        line = fileInput.readline().split(" ")
        line[0] = line[0].split('-')
        line[1] = line[1].replace('\n', '')
        
        index0 = FindNodeInList(nodes, line[0][0])
        index1 = FindNodeInList(nodes, line[0][1])

        nodes[index0].neighborsDistance.append(int(line[1]))
        nodes[index1].neighborsDistance.append(int(line[1]))
        nodes[index0].neighbors.append(nodes[index1])
        nodes[index1].neighbors.append(nodes[index0])

    if(nodes != []):
        line = fileInput.readline().split(" ")
        startIndex = FindNodeInList(nodes, line[0])
        endIndex = FindNodeInList(nodes, line[1])

        AStarSearch(nodes, nodes[startIndex], nodes[endIndex])
        
        Result(nodes, nodes[startIndex], nodes[endIndex])
