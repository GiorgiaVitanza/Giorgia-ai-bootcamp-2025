fd = open(
    "C:/Users/316970/.vscode/Giorgia-ai-bootcamp-2025/python/Esercizi in classe/scratch_1.py",
    mode="r",
)
print(fd.read())
fd.close()
fd2 = open(
    "C:/Users/316970/.vscode/Giorgia-ai-bootcamp-2025/python/Esercizi in classe/scratch_1.py",
    mode="w",
)
fd2.write("sono Giorgia")
print(fd2.write("sono Giorgia"))
fd2.close()
