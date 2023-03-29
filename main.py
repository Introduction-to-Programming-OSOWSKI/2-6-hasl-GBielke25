def hasL(w):
    num = 0
    for i in range(0, len(w)):
        if w[i] == "l":
            return True
    return False
    
hasL("alabama")