#!/usr/bin/python3
"""model_state module"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
import sys


Base = declarative_base()


class State(Base):
    '''
    contains the class definition of a State and
    an instance Base = declarative_base()
    '''
    __tablename__ = "states"
    id = Column(
            Integer,
            primary_key=True,
            unique=True,
            nullable=False,
            autoincrement=True
            )

    name = Column(String(128), nullable=False)
