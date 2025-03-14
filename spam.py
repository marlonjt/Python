def DNA_strand(dna):
    for char in dna:
        if char == "G":
            dna.replace("G", "C")
        elif char == "C":
            dna.replace("G", "C")
        elif char == "A":
            dna.replace("A", "T")
        elif char == "T":
            dna.replace("T", "A")
    return " ".join(char)


print(DNA_strand("GTAT"))
