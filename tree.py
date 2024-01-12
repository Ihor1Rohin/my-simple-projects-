class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def what_is_the_level(self):
        level = 0
        ancestor = self.parent
        while ancestor:
            level += 1
            ancestor = ancestor.parent
        return level



    def tree_print(self):
        spaces = ' ' * self.what_is_the_level() * 4
        prefix = spaces + "|___" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.tree_print()




def build_product_tree():
    root = TreeNode("Cinema")

    detective = TreeNode("Detective")
    detective.add_child(TreeNode("Sherlock"))
    detective.add_child(TreeNode("Batman"))
    detective.add_child(TreeNode("Chase"))

    dragon = TreeNode("Dragon")
    dragon.add_child(TreeNode("Kalesgos"))
    dragon.add_child(TreeNode("Murozond"))
    dragon.add_child(TreeNode("Sindragosa"))

    book = TreeNode("Book")
    book.add_child(TreeNode("Halo"))
    book.add_child(TreeNode("Witcher"))
    book.add_child(TreeNode("Gestby"))


    root.add_child(book)
    root.add_child(dragon)
    root.add_child(detective)

    print(book.what_is_the_level())
    return root


if __name__ =='__main__':
    root = build_product_tree()
    root.tree_print()
    #print(root.what_is_the_level())
    pass

