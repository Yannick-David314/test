# def all_in(a, b):
#     for i in a:
#         if i not in b:
#             return False
#     return True

# print(all_in([1, 2], [1, 2, 3]))
# print(all_in([1, 2], [3, 4, 5]))



# def create_dictionary(keys, values):
#     result = {}
#     for i in range(len(keys)):
#         result[keys[i]] = values[i]
#     return result

# print(create_dictionary(['a', 'b', 'c'], [1, 2, 3]))



# def print_pair(dictionary, target):
#     if target not in dictionary:
#         print("Key not found")
#     else:
#         print("Key: " + target)
#         print("Value: " + str(dictionary[target]))

# print_pair({'a': 1, 'b': 2, 'c': 3}, 'b')



# def keys_v_values(dictionary):
#     total_key = 0
#     total_value = 0

#     for key, value in dictionary.items():
#         total_key += key
#         total_value += value

#     if total_key < total_value:
#         return "values"
#     elif total_key > total_value:
#         return "keys"
#     else:
#         return "balanced"
    
# dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
# print(keys_v_values(dictionary1))

# dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
# print(keys_v_values(dictionary2))



# def restock_inventory(current_inventory, restock_list):
#     for key in restock_list:
#         if key in current_inventory:
#             current_inventory[key] += restock_list[key]
#         else:
#             current_inventory[key] = restock_list[key]

#     return current_inventory

# a = {
#     "apples": 30,
#     "bananas": 15,
#     "oranges": 10
# }

# b = {
#     "oranges": 20,
#     "apples": 10,
#     "pears": 5
# }

# restock_inventory(a, b)
# print(a)



# def calculate_gpa(report_card):
#     grades = report_card.values()
#     total_grade = 0
#     for grade in grades:
#         if grade == 'A':
#             grade = 4
#         elif grade == 'B':
#             grade = 3
#         elif grade == 'C':
#             grade = 2
#         elif grade == 'D':
#             grade = 1
#         else:
#             grade = 0

#         total_grade += grade

#     gpa = float(total_grade/len(grades))
#     return gpa

# a = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
# print(calculate_gpa(a))



# def highest_rated(books):
#     highest_book = []
#     highest_rating = 0
#     for book in books:
#         if book['rating'] > highest_rating:
#             highest_rating = book['rating']
#             highest_book = [] 
#             highest_book.append(book)
#         elif book['rating'] == highest_rating:
#             highest_book.append(book)
#     return highest_book
# # Modified the program in case there are multiple books with the highest
# # ratings
# a = [
#     {"title": "Tomorrow, and Tomorrow, and Tomorrow",
#      "author": "Gabrielle Zevin",
#      "rating": 4.18
#     },
#     {"title": "A Fortune For Your Disaster",
#      "author": "Hanif Abdurraqib",
#      "rating": 4.47
#     },
#     {"title": "The Seven Husbands of Evenlyn Hugo",
#      "author": "Taylor Jenkins Reid",
#      "rating": 4.40
#     }
# ]

# print(highest_rated(a))



# def index_to_value_map(lst):
#     map = {}
#     for i in range(len(lst)):
#         map[i] = lst[i]
#     return map

# b = ["apple", "banana", "cherry"]
# print(index_to_value_map(b))

'''
you have a list
you want to check if consecutive elements are all gretaer or lesser
than their preds

repeat until nums[i+1] = None
(
check if nums[i] > nums[i+1] and nums[i+1] > nums[i+2] or nums[]
increase counter by 1

if at end counter is length of list** return true
)

'''














































nums1 = [1,2,2,3,10]
print(is_monotonic(nums1))

nums2 = [12,9,8,3,1]
print(is_monotonic(nums2))

nums3 = [1,1,1]
print(is_monotonic(nums3))

nums4 = [1,9,8,3,5]
print(is_monotonic(nums4))
    



















        