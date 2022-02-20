
def move_element_to_end(array, toMove):

    i = 0
    j = len(array)-1
    while i < j:
        if array[i] == toMove and array[j] == toMove:
            j-=1
        elif array[i] == toMove and array[j] != toMove:
            print('before array', array)
            array[i], array[j]  = array[j], array[i]
            i+=1
            j-=1
            print('after array', array)
        elif array[i] != toMove and array[j] == toMove:
            i+=1
            j-=1
        elif array[i] != toMove and array[j] != toMove:
            i+=1
    
    return array


array = [2,1,2,2,2,3,4,2]
toMove = 2

move_element_list = move_element_to_end(array, toMove)
# print('move_element_list', move_element_list)