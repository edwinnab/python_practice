class Point:
    def reset(self):
       self.x = 0
       self.y = 0

p1 = Point()
p1.x = 3
p1.y = 4

print(p1.x)
print(p1.y)
p1.reset()
print(p1.x)
print(p1.y)

