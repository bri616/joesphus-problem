class Node:
  def __init__(self, name=None, next=None):
    self.name = name
    self.next = next
  def __str__(self):
    return str(self.name)


class CircularList(object):
  def __init__(self):
    self.head = Node(None, None)
    self.head.next = Node(None, self.first)

  def __str__(self):
    a = "["
    current = self.first
    while current != None:
      a += str(current.data) + ', '
      current = current.next
    a = a[:-2] + ']'
    return a

  def InsertLast(self, item):
    NewNode = Node(item)
    current = self.first

    if current == None:
      self.first = NewNode
      return

    while current.next != None:
      current = current.next
    current.next = Node(item)
