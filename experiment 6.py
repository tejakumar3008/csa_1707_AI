def vacuum_cleaner():
    room = {}
    room['A'] = input("Enter status of Room A (Clean/Dirty): ")
    room['B'] = input("Enter status of Room B (Clean/Dirty): ")
    current = 'A'
    print("\nInitial Room Status:", room)
    for _ in range(2):  
        if room[current] == "Dirty":
            print(f"Vacuum in Room {current}: Cleaning...")
            room[current] = "Clean"
        else:
            print(f"Vacuum in Room {current}: Already clean")
        current = 'B' if current == 'A' else 'A'
    print("\nFinal Room Status:", room)
vacuum_cleaner()
