from sys import argv
script, filename = argv
txt = open (filename)
app_name = "id:"
logs = [line.strip() for line in open(filename)]

for traverse in logs:
     applogs = traverse.split()
     for iterating in applogs:
          if not iterating.find(app_name):
               print iterating

