menu = ["githeri", "gwashi", "avocado", "ugali", "chai"]

def find_item(item):
    if item[0] == 'c':
        return item
    
map_items = map(find_item, menu)
for x in map_items:
    #print(x)
    pass
#print(map_items)

filter_items = filter(find_item, menu)
for x in filter_items:
    print(x)