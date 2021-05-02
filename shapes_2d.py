# Base Class 
from abc import ABC, abstractmethod 
import numpy as np
from enum import Enum
from overrides import overrides, final

class Shape2D(ABC):

    class OptionalAttrs(Enum):
        rotate_angle = "rotate_angle"

    def set_attrs(self, attrs, value):
        self.__setattr__(attrs.value, value)

    @staticmethod
    @final
    def get_pt_theta_rotate_pos(theta, point):
        return (point@np.array( [[np.cos(theta), #solve matri
                 np.sin(theta)], [-np.sin(theta) , np.cos(theta)]] )).tolist()

    @staticmethod
    @final
    def get_pt_theta_rotate_neg(theta, point):
        return (point@np.array( [[np.cos(theta), #solve matri
                 -np.sin(theta)], [np.sin(theta) , np.cos(theta)]] )).tolist() 

    def __init__(self, center_point, rotate_angle):
        self.center_point = center_point
        self.rotate_angle = rotate_angle # Acheive vertex points by rotate
        self.vertices, self.edges = [], []

    @abstractmethod
    def get_verticies_edges(self, start_point):
        ''' Logic'''
        return self.vertices, self.edges
