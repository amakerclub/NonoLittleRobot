from __future__ import division
import time


class Servo:
    """a Servo is a tuple of (position,id)"""
    def __init__(self,iId,iPosition):
        self._id = iId
        self._position = iPosition
        
    @property
    def id(self):
        return self._id
    
    @property
    def position(self):
        return self._position

    def toDict(self):
        return {'id': self._id , 'position' : self._position }

    def fromDict(self, dict):
        self._id  = dict('id')
        self._position = dict('position')


    def print2(self):
        print("Servo: _id: %d, _position: %d" % (self._id,self._position))
