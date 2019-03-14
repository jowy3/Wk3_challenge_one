def my_sort():
    d = {'even': [], 'odd' : [],'chars': { 'char' :[]}}
    
    list_sort = 'z','a',2,0,6,5,1,7
    for i in list_sort :
       if i is str:
               if  i % 2 !=0:
                d['odd'].append(i)
        else:         
                 
                d['even'].append(i)

                d['chars'].append(i)
    
    
    print()   
        
my_sort()
   
       