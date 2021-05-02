from pygame import * 
from pygame.locals import * 
import pygame

from OpenGL.GL import * 
from OpenGL.GLU import * 
from enum import Enum 

import numpy as np



get_pt_90pos = lambda theta, point: point@np.array( [[np.cos(theta), #solve matri
                 np.sin(theta)], [-np.sin(theta) , np.cos(theta)]] )

get_pt_90neg = lambda theta, point: point@np.array( [[np.cos(theta), #solve matri
                 -np.sin(theta)], [np.sin(theta) , np.cos(theta)]] )

class TwoAxis(Enum):
    X = 0  # x point pos
    Y = 1  # y point pos 

def get_pt_90pos(theta, point):
    # print(theta, point)
    return (point@np.array( [[np.cos(theta), #solve matri
                 np.sin(theta)], [-np.sin(theta) , np.cos(theta)]] )).tolist()

def get_pt_90neg(theta, point):
    # print(theta, point)
    return (point@np.array( [[np.cos(theta), #solve matri
                 -np.sin(theta)], [np.sin(theta) , np.cos(theta)]] )).tolist()    

rotate_functions = { 
    "X":get_pt_90pos, 
    "Y":get_pt_90neg
}

class Square:

    def __init__(self, center_point):
        self.center_point = center_point
        # self.start_point = start_point
        self.vertices = []
        self.edges = []

    def get_verticies_edges(self, curr_point, xis_to_go):
        if curr_point in self.vertices:
            return 
        self.vertices.append(curr_point)
        for xis in xis_to_go:
            copy_xis_to_go = xis_to_go.copy()
            copy_xis_to_go.remove(xis)
            adj_point = self.get_pair_point_rotate_vrsn(curr_point.copy(), xis)
            self.edges.append([curr_point, adj_point])
            self.get_verticies_edges(adj_point, copy_xis_to_go)
    
        return self.vertices, self.edges

    def get_pair_point(self, curr_point, axis):
        # @curr_point List[int, 3]@sample[1,1,1] @axis ∈ {0,1,2}
        rep = ( (self.center_point[axis.value]*2) -   
            # %sample center_point = [1, 1, 1], axis.value=1 --> (1*2)-
                 curr_point[axis.value] ) 
                # %sample curr_point=[2,2,2] %lrdy axis.value --> 2 
        curr_point[axis.value] = rep 
        return curr_point 

    def get_pair_point_rotate_vrsn(self, curr_point, rotate_key):
        return rotate_functions[rotate_key]( np.pi/2, curr_point,)

def show_square(point, angle):
    square = Square([0,0])  
    vertices, edges = square.get_verticies_edges(point, list(rotate_functions.keys()))
    glBegin(GL_LINES)
    for edge in edges:
        glVertex2fv(edge[0])
        glVertex2fv(edge[1])
    glEnd()
    return rotate(point, angle)

def rotate(point, theta):
    return (point@np.array( [[np.cos(theta), #solve matri)
                    np.sin(theta)], [-np.sin(theta) , np.cos(theta)]] )).tolist()

def main(point):
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    glRotatef(0, 0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        glRotatef(0, 0, 0, 0)        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        point = show_square(point, (np.pi/2))
        pygame.display.flip()
        pygame.time.wait(1000)

if __name__ == "__main__":
    main([1,1]) 

# if __name__ == "__main__":
#     square = Square([0,0])
#     vtcs, dgs = square.get_verticies_edges([1,1],list(TwoAxis))
#     print(vtcs, dgs)
