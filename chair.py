from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from numpy import *

def myinit():
    glMatrixMode(GL_PROJECTION)
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    gluPerspective(60,1,0.1,50)
    gluLookAt(10,10,10,0,0,0,0,1,0)

def draw_chair(x,y,z,b,n,m):
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(b,n,m)
    glLoadIdentity()
    glTranslate(x, y, z)
    glScale(2, 2, .5)
    glutSolidCube(2)
    glPopAttrib()
    glPopMatrix()
def draw_chair1(s,d,f,z,v,c):
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(z,v,c)
    glLoadIdentity()
    glTranslate(s,d,f)
    glScale(2, .5, 2)
    glutWireCube(2)
    glPopAttrib()
    glPopMatrix()
def leg(q,w,e,u,i,o):
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(u,i,o)
    glLoadIdentity()
    glTranslate(q,w,e)
    glScale(.5, 2, .5)
    glutSolidCube(2)
    glPopAttrib()
    glPopMatrix()
def draw_cube():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)

    draw_chair(-5,2,0,1,0,0)
    draw_chair1(-4.5,0,2,1,0,0)
    leg(-3.5,-3,0,1,0,0)
    leg(-7, -3, 0,1,0,0)
    leg(-3.5, -3, 3.2,1,0,0)
    leg(-7, -3, 3.2,1,0,0)

    draw_chair(3.2, 2, 0,0,0,1)
    draw_chair1(3.5, 0, 2,0,0,1)
    leg(4.8, -3, 0,0,0,1)
    leg(1.5, -3, 0,0,0,1)
    leg(4.8, -3, 3.2,0,0,1)
    leg(1.5, -3, 3.2,0,0,1)

    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"chair")
glutDisplayFunc(draw_cube)
glutIdleFunc(draw_cube)
myinit()
glutMainLoop()
