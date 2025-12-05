def pizzasNeeded(people, slices_each):
    slices_needed = people * slices_each
    if slices_needed % 8 == 0:
        slices = slices_needed // 8
    else:
        slices = (slices_needed // 8) + 1
    return slices
print(pizzasNeeded(3, 8))