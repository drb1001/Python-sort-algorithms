import random as rand
import Bubblesort,Mergesort,Quicksort,Shellsort,Heapsort

a=[]
b=[1]
c=[1,2,3,4]
d=[5,4,3,2,1]
e=[5,5,1,5,5,1,5,5]
f=[1,4,7,2,6,9,0,76,3,6,1,6,2,5,3,1,1,2,6,2,8,6,3,1,8,54,1,2,3,9,8,7,1,3,2,4]
g=rand.sample( range(0,100) , 25 )
h=rand.sample( range(0,10000) , 1000 )
mylist=[a,b,c,d,e,f,g,h]


print "-------bubblesort------"
for eachlist in mylist:
    print eachlist if len(eachlist)<40 else "%s ..." %eachlist[:25]
    sorted_list = Bubblesort.bubblesort(eachlist)
    print sorted_list if len(eachlist)<40 else "%s ..." %sorted_list[:25]

print "-------mergesort------"
for eachlist in mylist:
    print eachlist if len(eachlist)<40 else "%s ..." %eachlist[:25]
    sorted_list =  Mergesort.mergesort(eachlist)
    print sorted_list if len(eachlist)<40 else "%s ..." %sorted_list[:25]

print "-------quicksort------"
for eachlist in mylist:
    print eachlist if len(eachlist)<40 else "%s ..." %eachlist[:25]
    sorted_list =  Quicksort.quicksort(eachlist)
    print sorted_list if len(eachlist)<40 else "%s ..." %sorted_list[:25]

print "-------shellsort------"
for eachlist in mylist:
    print eachlist if len(eachlist)<40 else "%s ..." %eachlist[:25]
    sorted_list =  Shellsort.shellsort(eachlist)
    print sorted_list if len(eachlist)<40 else "%s ..." %sorted_list[:25]
