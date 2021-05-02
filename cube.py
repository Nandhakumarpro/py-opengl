from pygame import * 
from pygame.locals import * 
import pygame

from OpenGL.GL import * 
from OpenGL.GLU import * 
from enum import Enum 

from copy import copy 

class AxisPos(Enum):
    # [0, 1, 2]
    #  X, Y, Z
    X = 0 
    Y = 1
    Z = 2 

class Cube:

    def __init__(self, center_point):
        self.center_point = center_point
        self.vertices = []
        self.edges = []

    def get_vertices_edges(self, curr_point:list, xis_to_go:list):
        if curr_point in self.vertices:
            return 
        self.vertices.append(curr_point)
        for xis in xis_to_go:            
            copy_xis_to_go = xis_to_go.copy()
            copy_xis_to_go.remove(xis)
            adj_point = self.get_pair_point(curr_point.copy(), xis)
            self.edges.append([curr_point, adj_point])
            self.get_vertices_edges(adj_point, copy_xis_to_go)
        return self.vertices, self.edges

    def get_pair_point(self, curr_point, axis):
        # @curr_point List[int, 3]@sample[1,1,1] @axis ∈ {0,1,2}
        rep = ( (self.center_point[axis.value]*2) -   
            # %sample center_point = [1, 1, 1], axis.value=1 --> (1*2)-
                 curr_point[axis.value] ) 
                # %sample curr_point=[2,2,2] %lrdy axis.value --> 2 
        curr_point[axis.value] = rep 
        return curr_point 

    def get_pair_point(self, curr_point, axis):
        rep = ( (self.center_point[axis.value]*2) - curr_point[axis.value] ) 
        curr_point[axis.value] = rep 
        return curr_point  

    def __doc__():
        return '''
            center_point = [0, 0, 0] #@sample
            verticies, edges = [], []
            get_vertices_edges([1,1,1], list(AxisPos)) # @call
            verticies = 

        '''



def show_cube():
    cube = Cube([0,0,0])  
    vertices, edges = cube.get_vertices_edges([1, 1, 1], list(AxisPos))
    glBegin(GL_LINES)
    for edge in edges:
        glVertex3fv(edge[0])
        glVertex3fv(edge[1])
    glEnd()

def main():
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
        glRotatef(90, 0, 0.5, 0.5)        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        show_cube()
        pygame.display.flip()
        pygame.time.wait(1000)

if __name__ == "__main__":
    main() 



