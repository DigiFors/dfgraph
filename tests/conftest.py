from dfgraph import *
import pytest
from sqlalchemy.orm import make_transient
import copy
from pathlib import Path

# https://www.nerdwallet.com/blog/engineering/5-pytest-best-practices/

def add_node(g:Graph, n:Node):
    session = g.session
    session.add(n)
    session.commit()

def delete_node(g:Graph, n:Node):
    session = g.session
    session.query(Node).filter_by(id=n.id).delete()
    session.commit()

@pytest.fixture
def connect():
    name = 'test.db'
    yield Graph(name)
    # Path(name).unlink()


@pytest.fixture
def apple():
    return Node('Apple Computer Company', ['company', 'start-up'], {'founded': 'April 1, 1976'})
    

@pytest.fixture
def steve_wozniak():
    return Node('Steve Wozniak', ['person','engineer','founder'])


@pytest.fixture
def steve_jobs():
    return Node('Steve Jobs', ['person','designer','founder'])


@pytest.fixture
def ronald_wayne():
    return Node('Ronald Wayne', ['person','administrator','founder'])


@pytest.fixture
def mike_arkkula():
    return Node('Mike Markkula', ['person','investor'])

@pytest.fixture
def add_nodes(connect, apple, steve_wozniak, steve_jobs, ronald_wayne, mike_arkkula):
    graph = connect
    s = graph.session
    nodes = [apple, steve_wozniak, steve_jobs, ronald_wayne, mike_arkkula]
    for n in nodes:
        s.add(n)
    s.commit()
    yield graph, len(nodes)
    s.query(Node).delete()
    s.commit()


@pytest.fixture
def delete_wozniak(add_nodes, steve_wozniak):
    graph, length = add_nodes
    s = graph.session
    n = copy.deepcopy(steve_wozniak) #copy.deepcccopy()
    # make_transient(n)
    s.query(Node).filter_by(id=n.id).delete()
    s.commit()
    yield graph, length -1
    steve_wozniak = copy.deepcopy(n)
    s.add(steve_wozniak)
    s.commit()

@pytest.fixture
def delete_nodes(add_nodes, apple, steve_wozniak, steve_jobs, ronald_wayne, mike_arkkula):
    graph,length = connect
    s = graph.session
    s.query(Node).delete()
    s.commit()
    yield graph, 0
    nodes = [apple, steve_wozniak, steve_jobs, ronald_wayne, mike_arkkula]
    for n in nodes:
        s.add(n)
    s.commit()
