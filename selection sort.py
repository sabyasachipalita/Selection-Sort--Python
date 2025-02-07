def selection_sort(a):
        n=len(a)
        for i in range(n-1):
                min=i
                for j in range(i+1,n):
                        if a[j]<=a[min]:
                                min=j
                                a[i],a[min]=a[min],a[i]
        return a
a=[2,1,4,3]
print(selection_sort(a))            






                     
                                






                      




        
      




















               


        


                


   
        


                        

                        
                                              

