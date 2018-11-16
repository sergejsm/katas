class List(object):
    def remove_(self, integer_list, values_list):
        return list(filter(lambda a: a not in values_list, integer_list))


l = List()
integer_list =  [1, 1, 2 ,3 ,1 ,2 ,3 ,4]
values_list = [1, 3]
print(l.remove_(integer_list, values_list))


#Best Solution

class List(object):
    def remove_(self, integer_list, values_list):
        return [i for i in integer_list if i not in values_list]