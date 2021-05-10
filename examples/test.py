from dfgraph import *


graph = Graph()
apple = Node('Apple Computer Company', ['company', 'start-up'], {'founded': 'April 1, 1976'})
wozniak = Node('Steve Wozniak', ['person', 'engineer', 'founder'])
jobs = Node('Steve Jobs', ['person', 'designer', 'founder'])
wayne = Node('Ronald Wayne', ['person', 'administrator', 'founder'])
arkkula = Node('Mike Markkula', ['person', 'investor'])
graph.add(apple)

graph.add(wozniak)
graph.add(jobs)
graph.add(wayne)
graph.add(arkkula)
Relation(wozniak, 'founded', apple)
Relation(jobs, 'founded', apple)
Relation(wayne, 'founded', apple)
Relation(arkkula, 'invested', apple, {'equity': 80000, 'debt': 170000})
Relation(apple, 'divested', wayne, {'amount': 800, 'date': 'April 12, 1976'})
Relation(wozniak, '', jobs)
Relation(apple, '', jobs)

print("Before delete:", len(graph.nodes), len(graph.relations))
for r in graph.relations:
    print(r.source.name, r.to_dict())

wozniak.delete()

print("After delete:", len(graph.nodes), len(graph.relations))

for r in graph.relations:
    if r.source.name == "Steve Wozniak":
        print("FOUND", r.source.name, r.to_dict())
    else:
        print(r.source.name, r.to_dict())
