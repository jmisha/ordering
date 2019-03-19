def bubble_sort(items):
    
    '''
    Return array of items, sorted in ascending order using the bubble sort algorithm
    
    Args:
        items: list or array-like object of unordered values
        
    Returns
    array: in ascending order

    Examples:
        >>> bubble_sort([10, 1, 12, 9, 2])
        [1, 2, 9, 10, 12]
        
        >>> bubble_sort(['dolphin', 'walrus', 'elephant', 'zebra', 'monkey'])
        ['dolphin', 'elephant', 'monkey', 'walrus', 'zebra']
    '''
        
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    
    return items



def merge_sort(items):
    
    '''
    Return array of items, sorted in ascending order using the merge sort algorithm
    
    Args:
        items: list or array-like object of unordered values
       
    Returns
    array: in ascending order

    Examples:
        >>> merge_sort([12, 1, 2, 3, 4, 5])
        [1, 2, 3, 4, 5, 12]
                
        >>> merge_sort(['bob', 'jen', 'ann', 'reg', 'kip'])
        ['ann', 'bob', 'jen', 'kip', 'reg']
    '''
    
    def merge(list1,list2):    
    
        new = []

        while len(list1) >= 1 and len(list2) >= 1:
            if list1[0] < list2[0]:
                new.append(list1[0])
                list1.pop(0)
            else:
                new.append(list2[0])
                list2.pop(0)

        return new+list1+list2
    
    if len(items) == 1:
        return items       
    else:
        div = round(len(items)/2)
        ls1 = merge_sort(items[:div])
        ls2 = merge_sort(items[div:])       

        return merge(ls1, ls2)



def quick_sort(items,split_point=-1):
    
    '''
    Return array of items, sorted in ascending order using the quick sort algorithm

    Args:
        items: list or array-like object of unordered values
        split: int, optional
                index number at which to choose the split value
                default set to the last item in the input list

    Returns
    array: in ascending order

    Examples:
        >>> quick_sort([8, 3, 2, 7, 4])
        [2, 3, 4, 7, 8]
        
        >>> quick_sort(['bb', 'jj', 'aa', 'rr', 'kk'])
        ['aa','bb','jj','kk','rr']
    '''

    if len(items) <= 1:
        return items

    else:
        split = items[split_point]
        smaller = []
        larger = []
        split_val = []
        for i in items:
            if i < split:
                smaller.append(i)
            elif i > split:
                larger.append(i)
            elif i == split:
                split_val.append(i)

        smaller = quick_sort(smaller)
        larger = quick_sort(larger)

        return smaller+split_val+larger