from dfgraph import Node, Relationship, Graph
from pathlib import Path

if Path('apple.db').is_file():
    import fill

graph = Graph('apple.db')
session = graph.session

# like
print("###################")
print("all Steve's")
result = session.query(Node).filter(Node.name.like('%Steve%'))
for row in result:
    print(str(row.to_json()))

print("###################")
print("all persons and founders")
result = session.query(Node).filter(Node._types.like('%person%') , Node._types.like("%founder%"))
for row in result:
    print(str(row.to_json()))



workingnode = session.query(Node).filter_by(name='Ronald Wayne').first()

print("###################")
print("all relations of Ronald Wayne")

result = workingnode.relation_sources.all()
result += workingnode.relation_targets.all()

for row in result:
    print(str(row.to_json()))

print("###################")
print("all Nodes connected to Ronald Wayne")
result = workingnode.targets(iterate=True, relations=['founded'])

for row in result:
    print(str(row.to_json()))

print("###################")
print("all Nodes connected to Ronald Wayne by founded")
result = workingnode.targets(iterate=True, relations=['founded'])

for row in result:
    print(str(row.to_json()))

