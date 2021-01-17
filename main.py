from dialog import Popup
import pygame
from random import randint


WHITE = (230, 230, 230)
BLUE = (1,100,255)
#YELLOW = (0, 200, 0)

class Main:
    def __init__(self, width, height, algorithm):
        self.width = width
        self.height = height
        self.running = True
        self.window = pygame.display.set_mode((self.width, self.height))
        self.array = [randint(5, self.height) for _ in range(int(self.width//(self.width*0.01)))] 
        self.algorithm = algorithm
        pygame.display.set_caption("Sorting visualizer")

    def on_event(self, event):
        # :on_event - evet handeling
        if event.type == pygame.QUIT:
            self.running = False

    def draw_rectangles(self, j):
        # :draw_rectangles - draw 100 bars no mather of application width
        onehundred = int(self.width//(self.width*0.01))
        width = int(self.width*0.01)
        for i in range(onehundred):
            rect_height = self.array[i]
            rect = pygame.Rect(width*i, self.height-rect_height, width, rect_height)
            pygame.draw.rect(self.window, BLUE, rect, 0)
            pygame.draw.rect(self.window, WHITE, rect, 1)
            # if i == j:
            #   pygame.draw.rect(self.window, YELLOW, rect, 0)        

    def bubble_sort(self, i, j):
        first_number = self.array[j]
        second_number = self.array[j+1]

        if (first_number > second_number):
            self.array[j], self.array[j+1] = self.array[j+1], self.array[j]

        if i < len(self.array):
            j +=1
            if j >= (len(self.array)-i-1):
                j = 0
                i += 1
        return i, j

    def insertion_sort(self, i, j, key, while_loop):
        if not while_loop and i < len(self.array):
            key = self.array[i]
            j = i - 1

        if j >= 0 and self.array[j] > key:
            self.array[j+1] = self.array[j]
            j = j - 1
            while_loop = True
        else:
            self.array[j+1] = key
            while_loop = False
            i += 1

        return i, j, key, while_loop

    def selection_sort(self, i, j, min_index, for_loop):
        if not for_loop and i < len(self.array)-1:
            min_index = i
            j = i + 1
        if j < len(self.array):
            for_loop = True
            if self.array[j] < self.array[min_index]:
                min_index = j
            self.array[min_index], self.array[i] = self.array[i], self.array[min_index]
            j += 1
            
        else:
            for_loop = False
            if i < len(self.array)-1 and j < len(self.array):
                self.array[min_index], self.array[i] = self.array[i], self.array[min_index]
            i += 1  
        
        return i, j, min_index, for_loop  

    def run(self):
        # :run - main application loop
        if self.algorithm == 'Bubble Sort':
            i = j = 0
        elif self.algorithm == 'Insertion Sort':
            i = 0
            j = key = -1
            while_loop = False
        elif self.algorithm == "Selection Sort":
            i = 0
            j = min_index = -1
            for_loop = False

        while self.running:
            for event in pygame.event.get():
                self.on_event(event)
            
            self.window.fill(WHITE)
            self.draw_rectangles(j)

            if self.algorithm == 'Bubble Sort':
                i, j = self.bubble_sort(i, j)
            elif self.algorithm == 'Insertion Sort':
                i, j, key, while_loop = self.insertion_sort(i, j, key, while_loop)
            elif self.algorithm == "Selection Sort":
                i, j, min_index, for_loop = self.selection_sort(i, j, min_index, for_loop)
            
            pygame.display.update()
            # clock = pygame.time.Clock()
            # clock.tick(100)
        pygame.quit()
  

if __name__ == "__main__":
    algorithm = Popup().choice
    app = Main(900, 600, algorithm)
    app.run()