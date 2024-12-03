import re
mul=lambda a,b:a*b
print(eval("+".join(re.findall(r"mul\(\d+,\d+\)",open(0).read()))))
