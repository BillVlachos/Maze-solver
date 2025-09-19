import random
import time
import tkinter as tk
import winsound

def create_maze(w=20,h=15):
    cell = 'c'
    wall = 'w'
    unvisited = 'u'
    width=w
    height=h
    def ftiakse_maze(width, height):
        maze=[]
        for i in range(0, height):
            line = ['u' for j in range(0,width) ]
            maze.append(line)
        return maze


    def surroundingCells(rand_wall):
            s_cells = 0
            if (maze[rand_wall[0]-1][rand_wall[1]] == 'c'):
                    s_cells += 1
            if (maze[rand_wall[0]+1][rand_wall[1]] == 'c'):
                    s_cells += 1
            if (maze[rand_wall[0]][rand_wall[1]-1] == 'c'):
                    s_cells +=1
            if (maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
                    s_cells += 1

            return s_cells


    def create_entr_exit(width,height):
        for i in range(0, width):
                if (maze[1][i] == 'c'):
                        maze[0][i] = 'e'
                        break

        for i in range(width-1, 0, -1):
                if (maze[height-2][i] == 'c'):
                        maze[height-1][i] = 'x'
                        break
    maze = ftiakse_maze(width,height)

    #Rikse kerma
    start_height = random.randint(1,height-2)
    start_width = random.randint(1,height-2)

    maze[start_height][start_width]=cell
    walls=[]
    walls.append([start_height-1, start_width])
    walls.append([start_height, start_width-1])
    walls.append([start_height, start_width+1])
    walls.append([start_height+1, start_width])

    maze[start_height-1][start_width] = wall
    maze[start_height][start_width-1] = wall
    maze[start_height][start_width+1] = wall
    maze[start_height+1][start_width] = wall


    def create_walls(width,height):
        while (walls):
                #Rikse kerma
                rand_wall = walls[int(random.random()*len(walls))-1]

                #Koita to areistero cell
                if (rand_wall[1] != 0):
                        if (maze[rand_wall[0]][rand_wall[1]-1] == 'u' and maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
                                #Vres ta gurw cells
                                s_cells = surroundingCells(rand_wall)

                                if (s_cells < 2):
                                        #Kane dromo
                                        maze[rand_wall[0]][rand_wall[1]] = 'c'

                                        #Markare ta kainourgia cells
                                        
                                        if (rand_wall[0] != 0):
                                                if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                                                        maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                                                if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                                                        walls.append([rand_wall[0]-1, rand_wall[1]])


                                        
                                        if (rand_wall[0] != height-1):
                                                if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
                                                        maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                                                if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                                                        walls.append([rand_wall[0]+1, rand_wall[1]])

                                        
                                        if (rand_wall[1] != 0):	
                                                if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
                                                        maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                                                if ([rand_wall[0], rand_wall[1]-1] not in walls):
                                                        walls.append([rand_wall[0], rand_wall[1]-1])
                                

                                #Diegrapse to toixo
                                for wall in walls:
                                        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                                                walls.remove(wall)

                                continue

                #Koita panw cell
                if (rand_wall[0] != 0):
                        if (maze[rand_wall[0]-1][rand_wall[1]] == 'u' and maze[rand_wall[0]+1][rand_wall[1]] == 'c'):

                                s_cells = surroundingCells(rand_wall)
                                if (s_cells < 2):
                                        
                                        maze[rand_wall[0]][rand_wall[1]] = 'c'

                                        
                                        
                                        if (rand_wall[0] != 0):
                                                if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                                                        maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                                                if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                                                        walls.append([rand_wall[0]-1, rand_wall[1]])

                                        
                                        if (rand_wall[1] != 0):
                                                if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
                                                        maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                                                if ([rand_wall[0], rand_wall[1]-1] not in walls):
                                                        walls.append([rand_wall[0], rand_wall[1]-1])

                                        
                                        if (rand_wall[1] != width-1):
                                                if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
                                                        maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                                                if ([rand_wall[0], rand_wall[1]+1] not in walls):
                                                        walls.append([rand_wall[0], rand_wall[1]+1])

                                
                                for wall in walls:
                                        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                                                walls.remove(wall)

                                continue

                #Koita katw cell
                if (rand_wall[0] != height-1):
                        if (maze[rand_wall[0]+1][rand_wall[1]] == 'u' and maze[rand_wall[0]-1][rand_wall[1]] == 'c'):

                                s_cells = surroundingCells(rand_wall)
                                if (s_cells < 2):
                                        
                                        maze[rand_wall[0]][rand_wall[1]] = 'c'

                                        
                                        if (rand_wall[0] != height-1):
                                                if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
                                                        maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                                                if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                                                        walls.append([rand_wall[0]+1, rand_wall[1]])
                                        if (rand_wall[1] != 0):
                                                if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
                                                        maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                                                if ([rand_wall[0], rand_wall[1]-1] not in walls):
                                                        walls.append([rand_wall[0], rand_wall[1]-1])
                                        if (rand_wall[1] != width-1):
                                                if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
                                                        maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                                                if ([rand_wall[0], rand_wall[1]+1] not in walls):
                                                        walls.append([rand_wall[0], rand_wall[1]+1])

                                
                                for wall in walls:
                                        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                                                walls.remove(wall)


                                continue

                #Koita deksi cell
                if (rand_wall[1] != width-1):
                        if (maze[rand_wall[0]][rand_wall[1]+1] == 'u' and maze[rand_wall[0]][rand_wall[1]-1] == 'c'):

                                s_cells = surroundingCells(rand_wall)
                                if (s_cells < 2):
                                        
                                        maze[rand_wall[0]][rand_wall[1]] = 'c'

                                        
                                        if (rand_wall[1] != width-1):
                                                if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
                                                        maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                                                if ([rand_wall[0], rand_wall[1]+1] not in walls):
                                                        walls.append([rand_wall[0], rand_wall[1]+1])
                                        if (rand_wall[0] != height-1):
                                                if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
                                                        maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                                                if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                                                        walls.append([rand_wall[0]+1, rand_wall[1]])
                                        if (rand_wall[0] != 0):	
                                                if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                                                        maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                                                if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                                                        walls.append([rand_wall[0]-1, rand_wall[1]])

                                
                                for wall in walls:
                                        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                                                walls.remove(wall)

                                continue

                
                for wall in walls:
                        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                                walls.remove(wall)
        #Kane walls osa emeinan unvisited
        for i in range(0, height):
            for j in range(0,width):
                if(maze[i][j] == 'u'):
                    maze[i][j] = 'w'

    create_walls(width,height)
    create_entr_exit(width,height)
    return maze

def path_finder(maze):
    #path finding algorithm
    #συντεταγμενες εισοδου-εξοδου

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] =='e':
                x_e=i
                y_e=j
            if maze[i][j] == 'x':
                x_x=i
                y_x=j
    start=[x_e,y_e]
    end=[x_x,y_x]


    ##δημιουργεια πίνακα για την ανάθεση τιμών σε κάθε πιθανή θέση

    m = []
    for i in range(len(maze)):
        m.append([])
        for j in range(len(maze[i])):
            m[-1].append(0)
    i,j = start
    m[i][j] = 1


    #Αρίθμηση αξίας κάθε βήματος

    def step_value(k):
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] == k:
                    if i>0 and m[i-1][j] == 0 and not maze[i-1][j]=='w':
                        m[i-1][j] = k + 1
                    if j>0 and m[i][j-1] == 0 and not maze[i][j-1]=='w': 
                        m[i][j-1] = k + 1
                    if i<len(m)-1 and m[i+1][j] == 0 and not maze[i+1][j]=='w': 
                        m[i+1][j] = k + 1
                    if j<len(m[i])-1 and m[i][j+1] == 0 and not maze[i][j+1]=='w': 
                        m[i][j+1] = k + 1

    k = 0
    count = 0
    while m[end[0]][end[1]] == 0 and count <= 300:
        k += 1
        count += 1
        step_value(k)
    
    


    ##Εύρεση Διαδρομής
    else:
        i, j = end
        k = m[i][j]
        the_path = [(i,j)]
        while k > 1:
            if i > 0 and m[i - 1][j] == k-1:
                i, j = i-1, j
                the_path.append((i, j))
                k-=1
            elif j > 0 and m[i][j - 1] == k-1:
                i, j = i, j-1
                the_path.append((i, j))
                k-=1
            elif i < len(m) - 1 and m[i + 1][j] == k-1:
                i, j = i+1, j
                the_path.append((i, j))
                k-=1
            elif j < len(m[i]) - 1 and m[i][j + 1] == k-1:
                i, j = i, j+1
                the_path.append((i, j))
                k -= 1
        the_patch=the_path.reverse()
        return the_path

def random_generated():
    winsound.PlaySound('start', winsound.SND_FILENAME)
    new_root=tk.Toplevel()
    canvas = tk.Canvas(new_root, bg='black')
    canvas.pack(anchor=tk.CENTER, expand=True)
    backround_image = tk.PhotoImage(file='space_webp.png')
    canvas.create_image((0,0),anchor='nw',image=backround_image)
    maze=create_maze()
    the_path=path_finder(maze)
    obstacle_image = tk.PhotoImage(file='obstacle.png')
    sprite_image = tk.PhotoImage(file='ufo.png')
    
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j]=='w':
                x=i
                y=j
                tk.Label(canvas,image=obstacle_image,highlightthickness = 0,borderwidth=0).grid(row=x,column=y)
            if maze[i][j]=='e':
                sprite_test=tk.Label(canvas,image=sprite_image,highlightthickness = 0,borderwidth=0)
                sprite_test.grid(row=i,column=j)
                sprite=sprite_test
    for i in range(len(the_path)):
        x=the_path[i][0]
        y=the_path[i][1]
        
        sprite.grid_forget()
        sprite.grid(row=x,column=y)
        new_root.update()
        winsound.PlaySound('short_beep_v2', winsound.SND_FILENAME)
        time.sleep(0.3)

    winsound.PlaySound('ufo_landing', winsound.SND_FILENAME)
    new_root.destroy()
   
                


def user_generated():
    def clicked(event):
        x = event.x_root - f.winfo_rootx()
        y = event.y_root - f.winfo_rooty() 

        z=f.grid_location(x,y)
        if z[1]!=15:
            if z[0]==1 and z[1]==0:
                pass
            elif z[0]==18 and z[1]==14:
                pass
            else:
                x1=z[0]
                y1=z[1]
                maze_i[y1][x1]='c'
                event.widget['bg']='black'

    def clicked1(event):
        x = event.x_root - f.winfo_rootx()
        y = event.y_root - f.winfo_rooty()

        z=f.grid_location(x,y)
        if z[1]!=15:
            if z[0]==1 and z[1]==0:
                pass
            elif z[0]==18 and z[1]==14:
                pass
            else:
                x1=z[0]
                y1=z[1]
                maze_i[y1][x1]='w'
                event.widget['bg']='white'
            


    def finished():
        new_window.destroy()
        maze=maze_i
        the_path=path_finder(maze)
        if len(the_path)<20:
            new_root=tk.Toplevel()
            l=tk.Label(new_root,text='No path found',font='Arial 25',bg='#2D033B',fg='#E5B8F4').pack()
            new_root.mainloop()
            #time.sleep(3)
            #new_root.destroy()
        else:
            new_root=tk.Toplevel()
            canvas = tk.Canvas(new_root, bg='black')
            canvas.pack(anchor=tk.CENTER, expand=True)
            backround_image = tk.PhotoImage(file='space_webp.png')
            canvas.create_image((0,0),anchor='nw',image=backround_image)
            
            obstacle_image = tk.PhotoImage(file='obstacle.png')
            sprite_image = tk.PhotoImage(file='ufo.png')
            
            winsound.PlaySound('start', winsound.SND_FILENAME)
            
            
            for i in range(len(maze)):
                for j in range(len(maze[i])):
                    if maze[i][j]=='w':
                        x=i
                        y=j
                        tk.Label(canvas,image=obstacle_image,highlightthickness = 0,borderwidth=0).grid(row=x,column=y)
                    if maze[i][j]=='e':
                        sprite_test=tk.Label(canvas,image=sprite_image,highlightthickness = 0,borderwidth=0)
                        sprite_test.grid(row=i,column=j)
                        sprite=sprite_test
            time.sleep(3)
            new_root.update()
            for i in range(len(the_path)):
                x=the_path[i][0]
                y=the_path[i][1]
                
                sprite.grid_forget()
                sprite.grid(row=x,column=y)
                new_root.update()
                winsound.PlaySound('short_beep_v2', winsound.SND_FILENAME)
                time.sleep(0.3)

            winsound.PlaySound('ufo_landing', winsound.SND_FILENAME)
            new_root.destroy()

        
    

    maze_i=[]
    for i in range(0,15):
        line_i=['w' for i in range(0,20)]
        maze_i.append(line_i)
    
    maze_i[0][1]='e'
    maze_i[14][18]='x'
  
    
        
            
    new_window=tk.Toplevel()
    new_window.geometry('1030x750')
    f=tk.Frame(new_window,bg='black')
    f.pack()
    for i in range(0,15):
        for j in range(0,20):
            if i==0 and j==1:
                tk.Label(f,text='e',font='Arial 10',bg='green').grid(row=i,column=j,ipadx=18,ipady=12)
            elif i==14 and j==18:
                tk.Label(f,text='x',font='Arial 10',bg='red').grid(row=i,column=j,ipadx=18,ipady=12)
            else:
                tk.Button(f).grid(row=i,column=j,ipadx=20,ipady=10)

    finish_b=tk.Button(f,text='finished',font='Arial 20',bg='#2D033B',fg='#E5B8F4',command=finished).grid(row=15,column=9,columnspan=3)
    
            

    new_window.bind('<Button-1>',clicked)
    new_window.bind('<Button-3>',clicked1)
        
    
    new_window.mainloop()

   
#Dhmiourgia canva

root = tk.Tk()
screen_width = root.winfo_screenwidth()  
screen_height = root.winfo_screenheight() 

x = (screen_width/2) - (500)
y = (screen_height/2) - (300)
 
root.geometry('%dx%d+%d+%d' % (1000, 600, x, y))
root.title('Self Driving Virtual Vehicle Using Python')
canvas = tk.Canvas(root, width=1000, height=600)
root.resizable(False, False)
frame = tk.Frame(root, relief='raised', borderwidth=2)
canvas.pack()

#bg_img
background_image = tk.PhotoImage(file='bgimg.png')
canvas.create_image((0,0),anchor='nw',image=background_image)

#btn1
button1=tk.Button(root,text='RANDOM GENERATED COURSE',
                               font='Arial 10 bold',
                               bg='deep pink',fg='black', activebackground = "#33B5E5", command=random_generated)
button1_window=canvas.create_window(400,300,width=220, height=40,anchor='nw', window=button1)

#btn2
button2=tk.Button(root,text='USER GENERATED COURSE',font='Arial 10 bold',
                  bg='deep pink',fg='black', activebackground = "#33B5E5",
                  command=user_generated)
button2_window=canvas.create_window(400,340, width=220, height=40,anchor='nw', window=button2)

'''#btn3
def music():
    winsound.PlaySound('bg_music', winsound.SND_FILENAME)
    
button3=tk.Button(root, text='MUSIC', font='Arial 10 bold',
                  bg='deep pink', fg='black', activebackground='#33B5E5', command=music)
button3_window=canvas.create_window(400,380, width=220, height=40,anchor='nw', window=button3)'''

#btn4
button4=tk.Button(root,text='ΕΧΙΤ',font='Arial 10 bold',
                  bg='deep pink',fg='black',activebackground = "#33B5E5",
                  command=root.destroy)
button4_window=canvas.create_window(400,380, width=220, height=40,anchor='nw', window=button4)

root.mainloop()













