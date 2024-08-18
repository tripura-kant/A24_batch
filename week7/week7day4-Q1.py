# User function Template for python3

# Insert into dictionary and print "Inserted"
def insert_dict(key, value, Dict):
    Dict[key] = value
    print("Inserted")


# Delete from dictionary and print "Deleted" if key is present, else "-1"
def del_dict(key, Dict):
    if key in Dict:
        del Dict[key]
        print("Deleted")
    else:
        print("-1")


# Print marks of student with the specified key if present in dictionary
# Otherwise, print "-1"
def print_dict(key, Dict):
    if key in Dict:
        print(f"Marks of {key} is : {Dict[key]}")
    else:
        print("-1")


# Driver code
def main():
    for _ in range(int(input())):
        Q = int(input())
        Dict = {}
        for _ in range(Q):
            query = input().split()
            if query[0] == 'i':
                insert_dict(query[1], query[2], Dict)
            elif query[0] == 'd':
                del_dict(query[1], Dict)
            elif query[0] == 'p':
                print_dict(query[1], Dict)


if __name__ == '__main__':
    main()
