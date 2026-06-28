lists=input("Enter elements separated by commas: ").split(",")
search_element=input("Enter the element to search: ")
if search_element in lists:
    print(f"{search_element} Element Found.")          
else:
    print(f"{search_element} Not Found.")          