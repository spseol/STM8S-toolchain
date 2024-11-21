def pick(options, title):
    """Jednoduchá náhrada za pick bez závislosti na curses"""
    print("\n" + title)
    for i, option in enumerate(options, 1):
        print(f"{i}) {option}")

    while True:
        try:
            choice = input("\nZadejte číslo volby: ")
            index = int(choice) - 1
            if 0 <= index < len(options):
                return options[index], index
            print(f"Prosím zadejte číslo mezi 1 a {len(options)}")
        except ValueError:
            print("Prosím zadejte platné číslo")
