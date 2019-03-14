

def my_sort():
    d = {'even': [], 'odd' : [],'chars': []}
    
    list_sort = [2,0,6,5,1,7,'z','a']
    for i in list_sort:
        if isinstance(i,str):
                d['chars'].append(i)
        elif isinstance(i,int):
                if i % 2 !=0:
                        d['odd'].append(i)
                elif i % 2 == 0:
                        d['even'].append(i)
    print(d)  
my_sort()
   
       