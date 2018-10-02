import difflib
print("Night Canteen List")

list_of_canteens = ['Cafe Dialog', 'Kebab Nation', 'Login', 'Saras']

res = input("\nEnter Night Canteen Hotel Name \n")
matches = difflib.get_close_matches(res, list_of_canteens, 2)
print("Matches", matches)
for match in matches:
    print(match)
