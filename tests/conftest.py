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


@pytest.fixture
def connect():
    yield Graph("")
    # if request.param:
    #     Path(request.param).unlink()


@pytest.fixture
def connect_db():
    yield Graph("test.db")


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
    Relation(wozniak, 'founded', apple)
    Relation(jobs, 'founded', apple)
    Relation(wayne, 'founded', apple)
    Relation(arkkula, 'invested', apple, {'equity': 80000, 'debt': 170000})
    Relation(apple, 'divested', wayne, {'amount': 800, 'date': 'April 12, 1976'})
    Relation(wozniak, '', jobs)
    Relation(apple, '', jobs)
    yield graph


@pytest.fixture
def delete_wozniak(fill):
    graph = fill
    wozniak = None
    apple = None
    jobs = None
    for node in graph.nodes:
        if node.name == "Steve Wozniak":
            wozniak = node
        if node.name == "Apple Computer Company":
            apple = node
        if node.name == "Steve Jobs":
            jobs = node
    wozniak.delete()
    yield graph
    wozniak = Node('Steve Wozniak', ['person', 'engineer', 'founder'])
    graph.add(wozniak)
    Relation(wozniak, 'founded', apple)
    Relation(wozniak, '', jobs)


@pytest.fixture
def add_wozniak(delete_wozniak):
    graph = delete_wozniak
    apple = None
    jobs = None
    for node in graph.nodes:
        if node.name == "Apple Computer Company":
            apple = node
        if node.name == "Steve Jobs":
            jobs = node
    wozniak = Node('Steve Wozniak', ['person', 'engineer', 'founder'])
    graph.add(wozniak)
    Relation(wozniak, 'founded', apple)
    Relation(wozniak, '', jobs)
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
