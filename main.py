#
from pyscript import display

class classmate:
   def __init__(self, name, section, subject):
       self.name = name
       self.section = section
       self.subject = subject


student = [(name, section, subject) for name, section, subject in [
   ("Mergal", "Sapphire", "Math"), ("Seth", "Sapphire","PE"), ("Vito", "Sapphire","Math")
]]

for human in student:
   print(f"Hi! my name is{human.name}my section is{human.section}and my favorite subject is{human.subject}.")



