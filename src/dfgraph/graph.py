from .database import DBNode, DBGraph, DBRelation
from .seralizer import *
import uuid
import weakref


class Node(SerializerInterface):
    def __init__(self, name: str, types=[], body={}, id=None, parent=None):
        self.id = id
        if self.id is None:
            self.id = str(uuid.uuid4())
        self.name = name
        self.types = types
        self.body = body
        self.parent = parent
        self.relations = []

    def set_parent(self, parent):
        self.parent = parent
        if self.parent:
            self.parent.relations += self.relations

    def add_relation(self, relation):
        self.relations.append(relation)
        if self.parent:
            self.parent.relations.append(relation)

    def to_dict(self) -> dict:
        return dict(id=self.id, name=self.name, types=self.types, body=self.body)

    def delete(self):
        if self.parent:
            print("found", len(self.relations))
            self.parent.nodes.remove(self)
            for r in self.relations:
                print("found", r.to_dict())
                self.parent.relations.remove(r)
        self.relations.clear()

    def __del__(self):
        self.relations.clear()

    def __eq__(self, other):
        return self.id == other.id


class Relation(SerializerInterface):
    def __init__(self, source: Node, relation: str, target: Node, properties={}):
        self.source = source
        self.target = target
        self.relation = relation
        self.properties = properties
        if source:
            self.source.add_relation(self)

    def to_dict(self) -> dict:
        return dict(source_id=self.source.id,
                    relation=self.relation,
                    target_id=self.target.id,
                    properties=self.properties)

    def __eq__(self, other):
        print("relation")
        return self.source.id == other.source.id and self.target.id == other.target.id


class Graph(SerializerInterface):
    def __init__(self, dbfile=""):
        self.nodes = []
        self.relations = []
        if dbfile:
            graph = DBGraph(dbfile)
            session = graph.session
            nodes = session.query(DBNode).all()
            for node in nodes:
                self.nodes.append(Node(node.name, node.body, node.types(), node.id, self))

            relations = session.query(DBRelation).all()
            for relation in relations:
                source = None
                target = None
                for node in self.nodes:
                    if relation.source_id == node.id:
                        source = node
                    break
                for node in self.nodes:
                    if relation.target_id == node.id:
                        target = node
                    break
                if source and target:
                    Relation(source, relation.relation, target, relation.properties)

    def save(self, db):
        graph = DBGraph(db)
        session = graph.session
        for node in self.nodes:
            session.add(DBNode(node.name, node.types, node.body, node.id))
        session.commit()

        for relation in self.relations:
            source = session.query(DBNode).filter_by(id=relation.source.id).first()
            target = session.query(DBNode).filter_by(id=relation.target.id).first()
            session.add(DBRelation(source, relation.relation, target, node.id))
        session.commit()

    def add(self, elem) -> bool:
        if isinstance(elem, Node):
            self.nodes.append(elem)
            elem.set_parent(self)
            return True
        elif isinstance(elem, Relation):
            self.relations.append(elem)
            return True
        return False


    def to_dict(self) -> dict:
        res = dict()
        nodes = []
        for node in nodes:
            nodes.append(node.to_dict())
        res["nodes"] = nodes

        relations = []
        for relation in relations:
            relations.append(relation.to_dict())
        res["relations"] = relations
