# Ask value in Rupees and Convert into Paise.


def convert_to_paise(rupee):
    paisa = rupee * 100
    print(f"Rs {rupee} = {paisa} paisa ")


rupee = int(input("Enter rs "))
convert_to_paise(rupee)
