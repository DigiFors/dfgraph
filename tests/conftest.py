from dfgraph import *
import pytest
from sqlalchemy.orm import make_transient
import copy
from pathlib import Path


def add_node(g: Graph, n: Node):
    session = g.session
    session.add(n)
    session.commit()


def delete_node(g: Graph, n: Node):
    session = g.session
    session.query(Node).filter_by(id=n.id).delete()
    session.commit()


@pytest.fixture(params=["", "test.db"])
def connect(request):
    yield Graph(request.param)
    # if request.param:
    #     Path(request.param).unlink()



@pytest.fixture
def fill(connect):
    graph = connect
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
    yield graph



# @pytest.fixture
# def delete_nodes(add_nodes, apple, steve_wozniak, steve_jobs, ronald_wayne, mike_arkkula):
#     graph, length = connect
#     s = graph.session
#     s.query(Node).delete()
#     s.commit()
#     yield graph, 0
#     nodes = [apple, steve_wozniak, steve_jobs, ronald_wayne, mike_arkkula]
#     for n in nodes:
#         s.add(n)
#     s.commit()
