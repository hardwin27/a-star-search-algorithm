import math

class Node:
    def __init__(self, name, xCor, yCor):
        self.name = name
        self.xCor = xCor
        self.yCor = yCor
        self.neighbors = [] #2D list
        self.prevNode = None
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
                return true
        return false 
  
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

def AStarSearch(nodes, startNode, endNode):
    openList = OpenList()
    closeList = [startingNode]

    startingNode.hValue = Heuristic(startNode, endNode)
    startingNode.fValue = startingNode.gValue + startingNode.hValue

    currentNode = startingNode

    # while(currentNode.name != endNode.name):
    #     for neighbor in currentNode.neighbors:
    #         if (FindNodeInList(nodes, neighbor[0].name) == -1 and not openList.isExist(neighbor[0].name)):
    #             openList.push(neighbor[0])
    #             costToStart = 0
    #             tempCurrent = neighbor[0]
    #             while(true):
    #                 prevNodeIndex = FindNodeInList(nodes, tempCurrent.prevNode.name)
    #                 costToStart 
