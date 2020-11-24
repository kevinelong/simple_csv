""" EXAMPLE simple_csv.csv
ID,NAME,PRICE,DESCRIPTION,PHOTO_URL
1001,Meat Lovers,29.99,All the meats!,http://www.example.com/photos/img_1001.png
1002,Veggie Delight,29.99,All the veg!,http://www.example.com/photos/img_1002.png
"""

line_list = open("simple_csv.csv", "r").readlines()
PRICE_INDEX = 2
grand_total = 0.0
for line_index, line_text in enumerate(line_list):
    parts = line_text.split(",")
    if line_index > 0:
        grand_total += float(parts[PRICE_INDEX])
print(grand_total)
