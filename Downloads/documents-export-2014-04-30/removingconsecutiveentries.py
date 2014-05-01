from sys import argv

script, filename = argv
txt = open (filename)
logs = [line.strip() for line in open(filename)]

i = 0
endoffile = "id:endoffile"
logs.append(endoffile)

for traverse in logs:
     if logs[i] == endoffile:
          break
     if not logs[i] == logs[i+1]:
          print logs[i]
     i+=1



