from dfgraph import Node, Relationship, db_session, init_db

init_db()

graph = db_session

n1 = Node('Apple Computer Company', ['company', 'start-up'], {'founded': 'April 1, 1976'})
n2 = Node('Steve Wozniak', ['person','engineer','founder'])
n3 = Node('Steve Jobs', ['person','designer','founder'])
n4 = Node('Ronald Wayne', ['person','administrator','founder'])
n5 = Node('Mike Markkula', ['person','investor'])
graph.add(n1)
graph.add(n2)
graph.add(n3)
graph.add(n4)
graph.add(n5)

graph.commit()

rel1 = Relationship(n2, 'founded', n1)
rel2 = Relationship(n3, 'founded', n1)
rel3 = Relationship(n4, 'founded', n1)
rel4 = Relationship(n5, 'invested', n1, {'equity': 80000, 'debt': 170000})
rel5 = Relationship(n1, 'divested', n4, {'amount': 800, 'date': 'April 12, 1976'})
rel6 = Relationship(n2, '', n3)
rel6 = Relationship(n1, '', n3)

graph.add(rel1)
graph.add(rel2)
graph.add(rel3)
graph.add(rel4)
graph.add(rel5)
graph.add(rel6)

graph.commit()