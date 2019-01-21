
class AdminUser():
    def __init__(self, username):
        self.username = username

    def delete_any(self, key, value):
        items = [item for item in comments if item[key] == value]
        return items[0]
        comments.remove(items)

    def delete(self, value):
        value = input ("Which comment would you like to delete: ")
        resp = AdminUser().delete_any("value", value)
        print ("Successfully deleted comment")