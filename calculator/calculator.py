import math

def calculate(fnum, process, snum):
    if process == "+":
        result = fnum + snum
    elif process == "/":
        result = fnum / snum
    elif process == "*":
      result = fnum * snum
    elif process == "**":
        result = fnum * snum
    elif process == "root":
        result = math.sqrt(fnum)
    else:
        result = "An Error has occured please try again."
    return result

