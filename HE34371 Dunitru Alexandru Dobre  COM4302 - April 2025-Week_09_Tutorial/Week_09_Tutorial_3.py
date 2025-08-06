def draw_triangle(n):
    for i in range(1, n + 1):
        print("*" * i)

def draw_rectangle(w, h=4):
    print("*" * w)
    for _ in range(h - 2):
        print("*" + " " * (w - 2) + "*")
    print("*" * w)

draw_triangle(6)
draw_rectangle(10)