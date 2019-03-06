def my_sort():
    d = {'even': [], 'odd' : [], 'chars': []}
    list_sort =[2,0,6,5,1,7,'z','a' ]
    for i in list_sort:
        if i is chr:
                d['chars'].append(i)
        elif i % 2 !=0:
                d['odd'].append(i)  
        else:
                d['even'].append(i)
        print(d) 
        
my_sort()
   
       