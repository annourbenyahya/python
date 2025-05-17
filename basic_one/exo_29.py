#Python program that prints out all colors from color_list_1 that are not present in color_list_2.
color_list_1 = {"White", "Black", "Red"}
color_list_2 = {"Red", "Green"}

# Find the difference
unique_colors = color_list_1 - color_list_2

print(unique_colors)  # Output: {'Black', 'White'}
