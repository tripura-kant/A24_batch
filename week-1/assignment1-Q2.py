# Python program to convert kilometers to miles. Ask kilometer from
# User.

def convert_to_km(km):
    miles = km * 0.621
    print(miles)


km = int(input("Enter km    "))
convert_to_km(km)
