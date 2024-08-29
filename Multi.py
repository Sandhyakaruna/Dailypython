import threading
import time

# Define a function for each task
def task1():
    for i in range(5):
        print("Task 1 is running")
        time.sleep(1)

def task2():
    for i in range(5):
        print("Task 2 is running")
        time.sleep(1)

# Create threads for each task
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both tasks are completed")
