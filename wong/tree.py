class BSTNode:
    def __init__(self, data):
        self.__data = data
        self.__left = None
        self.__right = None

    def __to_left(self, data: "BSTNode"):
        if self.__left:
            self.__left.insert(data)
        else:
            self.__left = BSTNode(data)

    def __to_right(self, data: "BSTNode"):
        if self.__right:
            self.__right.insert(data)
        else:
            self.__right = BSTNode(data)

    def __repr__(self):
        return str(self.__data)

    def insert(self, data: "BSTNode"):
        if data < self.__data:
            self.__to_left(data)
        elif data > self.__data:
            self.__to_right(data)

    def pre_order(self):
        r_list = []
        r_list.append(self)

        if self.__left:
            r_list.extend(self.__left.pre_order())
        if self.__right:
            r_list.extend(self.__right.pre_order())

        return r_list

    def in_order(self):
        r_list = []

        if self.__left:
            r_list.extend(self.__left.in_order())
        if self.__right:
            r_list.append(self)
            r_list.extend(self.__right.in_order())
        else:
            r_list.append(self)

        return r_list

    def post_order(self):
        r_list = []

        if self.__left:
            r_list.extend(self.__left.post_order())
        if self.__right:
            r_list.extend(self.__right.post_order())

        r_list.append(self)

        return r_list
