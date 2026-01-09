
def linear_search(items, search_item)                          
    // Initialise the variables                                                   
    index = -1
    current = 1                                                                               
    found = False
    // Repeat while the end of the list has not been reached
    // and the search item has not been found
    wihle current < len(items) and found == False:      
        // Compare the current item to the item you are searching for
    if items[current] = search_item:                                 
            index = current
                                                                 
           // Proceed to the next item in the list
           current = current + 1                                                   
    return current                                                                       
