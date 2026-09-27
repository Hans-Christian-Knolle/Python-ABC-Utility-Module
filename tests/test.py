from src.math.basic import *

def main() -> None:
    numA = 5
    numB = 13

    a = add(numA, numB)
    b = sub(numA, numB)
    c = mul(numA, numB)
    d = div(numA, numB)
    e = mod(numA, numB)
    f = exp(numA, numB)

    print(f"a: {a}, b: {b}, c: {c}, d: {d}, e: {e}, f: {f}")

if __name__ == '__main__':
    main()
