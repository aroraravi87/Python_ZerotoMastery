import threading
import time

#Synchronizing Threads
#Multithreaded Priority Queue

class  ThreadClass(threading.Thread):
    
    
    def __init__(self, threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID,
        self.name=name,
        self.counter=counter
   
    def run(self):
        print("Thread Starting %s:" % self.name)
        threadLock.acquire()
        print_time(self.name,self.counter,self.counter)
        threadLock.release()
        print("Thread Completed %s:" % self.name)    
            
    
def print_time(threadName,delay,counter):
    count=0
    while count<counter:
        time.sleep(delay)
        count+=1
        print("Thread %s: and time %s:"% (threadName,time.ctime(time.time()))) 

threadLock= threading.Lock()
threads=[]
  

threadObj1=ThreadClass(1,"Thread-1",1)
threadObj2=ThreadClass(2,"Thread-2",2)
threadObj3=ThreadClass(3,"Thread-3",3)
threadObj4=ThreadClass(4,"Thread-4",4)
    
#threadObj2=ThreadClass(target=print_time,args=(2,2))

threadObj1.start()
threadObj2.start()
threadObj3.start()
threadObj4.start()

threads.append(threadObj1)
threads.append(threadObj2)
threads.append(threadObj3)
threads.append(threadObj4)

for th in threads:
    th.join()



print("Exiting Main Thread")



    