names = [ "connor, rj, sara, kristen, stefanie, randell, emma, jessica, alex, katie" ]
len (names)
queue = [ ]

print ("\nInitial queue")
print (queue)

for x in names :
    print ('queues are first-in-first-out (fifo) data structures')
    print ('\nInitial queue. used queue.pop(0) to pop element in front')
    print (names)

for x in names :
    print ('\nElements dequeued from queue. used queue.pop(0) to pop element in front')
    print (names.pop(0))

print ('\nQueue after removing elements')
print (names)
