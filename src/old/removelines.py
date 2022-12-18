
def func(value):
    file = open(value)
    line = file.read()
    appendFile = open("/Users/varunjoshi/Documents/Python/STIA_458/stiaFinalProject/Data/RegionalSets/newTest.txt", 'a')
    description = ""
    description.join(line.splitlines())
    appendFile.write(description)

    # return ''.join(line.splitlines())

# appendFile = open("/Users/varunjoshi/Documents/Python/STIA_458/stiaFinalProject/Data/RegionalSets/newTest.txt")
func("Data/RegionalSets/Africa.txt")
# func("/Users/varunjoshi/Documents/Python/STIA_458/stiaFinalProject/Data/RegionalSets/Africa.txt")
