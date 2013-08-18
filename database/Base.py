__author__ = 'matt'
from sqlalchemy.ext.declarative import declarative_base

class Base():
    base = declarative_base()

    def get_base(self):
        if self.base == None:
            self.base = declarative_base()
        return self.base