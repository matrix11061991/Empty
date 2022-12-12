class BinaryTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def add_child(self, value):
    if value <= self.value:
      if self.left is None:
        self.left = BinaryTree(value)
      else:
        self.left.add_child(value)
    else:
      if self.right is None:
        self.right = BinaryTree(value)
      else:
        self.right.add_child(value)

  def contains(self, target):
    if self.value == target:
      return True
    elif target < self.value:
      if self.left is None:
        return False
      else:
        return self.left.contains(target)
    else:
      if self.right is None:
        return False
      else:
        return self.right.contains(target)
