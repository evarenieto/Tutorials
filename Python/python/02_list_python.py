books = [
"super nova - Eddin Cooler",
"badmat - Chirtian Vally",
"heidi - chino mandarino",
"cenicienta - disney"
]

video_games = [
"The Legend of Zelda: Breath of the Wild",
"Splatoon 2",
"Super Mario Odyssey",
]

print("Suggested gift: {}".format(books[0]))
print("Books:")
for book in books:
    print("* " + book)

for book in books:
    if book[0] == "b": print("* " + book)

def display_wishlist(display_name, wishes):
    #as many times we run this code, the last item in going to be
    #deleted again and again, to avoid this, we´ll used the
    #copy() funcion
    items = wishes.copy()
    print(display_name, ":")
    suggested_gift = wishes.pop(0)
    print("=========>", suggested_gift,"<========")
    for item in items:
        print("* " + item)
    print()

display_wishlist("Books", books)
display_wishlist("Video games", video_games)
