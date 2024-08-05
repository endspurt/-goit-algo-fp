import turtle
import math

def draw_branch(t, branch_length, level):
    if level > 0:
        t.forward(branch_length)
        angle = 45

        # Ліва гілка
        t.left(angle)
        draw_branch(t, branch_length / 2, level - 1)

        # Права гілка
        t.right(2 * angle)
        draw_branch(t, branch_length / 2, level - 1)

        # Повернення до початкової позиції
        t.left(angle)
        t.backward(branch_length)

def draw_pythagoras_tree(level):
    window = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)  # Повернути черепаху на 90 градусів вліво

    draw_branch(t, 100, level)
    window.mainloop()

# Запитати рівень рекурсії у користувача
level = int(input("Введіть рівень рекурсії: "))
draw_pythagoras_tree(level)
