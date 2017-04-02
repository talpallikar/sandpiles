from random import randrange

class Sandpile:
#sandpiles are a 2d matrix of  numbers

    def __init__(self, matrix):
        self.matrix = matrix

    def display_Pile(self):
        for x in range(len(self.matrix)):
            print(self.matrix[x])
        print()

    def seed(self, low, high):
        i=0
        while i < len(self.matrix):
            j=0
            while j < len(self.matrix[i]):
                self.matrix[i][j] = randrange(low,high)
                j+=1
            i+=1

    def topple(i,j)
        if self.matrix[i][j]>4:
            self.matrix[i][j]-=4
            try:
                self.matrix[i-1][j-1]+=1
                self.matrix[i-1][j+1]+=1
                self.matrix[i+1][j-1]+=1
                self.matrix[i+1][j+1]+=1
            except IndexError

    def update(self):
        i = 0
        while i < len(self.matrix):
            j=0
            while j < len(self.matrix[i]):
                self.topple()

def create(x_dim,y_dim):
    for x in range(0,x_dim):
        print()

def add(a,b):

    c = Sandpile(a.matrix)
    i=0
    while i < len(a.matrix):
        j=0
        while j < len(a.matrix[i]):
            c.matrix[i][j] = a.matrix[i][j] + b.matrix[i][j]
            j+=1
        i+=1
    return c

# matrix_1 = Sandpile([[0,1,2],[3,4,5],[6,7,8]])
# matrix_2 = Sandpile([[0,1,2],[3,4,5],[6,7,8]])

# print("original matrix 1:")
# matrix_1.display_Pile()
# print("original matrix 2:")
# matrix_2.display_Pile()

# matrix_1.seed(0,3)
# matrix_2.seed(0,3)

# print("seeded matrix 1:")
# matrix_1.display_Pile()
# print("seeded matrix 2:")
# matrix_2.display_Pile()

# matrix_3 = add(matrix_1,matrix_2)

# print("result of addition: ")
# matrix_3.display_Pile()