from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *
x=0
f=True
z=0
def myinit():
    glMatrixMode(GL_PROJECTION)
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    gluPerspective(60,1,.1,50)
    gluLookAt(10,10,10,0,0,0,0,1,0)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    global x
    global f
    global z
    glMatrixMode(GL_MODELVIEW)

######################green################ ISLAM AHMED
    glLoadIdentity()
    glColor3f(0, .3, 0)
    glTranslate(3, 7.5, 9)
    glScale(50, 1, 3)
    glutSolidCube(1)

    glLoadIdentity()
    glColor3f(0, .3, 0)
    glTranslate(3, 5, -6.8)
    glScale(30, 1, 11)
    glutSolidCube(1)

    ###########ROAD
    glLoadIdentity()
    glColor3f(0, 0, 0)
    glTranslate(x, 3, -4)
    glScale(50, 1, 5)
    glutSolidCube(1)

    glLoadIdentity()
    glColor3f(0, 0, 0)
    glTranslate(0, -1.80, -2)
    glScale(80, .5, 10)
    glutSolidCube(1)

#######################road lines  ######3 ISLAM AHMED
    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(4, 1.8, 1.5)
    glScale(2, .1, .5)
    glutSolidCube(1)
    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(0, 1.8, 1.5)
    glScale(2, .1, .5)
    glutSolidCube(1)
    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(-4, 1.8, 1.5)
    glScale(2, .1, .5)
    glutSolidCube(1)
    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(-8, 1.8, 1.5)
    glScale(2, .1, .5)
    glutSolidCube(1)
    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(-12, 1.8, 1.5)
    glScale(2, .1, .5)
    glutSolidCube(1)
    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(8, 1.8, 1.5)
    glScale(2, .1, .5)
    glutSolidCube(1)
    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(12, 1.8, 1.5)
    glScale(2, .1, .5)
    glutSolidCube(1)
    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(16, 1.8, 1.5)
    glScale(2, .1, .5)
    glutSolidCube(1)
    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(-16, 1.8, 1.5)
    glScale(2, .1, .5)
    glutSolidCube(1)

    ########################road lines########################## ISLAM AHMED

    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(4, 1.8, -7)
    glScale(2, .1, .5)
    glutSolidCube(1)
    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(0, 1.8, -7)
    glScale(2, .1, .5)
    glutSolidCube(1)
    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(-4, 1.8, -7)
    glScale(2, .1, .5)
    glutSolidCube(1)
    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(-8, 1.8, -7)
    glScale(2, .1, .5)
    glutSolidCube(1)
    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(-12, 1.8, -7)
    glScale(2, .1, .5)
    glutSolidCube(1)
    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(8, 1.8, -7)
    glScale(2, .1, .5)
    glutSolidCube(1)
    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(12, 1.8, -7)
    glScale(2, .1, .5)
    glutSolidCube(1)
    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(16, 1.8, -7)
    glScale(2, .1, .5)
    glutSolidCube(1)
    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(-16, 1.8, -7)
    glScale(2, .1, .5)
    glutSolidCube(1)
    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(-20, 1.8, -7)
    glScale(2, .1, .5)
    glutSolidCube(1)

    #####################################################3

#########################car
    glLoadIdentity()
    glColor3f(0,0,1)
    glTranslate(x,0,0)
    glScale(1,.25,.5)
    glutSolidCube(5)
#ISLAM AHMED HASSAN
    glLoadIdentity()
    glTranslate(x,0,0)
    glTranslate(0,1.25,0)
    glScale(.5,.25,.5)
    glutSolidCube(5)

    glColor(0.4,.40,0.4)
    glLoadIdentity()
    glTranslate(x,0,0)
    glTranslate(2,-.5,1.25)
    glRotate(z,0,0,1)
    glutSolidTorus(.125,.5,12,8)

    glLoadIdentity()
    glTranslate(x,0,0)
    glTranslate(-2,-.5,-1.25)
    glRotate(z,0,0,1)
    glutSolidTorus(.125,.5,12,8)

    glLoadIdentity()
    glTranslate(x,0,0)
    glTranslate(2,-.5,-1.25)
    glRotate(z,0,0,1)
    glutSolidTorus(.125,.5,12,8)

    glLoadIdentity()
    glTranslate(x,0,0)
    glTranslate(-2,-.5,1.25)
    glRotate(z,0,0,1)
    glutSolidTorus(.125,.5,12,8)


    glColor(1,0,0)
    glLoadIdentity()
    glTranslate(x,0,0)
    glTranslate(2,-.3,.4)
    glutSolidSphere(.3,20,20)

    glLoadIdentity()
    glTranslate(x,0,0)
    glTranslate(2,-.3,-.4)
    glutSolidSphere(.3,20,20)
############################tree
    glLoadIdentity()
    glColor3f(.153, 0, 0)
    glTranslate(-6, 0, 0)
    glTranslate(x, 3, 0)
    glRotate(90, 1, 0, 0)
    glScale(0.5, .5, -5)
    glutSolidCylinder(1, 1, 10, 10)

    glLoadIdentity()
    glColor3f(.153, 0, 0)
    glTranslate(4, 0, 0)
    glTranslate(x, 3, 0)
    glRotate(90, 1, 0, 0)
    glScale(0.5, .5, -5)
    glutSolidCylinder(1, 1, 10, 10)

    glLoadIdentity()
    glColor((0, 0.6, 0))
    glTranslate(4, 0, 0)
    glTranslate(x, 8, -.4)
    glScale(5, 5, 5)
    glutSolidSphere(.3, 10, 20)

    glLoadIdentity()
    glColor((0, 0.6, 0))
    glTranslate(-7, 0, 0)
    glTranslate(x, 8, -.4)
    glScale(5, 5, 5)
    glutSolidSphere(.3, 10, 20)

    if x > 7:
      f = False

    if x < -14:
        f = True

    if f:
        x+=.01
        z-=1
    else:
        x-=.01
        z+=1


    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"car")
myinit()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()

