from sqlalchemy import Column, ForeignKey, Boolean, Integer, Numeric, String, Text, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Optional, Iterable
from sqlalchemy.orm import Session
from application.models.dao import *
import functools
import traceback
Base = declarative_base()

class Orders(Base):
    __tablename__ = "orders"
    id = Column(Integer, nullable=False, primary_key=True)
    date = Column(DateTime(), default=datetime.now, nullable=False) 

class Ingredients(Base):
    __tablename__ = 'ingredients'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    count = Column(Integer, default=0)

class Dishes(Base):
    __tablename__ = "dishes"
    id = Column(Integer, nullable=True, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)

class Storage(Base):
    __tablename__ = "storage"
    id = Column(Integer, nullable=True, primary_key=True)
    id_ingredient = Column(Integer, ForeignKey('ingredients.id'), nullable=False)
    count = Column(Integer, nullable=False, unique=False)
    expiry_date = Column(Date())

class DishesIngredients(Base):
    __tablename__ = 'dishes_ingredients'
    id_dish = Column(Integer, ForeignKey('dishes.id'), nullable=False, primary_key=True)
    id_ingredient = Column(Integer, ForeignKey('ingredients.id'),primary_key=True)
    amount = Column(Integer, nullable=False, unique=False)

class OrdersDishes(Base):
    __tablename__ = 'orders_dishes'
    id_dish = Column(Integer, ForeignKey('dishes.id'), nullable=False, primary_key=True)
    id_order = Column(Integer, ForeignKey('ingredients.id'),primary_key=True)
    amount = Column(Integer, nullable=False, unique=False)

class Test(Base):
    __tablename__ = 'TEST'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
