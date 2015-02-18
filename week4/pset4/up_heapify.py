#
# write up_heapify, an algorithm that checks if
# node i and its parent satisfy the heap
# property, swapping and recursing if they don't
#
# L should be a heap when up_heapify is done
#

# Call this routine if the heap rooted at i satisfies the heap property
# *except* perhaps i to its immediate children


def up_heapify(L, i):
    print L, i
    if no_parent(i):
        print "HAY!"
        return
    p = parent(i)
    print "node id/val:", i, L[i]
    print "parent id/val:", p, L[p]
    #if is_leaf(L, i): 
    #    if L[i] < L[p]:
    #        (L[i], L[p]) = (L[p], L[i])
    #        up_heapify(L, p)
    #    return

    if one_child(L,p):
        if L[i] < L[p]:
            (L[i], L[p]) = (L[p], L[i])
            up_heapify(L, p)
            return
    
    # if 2 child
    # if condition is ok
    print L[left_child(p)], L[right_child(p)], L[p]
    if min(L[left_child(p)], L[right_child(p)]) >= L[p]: 
        print "ok"
        # print L[left_child(p)], L[right_child(p)], L[p]
        if no_parent(p):
            return
        else:
            up_heapify(L, p)
    
    # else
    if L[left_child(p)] < L[right_child(p)]:
        (L[p], L[left_child(p)]) = (L[left_child(p)], L[p])
        if no_parent(p):
            return
        else:
            up_heapify(L, p)
    elif L[left_child(p)] > L[right_child(p)]:
        (L[p], L[right_child(p)]) = (L[right_child(p)], L[p])
        if no_parent(p):
            return
        else:
            up_heapify(L, p)
    return

def no_parent(i):
    return parent(i) == -1

def parent(i): 
    return (i-1)/2
def left_child(i): 
    return 2*i+1
def right_child(i): 
    return 2*i+2
def is_leaf(L,i): 
    return (left_child(i) >= len(L)) and (right_child(i) >= len(L))
def one_child(L,i): 
    return (left_child(i) < len(L)) and (right_child(i) >= len(L))

def test():
    L = [2, 4, 3, 5, 9, 7, 7]
    L.append(1)
    up_heapify(L, 7)
    print L
    assert 1 == L[0]
    assert 2 == L[1]

test()