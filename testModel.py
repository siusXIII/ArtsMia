from model.model import Model

myModel = Model()
myModel.buildGraph()
print("Num nodi:",myModel.getNumNodes(),"; Num archi:", myModel.getNumEdges())

myModel.getInfoConnessa(1234)
