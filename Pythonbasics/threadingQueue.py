import threading
import time
import queue

#Multithreaded Priority Queue

class  ThreadQueueClass(threading.Thread):
        
    def __init__(self, threadID,name,que):
        threading.Thread.__init__(self)
        self.threadID=threadID,
        self.name=name,
        self.que=que
   
    def run(self):
        print("Thread Starting %s:" % self.name)
        process_queue(self.name,self.que)
        print("Thread Completed %s:" % self.name)    

exitFlag=0            
    
def process_queue(threadName,que):
   
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data=que.get()
            queueLock.release()
            print("%s Processing %s"% (threadName,data))
        else:
            queueLock.release()
        time.sleep(1)

threadList=['Thread1','Thread2','Thread3']
nameList=['one','two','three','four','five']
queueLock= threading.Lock()
threads=[]
threadId=1
workQueue=queue.Queue(10)
 
 
# Create New Threads
for th in threadList:
    thread=ThreadQueueClass(threadId,th,workQueue)
    thread.start()
    threads.append(thread)  
    threadId+=1
    
#fill the Queue
queueLock.acquire()
for que in nameList:
    workQueue.put(que)
queueLock.release()

#wait for the queue to empty
while not workQueue.empty():
    pass

#notify threads  its time to exit
exitflag=1

# wait for all thread to complete
for t in threads:
    t.join()
    
print("Exiting Main Thread")



    