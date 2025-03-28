def memory_hog():
    data = []
    try:
        while True:
            # супер дупер крутий список який точно не зіпсує усю вашу пам'ять комп'ютера!
            data.append([0] * 10**6)
            print(f"Список з {len(data)} елементами займає пам'ять...")
    except MemoryError:
        print("Використано занадто багато пам'яті!")

if __name__ == "__main__":
    memory_hog()
