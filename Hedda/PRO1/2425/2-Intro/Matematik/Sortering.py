import matplotlib.pyplot as plt
import numpy as np
import random
import timeit

global switcharoos
switcharoos = 0

def quicksort(lista,line, fig, start = 0):
    global switcharoos
    # Välj ett pivot-element
    pivot = len(lista)-1
    for x in range(start, start+len(lista)-1):
        line[x].set_color('red')
    line[start+pivot].set_color('black')
    fig.canvas.draw()
    fig.canvas.flush_events()
    counter = 0
    if pivot >= 0:
        for i in range(len(lista)-1):
            # Om talet är mindre än pivot-talet flytta det
            if lista[i] <= lista[pivot]:
                if i != counter:
                    lista[i], lista[counter] = lista[counter], lista[i]
                    switcharoos += 1
                    line[i+start].set_height(lista[i])
                    line[counter+start].set_height(lista[counter])
                    #fig.canvas.draw()
                    #fig.canvas.flush_events()
                counter+=1
        # Färga skiten
        for x in range(start, start+counter):
            line[x].set_color('orange')
        fig.canvas.draw()
        fig.canvas.flush_events()
        # Flytta pivot
        lista[pivot], lista[counter] = lista[counter],lista[pivot]
        switcharoos += 1
        #Nu är pivot-talet på rätt plats.
        # Nu delar vi upp listan i två, den före pivot och den efter pivot

        line[start+pivot].set_height(lista[pivot])
        line[start+counter].set_height(lista[counter])
        #line[start+pivot].set_color('blue')
        fig.canvas.draw()
        fig.canvas.flush_events()
    for x in range(start, start+len(lista)):
        line[x].set_color('blue')
    if pivot > 0:
        line[start+pivot].set_color('blue')
    else:
        line[start+pivot].set_color('green')
    line[start+counter-1].set_color('green')
    fig.canvas.draw()
    fig.canvas.flush_events()
    if len(lista) > 1:
        lista[:counter] = quicksort(lista[:counter],line, fig, start)
        lista[counter+1:] = quicksort(lista[counter+1:],line, fig, counter+start+1)
    
    return lista

def quickwrap(lista):
    # Wrapper for the quick sort
    x = np.linspace(0,len(lista), len(lista))
    plt.ion()
    fig = plt.figure()
    ax=fig.add_subplot(111)
    line1 = ax.bar(x, lista, color='blue')
    plt.title("Quick sort")
    plt.xlabel("Index")
    plt.ylabel("Värde")
    quicksort(lista, line1, fig)

def insertionsort(lista):
    global switcharoos
    x = np.linspace(0, len(lista), len(lista))
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    line1 = ax.bar(x,lista,color='blue')
    plt.title("Insertion sort")
    plt.xlabel("Index")
    plt.ylabel("Värde")

    for i in range(1, len(lista)):
        index = i
        for j in range(i-1, -1, -1):
            if lista[j+1] < lista[j]:
                lista[j],lista[j+1] = lista[j+1],lista[j]
                switcharoos += 1

                line1[j].set_height(lista[j])
                line1[j+1].set_height(lista[j+1])
                line1[j].set_color('red')
                line1[j+1].set_color('blue')
                fig.canvas.draw()
                fig.canvas.flush_events()
            else:
                break
            line1[j].set_color('blue')
        fig.canvas.draw()
        fig.canvas.flush_events()
    for i in range(len(lista)-1,0,-1):
        line1[i].set_color('green')
        fig.canvas.draw()
        fig.canvas.flush_events()
            

def selectionsort(lista):
    global switcharoos
    x = np.linspace(0,len(lista), len(lista))
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    line1 = ax.bar(x,lista, color='blue')
    #line2, = ax.plot(0,0, 'r*')
    plt.title("Selection sort")
    plt.xlabel("Index")
    plt.ylabel("Värde")
    for i in range(len(lista)-1,0,-1):
        # Hitta största talet av de som är kvar:
        maximum = i
        for j in range(i):
            if j > 0 and j-1 != maximum:
                line1[j-1].set_color('blue')
            line1[j].set_color('orange')
            fig.canvas.draw()
            fig.canvas.flush_events()
            if lista[j] > lista[maximum]:

                line1[maximum].set_color('blue')
                
                maximum = j

                line1[maximum].set_color('red')
                fig.canvas.draw()
                fig.canvas.flush_events()
        # Byt plats
        lista[i], lista[maximum] = lista[maximum], lista[i]
        
        switcharoos += 1
        line1[i].set_height(lista[i])
        #line1[i].set_color('orange')
        line1[maximum].set_height(lista[maximum])
        line1[maximum].set_color('red')
        """
        line1.set_ydata(lista)
        line2.set_xdata([i, minimum])
        line2.set_ydata([lista[i],lista[minimum]])
        """
        fig.canvas.draw()
        fig.canvas.flush_events()
        line1[maximum].set_color('blue')
        line1[i].set_color('green')
    fig.canvas.draw()
    fig.canvas.flush_events()
        
def bubblesort(lista):
    global switcharoos
    x = np.linspace(0,len(lista), len(lista))
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    line1 = ax.bar(x,lista, color='blue' )
    #line2 = ax.bar([0], [0], color='r')
    plt.title("Bubble sort")
    plt.xlabel("Index")
    plt.ylabel("Värde")
    # Bubble sort
    for i in range(len(lista)):
        for j in range(1,len(lista)-i):
            # Jämför
            if lista[j] < lista[j-1]:
                # Här sker bytet
                lista[j], lista[j-1] = lista[j-1], lista[j]
                switcharoos += 1
                line1[j].set_height(lista[j])
                line1[j-1].set_height(lista[j-1])
                line1[j].set_color('red')
                line1[j-1].set_color('blue')
                """
                line1.set_ydata(lista)
                line2.set_xdata([j])
                line2.set_ydata([lista[j]])
                """
                fig.canvas.draw()
                fig.canvas.flush_events()
                line1[j].set_color('blue')
                line1[j-1].set_color('blue')
        line1[j].set_color('green')
    line1[0].set_color('green')
    fig.canvas.draw()
    fig.canvas.flush_events()

quicktime = """
import random
lista = [random.randint(1,100) for x in range(1000)]

def time_quicksort(lista):
    # Välj ett pivot-element
    pivot = len(lista)-1
    counter = 0
    if pivot >= 0:
        for i in range(len(lista)-1):
            # Om talet är mindre än pivot-talet flytta det
            if lista[i] <= lista[pivot]:
                if i != counter:
                    lista[i], lista[counter] = lista[counter], lista[i]
                counter+=1
        # Flytta pivot
        lista[pivot], lista[counter] = lista[counter],lista[pivot]
        #Nu är pivot-talet på rätt plats.
        # Nu delar vi upp listan i två, den före pivot och den efter pivot
    if len(lista) > 1:
        lista[:counter] = time_quicksort(lista[:counter])
        lista[counter+1:] = time_quicksort(lista[counter+1:])
    
    return lista
"""
selectiontime = """
import random
lista = [random.randint(1,100) for x in range(1000)]
def time_selectionsort(lista):
    for i in range(len(lista)-1,0,-1):
        # Hitta största talet av de som är kvar:
        maximum = i
        for j in range(i):
            if lista[j] > lista[maximum]:
                maximum = j
        # Byt plats
        lista[i], lista[maximum] = lista[maximum], lista[i]
"""
insertiontime = """
import random
lista = [random.randint(1,100) for x in range(1000)]
def time_insertionsort(lista):
    for i in range(1, len(lista)):
        index = i
        for j in range(i-1, -1, -1):
            if lista[j+1] < lista[j]:
                lista[j],lista[j+1] = lista[j+1],lista[j]
            else:
                break
"""
bubbletime = """
import random
lista = [random.randint(1,100) for x in range(1000)]
def time_bubblesort(lista):
    for i in range(len(lista)):
        for j in range(1,len(lista)-i):
            # Jämför
            if lista[j] < lista[j-1]:
                # Här sker bytet
                lista[j], lista[j-1] = lista[j-1], lista[j]
"""

switcharoos = 0
lista = []
for i in range(50):
    lista.append(random.randint(0,100))

lista1 = lista.copy()
lista2 = lista.copy()
lista3 = lista.copy()
lista4 = lista.copy()
times = 1
print("Bubblesort:   ",timeit.timeit(setup = bubbletime, stmt = "time_bubblesort(lista)", number=times))
print("Selectionsort:",timeit.timeit(setup = selectiontime, stmt = "time_selectionsort(lista)", number=times))
print("Insertionsort:",timeit.timeit(setup = insertiontime, stmt = "time_insertionsort(lista)", number=times))
print("Quicksort:    ",timeit.timeit(setup = quicktime, stmt = "time_quicksort(lista)", number=times))


#bubblesort(lista1)
#selectionsort(lista2)
quickwrap(lista3)
insertionsort(lista4)



