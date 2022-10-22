
import pygame ,sys ,random,time
from pygame.locals import *

#initializing the pygame window

pygame.init()
win=pygame.display.set_mode((1000,1000))
pygame.display.set_caption('')
win.fill("WHITE")
#pygame.mixer.music.load('AlanWalker1.mp3')
#pygame.mixer.music.play(-1,0.0)

rightLock=True
leftLock=False
upLock=False
downLock=False

#define all variables here
snakeList=[]
moveTrack=[]
listx=[a for a in range(20,481,20)]
listy=[a for  a in range(20,481,20)]
fps=10
score=0
#define all pygame related extra objects here
clock=pygame.time.Clock()
font3=pygame.font.SysFont('comicsans',25,True)
text3=font3.render('YOU CRASHED  GAME OVER',True,"BLACK")
#define all functions here
def gridredraw():
    for row in range(0,501,20):
        pygame.draw.line(win,"RED",(row,0),(row,500))
    for col in range(0,501,20):
        pygame.draw.line(win,"RED",(0,col),(500,col))
        
def displayUpdater():
    win.fill("WHITE")
    gridredraw()

    pygame.display.update() 
    clock.tick(fps)

def screenPasser():
    if snakeHead.Rect[0]<0:
        snakeHead.Rect[0]=500
    if snakeHead.Rect[0]>500:
        snakeHead.Rect[0]=0
    if snakeHead.Rect[1]>500:
        snakeHead.Rect[1]=0
    if snakeHead.Rect[1]<-10:
        snakeHead.Rect[1]=500

def foodGiver():
       global c,d
       c=random.choice(listx)
       d=random.choice(listy)
       pygame.draw.rect(win,"FUCHSIA",(c,d,20,20))
       pygame.display.update()
foodGiver()
def snakeAdder():
    if Sleft:
      snakeList.append(snake(moveTrack[-1][0]+20,moveTrack[-1][1]))
      moveTrack.append((moveTrack[-1][0]+20,moveTrack[-1][1]))
    elif Sright:
        snakeList.append(snake(moveTrack[-1][0]-20,moveTrack[-1][1]))
        moveTrack.append((moveTrack[-1][0]-20,moveTrack[-1][1]))
    elif Sup:
        snakeList.append(snake(moveTrack[-1][0],moveTrack[-1][1]+20))
        moveTrack.append((moveTrack[-1][0],moveTrack[-1][1]+20))
    elif Sdown:
        snakeList.append(snake(moveTrack[-1][0],moveTrack[-1][1]-20))
        moveTrack.append((moveTrack[-1][0],moveTrack[-1][1]+20))
def crashChecker():
    for i in moveTrack[1:]:
        if (snakeHead.Rect[0],snakeHead.Rect[1])==i:
            win.blit(text3,(600,600))
            pygame.display.update()
            time.sleep(5)
            pygame.quit()
            sys.exit()
def scoreDisplayer():
    font2=pygame.font.SysFont('comicsans',30,False,True)
    text2=font2.render('score='+str(score),True,"BLACK")
    win.blit(text2,(600,30))
    pygame.display.update()

#define all classes here
class snake:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.width=20
        self.height=20
        self.color="BLUE"
        self.vel=20
        self.Rect=[self.x,self.y,self.width,self.height]
    
    def snakeMover(self):
        #only changes the co_ordinates of the snake head
 
            if Sleft and not leftLock:#and (self.Rect[1]/10)%2==0:
                screenPasser()
                self.Rect[0]-=self.vel
                crashChecker()
                print('at left')
                print((self.Rect[0],self.Rect[1]))
            
            elif Sright and not rightLock:#and (self.Rect[1]/10)%2==0:
                 screenPasser()
                 self.Rect[0]+=self.vel          
                 crashChecker()
                 print('at right')
                 print((self.Rect[0],self.Rect[1]))
             
            elif Sup and not upLock:#and (self.Rect[0]/10)%2==0:
                screenPasser()
                self.Rect[1]-=self.vel
                crashChecker()
                print('at up')
                print((self.Rect[0],self.Rect[1]))
                
            elif Sdown and not downLock:#and (self.Rect[0]/10)%2==0:
                screenPasser()
                self.Rect[1]+=self.vel  
                crashChecker()
                print('at down')
                print((self.Rect[0],self.Rect[1]))
            print((Sup,upLock),(Sdown,downLock))
            global moveTrack,score
            if self.Rect[0]==c and self.Rect[1]==d:
                 foodGiver()
                 snakeAdder()
                 score+=1
                
 
            for i in moveTrack:
               if i[0]==c and i[1]==d:
                 foodGiver()
                 snakeAdder()
                 score+=1
          
 
          
            a=moveTrack[:-1]
            b=[]
            b.append((self.Rect[0],self.Rect[1]))
            b.extend(a)
            moveTrack=b
            print('moveTrack is',moveTrack)
            snakeHead.snakeDrawer()
            
            
    def snakeDrawer(self):
        for i in range(len(moveTrack)):
            pygame.draw.rect(win,"BLUE",(moveTrack[i][0],moveTrack[i][1],self.width,self.height))
        pygame.draw.rect(win,"FUCHSIA",(c,d,20,20))
        global score
        int(score)
        scoreDisplayer()
        pygame.display.update()
        win.fill("WHITE")
        #gridredraw()
        pygame.draw.line(win,"BLACK",(540,0),(540,1000))

        #time.sleep(0.2)
    
print('c and d are',c,d)
#mainloop
i=1
while True:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    #initializing the snake head shound run only during the first loop
    if i==1:
        moveTrack.append((260,20))
        moveTrack.append((280,20))
        snakeHead=snake(260,20)
        snakeList.append(snakeHead)
        Sleft=True
        Sright=False
        Sup=False
        Sdown=False
        snakeList.append(snake(280,20))

    #should capture each key moves and if the condition is True should send to the moving and drawing functions    
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if leftLock:
            #Sright=True
            #rightLock=False
            pass
        elif not leftLock:
            Sleft=True
            Sright=False
            Sup=False
            Sdown=False
            rightLock=True
            upLock=False
            downLock=False
    
        #send the call to sankeMover which changes the coordinartes of snake head
            snakeHead.snakeMover()

        
        
    if keys[pygame.K_RIGHT]:
        if rightLock:
          #  Sleft=True
          #  leftLock=False
          pass
        elif not rightLock:
            Sleft=False
            Sright=True
            Sup=False
            Sdown=False
            leftLock=True
            upLock=False
            downLock=False
            snakeHead.snakeMover()
    
  
    if keys[pygame.K_UP]:
        if upLock:
            pass
            #Sdown=True
           # downLock=False
        elif not upLock:
            Sleft=False
            Sright=False
            Sup=True
            Sdown=False
            downLock=True
            rightLock=False
            leftLock=False
   
        
            snakeHead.snakeMover()
  

    if keys[pygame.K_DOWN]:
        if downLock:
            pass
           # Sup=True
           # upLock=False
        elif not downLock:
            Sleft=False
            Sright=False
            Sup=False
            Sdown=True
            upLock=True
            rightLock=False
            leftLock=False

            snakeHead.snakeMover()

    snakeHead.snakeMover()
 #   displayUpdater()

    
    i+=1
    
          
            