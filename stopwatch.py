from tkinter import *
import tkinter.messagebox as tkMessageBox
import time
def Main():
    global root
    
    root = Tk()
    root.title("StopWatch")
    width = 600
    height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Top = Frame(root, width=600)
    Top.pack(side=TOP)
    stopWatch = StopWatch(root)
    stopWatch.pack(side=TOP)
    Bottom = Frame(root, width=600)
    Bottom.pack(side=BOTTOM)
    Start =  Button(Bottom, text='Start', command=stopWatch.Start, width=10, height=2)
    Start.pack(side=LEFT)
    Lap =  Button(Bottom, text='Lap', command=stopWatch.Lap, width=10, height=2)
    Lap.pack(side=LEFT)
    Stop = Button(Bottom, text='Stop', command=stopWatch.Stop, width=10, height=2)
    Stop.pack(side=LEFT)
    Reset = Button(Bottom, text='Reset', command=stopWatch.Reset, width=10, height=2)
    Reset.pack(side=LEFT)
    Exit = Button(Bottom, text='Exit', command=stopWatch.Exit, width=10, height=2)
    Exit.pack(side=LEFT)
    Title = Label(Top, text="Stopwatch", font=("roboto", 20), fg="white", bg="black")
    Title.pack(fill=X)
    root.config(bg='white')
    root.mainloop() 
    

class StopWatch(Frame):  
                                                         
    def __init__(self, parent=None, **kw):        
        Frame.__init__(self, parent, kw)
        self.startTime = 0.0        
        self.nextTime = 0.0
        self.onRunning = 0
        self.timestr = StringVar()               
        self.MakeWidget()
        self.timestr1=[StringVar() for i in range(0,100)]
        self.i=0
    def MakeWidget(self):                         
        timeText = Label(self, textvariable=self.timestr, font=("times new roman", 50), fg="red", bg="blue")
        self.SetTime(self.nextTime)
        timeText.pack(fill=X, expand=NO, pady=2, padx=2)                      
    
    def Updater(self): 
        self.nextTime = time.time() - self.startTime
        self.SetTime(self.nextTime)
        self.timer = self.after(25, self.Updater)
    
    def SetTime(self, nextElap):
        minutes = int(nextElap/60)
        seconds = int(nextElap - minutes*60.0)
        miliSeconds = int((nextElap - minutes*60.0 - seconds)*100)                
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, miliSeconds))
        
    def Start(self):                                                     
        if not self.onRunning:            
            self.startTime = time.time() - self.nextTime
            self.Updater()
            self.onRunning = 1
    def Lap(self):
        x=self.nextTime
        minutes = int(x/60)
        seconds = int(x- minutes*60.0)
        miliSeconds = int((x - minutes*60.0 - seconds)*100)
        self.timestr1[self.i].set('%02d:%02d:%02d' % (minutes, seconds, miliSeconds))
        self.time1= Label(self, textvariable=self.timestr1[self.i], font=("times new roman", 20), fg="green", bg="white")
        self.time1.pack(fill=X, expand=NO, pady=2, padx=2)
        self.i+=1        
    def Stop(self):                                    
        if self.onRunning:
            self.after_cancel(self.timer)            
            self.nextTime = time.time() - self.startTime    
            self.SetTime(self.nextTime)
            self.onRunning = 0

    def Exit(self):
        result = tkMessageBox.askquestion('Time Stops', 'Are you sure you want to exit?', icon='warning')
        if result == 'yes':
            root.destroy()
            exit()
    
    def Reset(self):                                  
        self.startTime = time.time()         
        self.nextTime = 0.0
        self.time1= Label(self, text='Reset', font=("times new roman", 20), fg="Black", bg="black")
        self.time1.pack(fill=X, expand=NO, pady=2, padx=2)
        self.SetTime(self.nextTime)
        
        

if __name__ == '__main__':
    Main()
