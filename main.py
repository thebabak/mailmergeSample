CHANGING="[name]"
with open ("./input/names.txt") as names_file:
    names=names_file.readlines()
print(names)
with open ("./input/letter.txt") as letter_file:
    letter=letter_file.read()
    for s in names:
        strNAME=s.strip()
        print(type(strNAME))
        new=letter.replace(CHANGING,s)
        with open (f"./output/{strNAME}.txt",mode="w") as finishing:
            finishing.write(new)
