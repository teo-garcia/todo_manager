class Task:
  def __init__(self, description, completed = False):
    self.description = description
    self.completed = completed
  
  def __repr__(self):
    status = " [X]" if self.completed else " [ ]"
    return f"{status} {self.description}"