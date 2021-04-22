from dfgraph import Node, Relationship, Graph

graph = Graph('apple.db')
session = graph.session

n1 = Node('Apple Computer Company', ['company', 'start-up'], {'founded': 'April 1, 1976'})
n2 = Node('Steve Wozniak', ['person','engineer','founder'])
n3 = Node('Steve Jobs', ['person','designer','founder'])
n4 = Node('Ronald Wayne', ['person','administrator','founder'])
n5 = Node('Mike Markkula', ['person','investor'])
session.add(n1)
session.add(n2)
session.add(n3)
session.add(n4)
session.add(n5)

session.commit()

rel1 = Relationship(n2, 'founded', n1)
rel2 = Relationship(n3, 'founded', n1)
rel3 = Relationship(n4, 'founded', n1)
rel4 = Relationship(n5, 'invested', n1, {'equity': 80000, 'debt': 170000})
rel5 = Relationship(n1, 'divested', n4, {'amount': 800, 'date': 'April 12, 1976'})
rel6 = Relationship(n2, '', n3)
rel6 = Relationship(n1, '', n3)

session.add(rel1)
session.add(rel2)
session.add(rel3)
session.add(rel4)
session.add(rel5)
session.add(rel6)

session.commit()