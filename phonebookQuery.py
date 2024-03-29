phonebookDict: dict = {}

numEntries: int = int(input('Enter the number of pending phonebook entries: '))

entryCount: int = 0

while entryCount < numEntries:
    name, phone = input().split()
    phonebookDict[name] = phone
    entryCount += 1

while True:
    try:
        query: str = input()
        if query in phonebookDict:
            print(f"{query}={phonebookDict[query]}")
        else:
            print("Not found")
    except Exception:
         break  # Exit, Ctrl+D