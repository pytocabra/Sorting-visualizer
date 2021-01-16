import pygame
from random import randint
from tkinter import *


WHITE = (230, 230, 230)
BLUE = (1,100,255)
#YELLOW = (0, 200, 0)

class Main:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.running = True
        self.window = pygame.display.set_mode((self.width, self.height))
        self.array = [randint(5, self.height) for _ in range(int(self.width//(self.width*0.01)))] 
        pygame.display.set_caption("Sorting visualizer")

    def on_event(self, event):
        # :on_event - evet handeling
        if event.type == pygame.QUIT:
            self.running = False

    def draw_rectangles(self):
        # :draw_rectangles - draw 100 bars no mather of application width
        onehundred = int(self.width//(self.width*0.01))
        width = int(self.width*0.01)
        for i in range(onehundred):
            rect_height = self.array[i]
            rect = pygame.Rect(width*i, self.height-rect_height, width, rect_height)
            pygame.draw.rect(self.window, BLUE, rect, 0)
            # if i == j:
            #   pygame.draw.rect(self.window, YELLOW, rect, 0)

    def swap(self, j):
        self.array[j], self.array[j+1] = self.array[j+1], self.array[j]

    def bubble_sort(self, i, j):
        first_number = self.array[j]
        second_number = self.array[j+1]

        if (first_number > second_number):
            self.swap(j)

        if i < len(self.array):
            j +=1
            if j >= (len(self.array)-i-1):
                j = 0
                i += 1
        return i, j

    def selection_sort(self, i, j, key, while_loop):
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

    def run(self, algorithm):
        # :run - main application loop
        if algorithm == 'bubble sort':
            i = j = 0
        elif algorithm == 'selection sort':
            i = 1
            j = key = -1
            while_loop = False
        while self.running:
            for event in pygame.event.get():
                self.on_event(event)
            
            self.window.fill(WHITE)
            self.draw_rectangles()
            #i, j = self.bubble_sort(i, j)
            i, j, key, while_loop = self.selection_sort(i, j, key, while_loop)
            
            pygame.display.update()
        pygame.quit()

'''
def dialog_popup():
    dialog = Tk()
    label_w = Label(dialog, text='Window width: ')
    win_width = Entry(dialog)
    win_height = Entry(dialog)
    label_h = Label(dialog, text='Window height: ')
    submit = Button(dialog, text='Submit', command='')
    dialog.update()
'''      


if __name__ == "__main__":
    # dialog_popup()
    app = Main(900, 600)
    app.run('selection sort')