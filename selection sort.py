# def selection_sort(a):
#             n=len(a)
#             for i in range(n-1):
#                     min=i
#                     for j in range(i+1,n):
#                             if a[j]<=a[min]:
#                                     min=j
#                     a[i],a[min]=a[min],a[i]                
                                    
#             return a                        
# a=[2,1,4,3]

# selection_sort(a)
# print("the soretd array is  that",a)





#selections sort


# def selection_sort(a):
#         n=len(a)
#         for i in range(n-1):
#                 min=i
#                 for j in range(i+1,n):
                        
#                         if a[j]<=a[min]:
#                                 min=j
#                 a[i],a[min]=a[min],a[i] 
#         return a
# a=[2,1,4,3]
# selection_sort(a)
# print("the sorted array is",a)                       
                                


# s="sabya"
# d=s[0:3:2]
# print(d)  
# 
# def insertion_sort(a):
#         n=len(a)
#         for j in range(n):
#                 key=a[j]
#                 i=j-1
#                 while i>=0 and a[i]>key:
#                         a[i+1]=a[i]
#                         i-=1
#                         a[i+1]=key
#         return a
# a=[2,1,4,3,6,5]
# print(insertion_sort(a))   
# 
# 
# def bubble_sort(a):
#             n=len(a)
#             for i in range(n):
#                     swaped=True
#                     for j in range(0,n-i-1):
#                             if a[j]>=a[j+1]:
#                                     a[j],a[j+1]=a[j+1],a[j]
#                                     swaped=True
#                     if not swaped:
#                             break
# a=[2,1,4,3]
# bubble_sort(a)
# print("the sorted array is that",a)


#selection sort
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




        
#lcs problem
# a="sabya"
# b="sachi"

# def  lcs(i,j):
#         if(i==0) or (j==0):
#                 return 0
#         elif(a[i-1]==b[j-1]):
#                 return 1+lcs(i-1,j-1)
#         else:
#                 return max  (lcs(i,j-1),lcs(i-1,j))
        
# # print(lcs(len(a),len(b)))        


# #quick sort in python
# def partition(a,low,high):
#         if len(a)<=1:
#                 return a
#         pivot=a[low]
#         i=low+1
#         j=high
#         while True:
#                 while i<=j and a[i]<=pivot:
#                         i+=1
#                 while i<=j and a[j]>pivot:
#                         j-=1
#                 if i<=j:
#                         a[i],a[j]=a[j],a[i]
#                 else:
#                         break
#         a[low],a[j]=a[j],a[low]
#         return j

# def quick_sort(a,low,high):
#         if (low<=high):
#                 piv=partition(a,low,high)
#                 quick_sort(a,low,piv-1)
#                 quick_sort(a,piv+1,high)

# a=[2,1,4,3]
# print("the array is",a)
# quick_sort(a,0,len(a)-1)
# print("the sorted array is",a)




#linear serch in python
# def linear_serch(list,n,key):
#         for i in range(0,n):
#                 if list[i]==key:
#                         return i
#         return -1


# list=[1,2,3,4]
# key=4
# n=len(list)
# s=linear_serch(list,n,key)
# if s==-1:
#         print("elements is not ")
# else:
#         print("elements is presentat index",s)
# 
# # 
# list=[1,2,3,4]
# print("before reverse the list is",list)
# list.reverse()
# print("after the reverse the list is",list)
# clone the list 
# list=[1,2,3,4]
# list1=[]
# list1.extend(list)
# print(list1)
list=[1,2,3]
list1=list[::]
print(list1)



# print("the list before ",list)
# list.reverse()
# print("the list after the list",list)

# list1=[]
# list1.extend(list)
# print(list1)




# name="sabya"
# for char in(name):
#         print(char.upper())



# merge_sort in python

def merge_sort(arr):
        if len(arr)<=1:
                return a
        mid=len(arr)//2 
        left_arr=arr[:mid]
        right_arr=arr[mid:]
        left_arr=merge_sort(left_arr)
        right_arr=merge_sort(right_arr) 
        return merge(left_arr,right_arr)

def merge(left_arr,right_arr):
        i=0
        j=0
        result=[]
        while i<len(left_arr) and j<len(right_arr):
                if left_arr[i]<=right_arr[j]:
                        result.append(left_arr[i])
                        i+=1
                else:
                        result.append(right_arr[j])
                        j+=1
        result+=left_arr[i:]
        result+=right_arr[j:]
        return result

arr=[2,1,5,3,4]
sorted=merge_sort(arr)
print(sorted)


               


        


                


   
        


                        

                        
                                              

