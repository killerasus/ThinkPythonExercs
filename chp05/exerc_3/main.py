def is_triangle(a : int, b : int, c : int) :
    if((a + b) < c or (a + c) < b or (b + c) < a) :
        print("No")
    else:
        print("Yes")

def check_triangle() :
    print("Verifies if a triangle is possible.")
    a = int(input("Enter size for a: "))
    b = int(input("Enter size for b: "))
    c = int(input("Enter size for c: "))
    is_triangle(a, b, c)

check_triangle()