#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from treelib import Tree, Node

tree = Tree()
tree.create_node("Henrietta", "h")
tree.create_node("Joseph", "j", parent="h")
tree.create_node("Beatrice", "b", parent="h")
tree.create_node("Diarmuid", "d", parent="j")
tree.create_node("Miriam", "m", parent="d")
tree.create_node("Henrietta", "h2", parent="j")

tree.show()

x = tree.get_node("m")
print(x.tag)
print(x.identifier)
y = tree.parent("m")
print(y.tag)
print(y.identifier)
z = tree.get_node("h")
print(z.tag)
print(z.is_root())


def duplicate_node_path_check(tree, node):
    validated_node = node
    result = False
    while not node.is_root():
        node = tree.parent(node.identifier)
        result = validated_node.tag == node.tag
    return result

print(duplicate_node_path_check(tree, tree.get_node("h2")))


# In[ ]:




