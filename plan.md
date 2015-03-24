# Josephus problem


* when the current node is pointing to itself it is the survivor

    def only_one_survives(number_of_people, starting_person, number_to_skip):
        create linked list (last person points to starting person, not nil)
        find starting point and set as current_node
        while current_node.next != current_node:
            skip the appropriate number of nodes by
                do a for loop using the range of number to skip by doing current_node=current_node.next
                kill the appropriate node by changing the pointer of the current_node to the one after its pointer
                (current_node.next = current_node.next.next ?)
                go to the next node, that is now current_node and the while loop goes next
        
        return current_node