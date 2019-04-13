#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from treelib import Tree, Node
import time


def duplicate_node_path_check(tree, node):
    validated_node = node
    result = False
    while not node.is_root():
        node = tree.parent(node.identifier)
        result = validated_node.tag == node.tag
    return result



reachable_states = {"Gdansk": [["Gdynia", 24], ["Koscierzyna", 58], ["Tczew", 33], ["Elblag", 63]],
                    "Gdynia": [["Gdansk", 24], ["Lebork", 60], ["Wladyslawowo", 33]],
                    "Koscierzyna": [["Gdansk", 58], ["Tczew", 59], ["Lebork", 58], ["Chojnice", 70], ["Bytów", 40]],
                    "Bytów": [["Chojnice", 65], ["Koscierzyna", 40], ["Slupsk", 70]],
                    "Chojnice": [["Koscierzyna", 70], ["Bytów", 65]],
                    "Slupsk": [["Bytów", 70], ["Ustka", 21], ["Lebork", 55]],
                    "Elblag": [["Tczew", 53], ["Gdansk", 63]],
                    "Tczew": [["Elblag", 53], ["Gdansk", 33]],
                    "Lebork": [["Leba", 29], ["Gdynia", 60], ["Slupsk", 55]],
                    "Hel": [["Wladyslawowo", 35]],
                    "Wladyslawowo": [["Hel", 35], ["Gdynia", 42], ["Leba", 66]],
                    "Leba": [["Lebork", 29], ["Wladyslawowo", 66], ["Ustka", 64]],
                    "Ustka": [["Leba", 64], ["Slupsk", 21]]}


def breadth_first_search(start_state, target_state):
    # do budowy drzewa potrzebujemy dla kazdego wierzcholka id
    # bedziemy je pozniej inkrementowac
    id = 0
    # #wrzucenie stanu startowego do drzewa (korzen) i kolejki
    tree = Tree()
    current_node = tree.create_node(start_state, id)
    fifo_queue = []
    fifo_queue.append(current_node)
    # petla szukajaca sciezki do stnau koncowego
    # #robimy ograniczenie na max wierzcholkow (id<200000)
    while id < 200000:
        # jesli kolejka pusta to znaczy ze nie da sie dojsc do stanu koncowego #drukowanie kolejki: print(fifo_queue)
        if len(fifo_queue) == 0:
            tree.show()
            print("failed to reach the target state")
            return 1
            # jesli kolejka niepusta to wez pierwszy stan z kolejki
        current_node = fifo_queue[0]
        # jesli ten stan jest koncowy to zakoncz program z sukcesem
        if current_node.tag == target_state:
            tree.show()
            print("the target state " + str(current_node.tag) + " with id = " + str(
                current_node.identifier) + " has been reached!")
            return 0
            # jesli stan niekoncowy to usun go z kolejki
        del (fifo_queue[0])
        # a nastepnie dodaj stany osiagalne z niego
        # #na koniec kolejki i do drzewa
        if not duplicate_node_path_check(tree, current_node):
            for elem in reachable_states[current_node.tag]:
                id += 1
                new_elem = tree.create_node(elem[0], id, parent=current_node.identifier)
                fifo_queue.append(new_elem)
    print("time limit exceeded")


start = time.time()
breadth_first_search("Gdansk", "Ustka")
end = time.time()
print(end - start)


def depth_first_search(start_state, target_state):
    # do budowy drzewa potrzebujemy dla kazdego wierzcholka id
    # bedziemy je pozniej inkrementowac
    id = 0
    # #wrzucenie stanu startowego do drzewa (korzen) i kolejki
    tree = Tree()
    current_node = tree.create_node(start_state, id)
    lifo_stack = []
    lifo_stack.append(current_node)
    # petla szukajaca sciezki do stnau koncowego
    # #robimy ograniczenie na max wierzcholkow (id<200000)
    while id < 200000:
        # jesli kolejka pusta to znaczy ze nie da sie dojsc do stanu koncowego #drukowanie kolejki: print(fifo_queue)
        if len(lifo_stack) == 0:
            tree.show()
            print("failed to reach the target state")
            return 1
            # jesli kolejka niepusta to wez pierwszy stan z kolejki
        current_node = lifo_stack.pop()
        # jesli ten stan jest koncowy to zakoncz program z sukcesem
        if current_node.tag == target_state:
            tree.show()
            print("the target state " + str(current_node.tag) + " with id = " + str(
                current_node.identifier) + " has been reached!")
            return 0
            # jesli stan niekoncowy to usun go z kolejki
        # del (lifo_stack[0])
        # a nastepnie dodaj stany osiagalne z niego
        # #na koniec kolejki i do drzewa
        if not duplicate_node_path_check(tree, current_node):
            for elem in reachable_states[current_node.tag]:
                id += 1
                new_elem = tree.create_node(elem[0], id, parent=current_node.identifier)
                lifo_stack.insert(0, new_elem)
    print("time limit exceeded")


start = time.time()
depth_first_search("Gdansk", "Ustka")
end = time.time()
print(end - start)


def uniform_cost_search(start_state, target_state):
    # do budowy drzewa potrzebujemy dla kazdego wierzcholka id
    # bedziemy je pozniej inkrementowac
    id = 0
    # #wrzucenie stanu startowego do drzewa (korzen) i kolejki
    tree = Tree()
    current_node = tree.create_node(start_state, id, data=0)
    priority_queue = []
    priority_queue.append(current_node)
    # petla szukajaca sciezki do stnau koncowego
    # #robimy ograniczenie na max wierzcholkow (id<200000)
    while id < 200000:
        # jesli kolejka pusta to znaczy ze nie da sie dojsc do stanu koncowego #drukowanie kolejki: print(fifo_queue)
        if len(priority_queue) == 0:
            tree.show()
            print("failed to reach the target state")
            return 1
            # jesli kolejka niepusta to wez pierwszy stan z kolejki
        priority_queue = sorted(priority_queue, key=lambda x: x.data)
        current_node = priority_queue[0]
        # jesli ten stan jest koncowy to zakoncz program z sukcesem
        if current_node.tag == target_state:
            tree.show()
            print("the target state " + str(current_node.tag) + " with id = " + str(
                current_node.identifier) + " has been reached after " + str(current_node.data) + " kms!")
            return 0
            # jesli stan niekoncowy to usun go z kolejki
        del (priority_queue[0])
        # a nastepnie dodaj stany osiagalne z niego
        # #na koniec kolejki i do drzewa
        if not duplicate_node_path_check(tree, current_node):
            for elem in reachable_states[current_node.tag]:
                id += 1
                new_elem = tree.create_node(elem[0], id, parent=current_node.identifier)
                new_elem.data = current_node.data + elem[1]
                priority_queue.append(new_elem)
        print("time limit exceeded")

# start = time.time()
# uniform_cost_search("Gdansk", "Ustka")
# end = time.time()
# print(end - start)


# In[ ]:




