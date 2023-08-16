import turtle as t
colors = ['red', 'green', 'blue',
          'yellow', 'gray', 'white']
t.bgcolor('black')
t.speed(0)  # максимальная скорость
angle = 360 / len(colors) - 1

for x in range(200):
    t.pencolor(colors[x % len(colors)])
    # t.pencolor(colors[x % len(colors[0:2])])
    t.width(x // 100 +1)
    t.forward(x)
    t.left(angle)
t.mainloop()


