guests_1        = [ "Bethaney Bain", "Kacey Johns", "Manpreet Saunders" ]
guests_2        = [ "Elwood Curtis", "Diya Griffin", "Kacey Johns" ]
guests_3        = [ "Tobey Weiss", "Kadie Barnes", "Diya Griffin" ]

guests_fin_list = []

for i in guests_1 + guests_2 + guests_3:
    if i not in guests_fin_list:
        guests_fin_list.append(i)
        guests_fin_list.sort() 

print(guests_fin_list)