from pygame import * 
from pygame.locals import * 
import pygame

from OpenGL.GL import * 
from OpenGL.GLU import * 

from enum import Enum 
from overrides import overrides 

import numpy as np
from shapes_2d import Shape2D 

class TwoAxis(Enum):
    X = 0  # x point pos
    Y = 1  # y point pos 


class Square_v2(Shape2D): # Idea: Vertices from rotate one point 90 degree * 4 times will get square points

    def __init__(self, center_point):
        # rotate angle indicates one point to another point angle in center point
        super(Square_v2, self).__init__(center_point=center_point, rotate_angle=(np.pi/2))# since it is square

    @overrides
    def get_verticies_edges(self, start_point):
        points = int ((2*np.pi)/ (self.rotate_angle))
        for i in range(points):
            next_start_point = self.get_pt_theta_rotate_pos(theta=self.rotate_angle,  point=start_point)
            self.edges.append([start_point, next_start_point]) # makes edge
            start_point = next_start_point
            if start_point not in self.vertices:
                self.vertices.append(start_point)
        return self.vertices, self.edges



def show_square(point, angle): # rotate angle indicates square rotate animation angle
    squarev2 = Square_v2([0.5,0.5])
    vertices, edges = squarev2.get_verticies_edges(start_point=point)
    glBegin(GL_LINES)
    for edge in edges:
        glVertex2fv(edge[0])
        glVertex2fv(edge[1])
    glEnd()
    return rotate(point, angle)

def rotate(point, theta):
    return Shape2D.get_pt_theta_rotate_pos(theta=theta, point=point)
        # (point@np.array( [[np.cos(theta), #solve matri)
        #             np.sin(theta)], [-np.sin(theta) , np.cos(theta)]] )).tolist()

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
        point = show_square(point, (-np.pi/10))
        pygame.display.flip()
        pygame.time.wait(1000)

if __name__ == "__main__":
    main([1,0.8])
