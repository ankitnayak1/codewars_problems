'''
Your goal in this kata is to implement a difference function, 
which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b 
keeping their order.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from 
the other:

array_diff([1,2,2,2,3],[2]) == [1,3]
'''

def lst_dif(list1, list2):
    a = []
    b = []
    if (len(list1) > len(list2)):
        for i in range(len(list1)):
            for j in range(len(list2)):
                if (list1[i]!=list2[j]):
                    a.append(list1[i])
        print("New list =",a)
            
    if (len(list1) < len(list2)):
        for i in range(len(list2)):
            for j in range(len(list1)):
                if (list2[i]!=list1[j]):
                    b.append(list2[i])
        print("New list =",b)
        
list1 = [1,2,2,2,3]
list2 = [2]
lst_dif(list1,list2)