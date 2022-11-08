#!/usr/bin/env python3

from app import knap

def main() -> None:
    first = knap(capacity=14, weight=[4,6,8], profit=[7,6,9])
    print("The Score of C:14, W:[4,6,8], P:[7,6,9] via Recursive: {}".format(first.recursive()))
    print("The Score of C:14, W:[4,6,8], P:[7,6,9] via TopDown: {}".format(first.dpTopDown()))
    print("The Score of C:14, W:[4,6,8], P:[7,6,9] via BottomUp: {}".format(first.dpBottomUp()))
    print("=" * 20)
    second = knap(capacity=14, weight=[5,6,8], profit=[7,6,9])
    print("The Score of C:14, W:[5,6,8], P:[7,6,9] via Recursive: {}".format(second.recursive()))
    print("The Score of C:14, W:[5,6,8], P:[7,6,9] via TopDown: {}".format(second.dpTopDown()))
    print("The Score of C:14, W:[5,6,8], P:[7,6,9] via Bottom: {}".format(second.dpBottomUp()))
    
if __name__ == "__main__":
    main()