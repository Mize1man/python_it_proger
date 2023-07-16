"""
Функции (def, lambda).

"""

# nums1 = [5, 7, 9, 4]

# min = nums1[0]
# for el in nums1:
#     if el < min:
#         min = el

# print(min)


# nums2 = [5.4, 7.2, 2.3, 2.1, 9.4, 4]

# min2 = nums2[0]
# for el in nums2:
#     if el < min2:
#         min2 = el

# print(min2)

def minimal(l):
    min_number = l[0]
    for el in l:
        if el < min_number:
            min_number = el

    print(min_number)

nums1 = [5, 7, 9, 4]
minimal(nums1)

nums2 = [5.4, 7.2, 2.3, 2.1, 9.4, 4]
minimal(nums2)

# Функция lambda

func = lambda x, y: x * y
res = func(5, 2)
print(res)

