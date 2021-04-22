import pytest
from pathlib import Path
from tests.conftest import *

@pytest.mark.filterwarnings('ignore::sqlalchemy.exc.SADeprecationWarning') 
def test_create(connect):
    connect
    assert Path('test.db').is_file()

@pytest.mark.filterwarnings('ignore::sqlalchemy.exc.SADeprecationWarning') 
def test_fill_nodes_general(add_nodes):
    graph, length = add_nodes
    session = graph.session
    assert len(session.query(Node).all()) == length

@pytest.mark.filterwarnings('ignore::sqlalchemy.exc.SADeprecationWarning')
@pytest.mark.parametrize("name, exits",[('Steve Wozniak', True), ('Mike Markkula', True), ('does not exists', False)])
def test_exists_nodes_by_name(add_nodes, name, exits):
    graph, length = add_nodes
    session = graph.session
    assert (len(session.query(Node).filter_by(name=name).all())==1) == exits


# @pytest.mark.filterwarnings('ignore::sqlalchemy.exc.SADeprecationWarning')
# @pytest.mark.parametrize("name, exits",[('Steve Wozniak', False), ('Mike Markkula', True), ('does not exists', False)])
# def test_exists_nodes_by_name_after_delete_wozniak(delete_wozniak, name, exits):
#     graph, length = delete_wozniak
#     session = graph.session
#     print("for", name, "found ",session.query(Node).filter_by(name=name).first())
#     assert (len(session.query(Node).filter_by(name=name).all())==1) == exits