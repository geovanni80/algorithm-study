def searchKey(box, pile):
    for item in box:
        if item == "key":
            print("the key was found")
        else:
            pile.append(item)
    print(f"pile: {pile}")

main_box = ["fan","skateboard","toy","key"]
pile = []

searchKey(main_box, pile)