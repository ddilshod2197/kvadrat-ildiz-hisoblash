def harflar_soni(matn):
    return len(matn.replace(" ", ""))

matn = input("Matnni kiriting: ")
print("Harflar soni:", harflar_soni(matn))
