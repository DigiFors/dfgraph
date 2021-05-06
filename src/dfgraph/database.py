from sqlalchemy import create_engine, Column, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, backref, relationship, object_session, Session
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from multiprocessing import Lock

import uuid
import json
from .seralizer import SerializerInterface

mutex = Lock()
current_engines = {}

# def init_db():
#     Model.metadata.create_all(bind=engine)

# https://docs.sqlalchemy.org/en/14/orm/join_conditions.html
DBModel = declarative_base(name='DBModel')


class DBGraph:
    def __init__(self, db_name: str, root=None):
        self.name = db_name

        global current_engines, mutex
        engine = None
        with mutex:
            if self.name in current_engines.keys():
                engine = current_engines[self.name]['engine']
                current_engines[self.name]['sessions'] += 1
            else:

                engine = create_engine('sqlite:///' + self.name,
                                       convert_unicode=True)
                DBModel.metadata.create_all(bind=engine)

                with engine.connect() as con:
                    con.execute("PRAGMA foreign_keys = TRUE;")
                current_engines.update({self.name: {"engine": engine, "sessions": 1}})

        self.session = scoped_session(sessionmaker(autocommit=False,
                                                   autoflush=False,
                                                   bind=engine))
        DBModel.query = self.session.query_property()

    def __del__(self):
        # self.close()
        global current_engines, mutex
        with mutex:
            if self.name in current_engines.keys():
                current_engines[self.name]['sessions'] -= 1
                if current_engines[self.name]['sessions'] == 0:
                    engine = current_engines[self.name]['engine']
                    # if engine:
                    #     engine.close()
                del current_engines[self.name]


class DBRelation(DBModel, SerializerInterface):
    __tablename__ = 'relationship'
    source_id = Column('source', String(36), ForeignKey("nodes.id"), primary_key=True)
    target_id = Column('target', String(36), ForeignKey("nodes.id"), primary_key=True)
    relation = Column('relation', Text)
    _properties = Column('properties', Text)

    source = relationship("DBNode", primaryjoin="DBRelation.source_id == DBNode.id",
                          backref=backref('relation_targets', lazy='dynamic'))
    target = relationship("DBNode", primaryjoin="DBRelation.target_id == DBNode.id",
                          backref=backref('relation_sources', lazy='dynamic'))

    def __init__(self, source, relation: str, target, properties={}):
        self.relation = relation
        self._properties = json.dumps(properties)
        source.relation_targets.append(self)
        target.relation_sources.append(self)

    @hybrid_property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, properties: {}):
        self._properties = json.dumps(properties)

    @properties.getter
    def properties(self):
        return json.loads(self._properties)

    def to_dict(self):
        return dict(source=self.source_id, target=self.target_id, relation=self.relation, properties=self.properties)


class DBNode(DBModel, SerializerInterface):
    __tablename__ = 'nodes'
    id = Column('id', String(36), primary_key=True, index=True)
    name = Column('name', String(64))
    _body = Column('body', Text)
    _types = Column('types', Text)

    def __init__(self, name, types=[], body={}, id=str(uuid.uuid4())):
        self.id = id
        self.name = name
        self._body = json.dumps(body)
        self._types = ','.join(types)  # .lower()

    @hybrid_property
    def body(self):
        return self._body

    @body.setter
    def body(self, body: {}):
        self._body = json.dumps(body)

    @body.getter
    def body(self):
        return json.loads(self._body)

    @hybrid_property
    def types(self):
        return self._types

    @types.setter
    def types(self, types):
        self._types = ','.join(types)

    @hybrid_method
    def types(self):
        return self._types.split(",")

    @hybrid_method  # property
    def targets(self, relations=None, iterate=False):
        result = []
        uniques = []

        def search(node: DBNode):
            query = object_session(node).query(DBNode) \
                .filter(DBRelation.target_id == DBNode.id)
            res = []
            if relations:
                res = query.filter(DBRelation.source_id == node.id,
                                   DBRelation.relation.in_(tuple(relations))).all()
            else:
                res = query.filter(DBRelation.source_id == node.id).all()

            if res:
                for elem in res:
                    print(elem.to_dict())
                    if not elem.id in uniques:
                        result.append(elem)
                        uniques.append(elem.id)
                        if iterate:
                            search(elem)

        search(self)
        return result

    def to_dict(self):
        return dict(id=self.id, name=self.name, body=self.body, types=self.types())
