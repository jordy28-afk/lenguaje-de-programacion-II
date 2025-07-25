from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class LetrasUNACentrada:
    def __init__(self):
        glutInit()
        glutInitDisplayMode(GLUT_RGBA | GLUT_SINGLE)
        glutInitWindowSize(800, 600)
        glutInitWindowPosition(100, 100)
        glutCreateWindow("UNA centrado - OpenGL".encode('utf-8'))

        glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo negro

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-10, 10, -10, 10, -10, 10)

        glutDisplayFunc(self.dibujar)
        glutMainLoop()

    def dibujar(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1.0, 1.0, 0.0)  # Amarillo
        glLineWidth(3)

        glBegin(GL_LINES)

        # ===== LETRA U (de -4 a -2) =====
        glVertex2f(-4, 3); glVertex2f(-4, -3)
        glVertex2f(-4, -3); glVertex2f(-2, -3)
        glVertex2f(-2, -3); glVertex2f(-2, 3)

        # ===== LETRA N (de -1 a +1) =====
        glVertex2f(-1, -3); glVertex2f(-1, 3)
        glVertex2f(-1, 3);  glVertex2f(1, -3)
        glVertex2f(1, -3);  glVertex2f(1, 3)

        # ===== LETRA A (de +2 a +4) =====
        glVertex2f(2, -3); glVertex2f(3, 3)     # Diagonal izquierda
        glVertex2f(3, 3); glVertex2f(4, -3)     # Diagonal derecha
        glVertex2f(2.4, 0); glVertex2f(3.6, 0)  # Barra horizontal media

        glEnd()
        glFlush()

# Ejecutar
if __name__ == "__main__":
    LetrasUNACentrada()