import math

class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page


    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        return math.ceil(self.item_count()/self.items_per_page)

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        print(self.page_count())
        if page_index in range(self.page_count()):
            if page_index+2 <= self.page_count():
                return self.items_per_page
            else:
                return self.item_count() % self.items_per_page
        else:
            return -1

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):

        if item_index in range(self.item_count()):
            return item_index // self.items_per_page
        else:
            return -1


collection = range(1, 25)
helper = PaginationHelper(collection, 10)


print(helper.page_count())
print(helper.item_count())
print(helper.page_item_count(2))

print(helper.page_index(10))
