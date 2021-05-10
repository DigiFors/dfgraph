import pytest
from .conftest import *


@pytest.mark.filterwarnings('ignore::sqlalchemy.exc.SADeprecationWarning')
@pytest.mark.parametrize(
    "name,exist",
    [("not existing", False),
     ("Apple Computer Company", True),
     ("Steve Wozniak", True),
     ("Steve Jobs", True),
     ("Ronald Wayne", True),
     ("Mike Markkula", True)],
)
def test_nodes(fill, name, exist):
    graph = fill
    found = False
    for node in graph.nodes:
        if node.name == name:
            found = True
            break
    assert found == exist


@pytest.mark.filterwarnings('ignore::sqlalchemy.exc.SADeprecationWarning')
@pytest.mark.parametrize(
    "json,exist",
    [
        ({"source": 'Steve Wozniak', "relation": 'founded', "target": 'Apple Computer Company'}, True),
        ({"source": 'Steve Jobs', "relation": 'founded', "target": 'Apple Computer Company'}, True),
        ({"source": 'Ronald Wayne', "relation": 'founded', "target": 'Apple Computer Company'}, True),
        ({"source": 'Mike Markkula', "relation": 'invested', "target": 'Apple Computer Company'}, True),
        ({"source": 'Apple Computer Company', "relation": 'divested', "target": 'Ronald Wayne'}, True),
        ({"source": 'Steve Wozniak', "relation": '', "target": 'Steve Jobs'}, True),
        ({"source": 'Apple Computer Company', "relation": '', "target": 'Steve Jobs'}, True),
    ],
)
def test_relations(fill, json, exist):
    graph = fill
    found = False
    for relation in graph.relations:
        if relation.source.name == json["source"]\
                and relation.relation == json["relation"]\
                and relation.target.name == json["target"]:
            found = True
            break
    assert found == exist


@pytest.mark.filterwarnings('ignore::sqlalchemy.exc.SADeprecationWarning')
@pytest.mark.parametrize(
    "json,exist",
    [
        ({"source": 'Steve Wozniak', "relation": 'founded', "target": 'Apple Computer Company'}, True),
        ({"source": 'Steve Wozniak', "relation": '', "target": 'Steve Jobs'}, True),
        ({"source": 'Apple Computer Company', "relation": '', "target": 'Steve Jobs'}, False),
    ],
)
def test_relations_of_wozniak(fill, json, exist):
    graph = fill
    found = False
    wozniak = None
    for node in graph.nodes:
        if node.name == 'Steve Wozniak':
            wozniak = node
            break
    for relation in wozniak.relations:
        if relation.source.name == json["source"]\
                and relation.relation == json["relation"]\
                and relation.target.name == json["target"]:
            found = True
    assert found == exist

# after deleting


@pytest.mark.filterwarnings('ignore::sqlalchemy.exc.SADeprecationWarning')
@pytest.mark.parametrize(
    "name,exist",
    [("not existing", False),
     ("Apple Computer Company", True),
     ("Steve Wozniak", False),
     ("Steve Jobs", True),
     ("Ronald Wayne", True),
     ("Mike Markkula", True)],
)
def test_nodes(delete_wozniak, name, exist):
    graph = delete_wozniak
    found = False
    for node in graph.nodes:
        if node.name == name:
            found = True
            break
    assert found == exist


@pytest.mark.filterwarnings('ignore::sqlalchemy.exc.SADeprecationWarning')
@pytest.mark.parametrize(
    "json,exist",
    [
        ({"source": 'Steve Wozniak', "relation": 'founded', "target": 'Apple Computer Company'}, False),
        ({"source": 'Steve Jobs', "relation": 'founded', "target": 'Apple Computer Company'}, True),
        ({"source": 'Ronald Wayne', "relation": 'founded', "target": 'Apple Computer Company'}, True),
        ({"source": 'Mike Markkula', "relation": 'invested', "target": 'Apple Computer Company'}, True),
        ({"source": 'Apple Computer Company', "relation": 'divested', "target": 'Ronald Wayne'}, True),
        ({"source": 'Steve Wozniak', "relation": '', "target": 'Steve Jobs'}, False),
        ({"source": 'Apple Computer Company', "relation": '', "target": 'Steve Jobs'}, True),
    ],
)
def test_relations(delete_wozniak, json, exist):
    graph = delete_wozniak
    print("delete", len(graph.relations))
    found = False
    for relation in graph.relations:
        if relation.source.name == json["source"]\
                and relation.relation == json["relation"]\
                and relation.target.name == json["target"]:
            found = True
            break
    assert found == exist


@pytest.mark.filterwarnings('ignore::sqlalchemy.exc.SADeprecationWarning')
@pytest.mark.parametrize(
    "json,exist",
    [
        ({"source": 'Steve Wozniak', "relation": 'founded', "target": 'Apple Computer Company'}, True),
        ({"source": 'Steve Wozniak', "relation": '', "target": 'Steve Jobs'}, True),
        ({"source": 'Apple Computer Company', "relation": '', "target": 'Steve Jobs'}, False),
    ],
)
def test_relations_of_wozniak(add_wozniak, json, exist):
    graph = add_wozniak
    found = False
    wozniak = None
    for node in graph.nodes:
        if node.name == 'Steve Wozniak':
            wozniak = node
            break
    for relation in wozniak.relations:
        if relation.source.name == json["source"]\
                and relation.relation == json["relation"]\
                and relation.target.name == json["target"]:
            found = True
    assert found == exist
