# This is all my code


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()

    def insert(self, value, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

        current_node = self.root

        if value == '/':
            current_node.handler = 'root handler'

        for item in value.split('/'):
            if item not in current_node.children:
                current_node.insert(item)
            current_node = current_node.children[item]
        current_node.handler = handler

    def find(self, value):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        current_node = self.root

        if value == '/':
            current_node.handler = 'root handler'
            return self.root

        split_value = value.split('/')

        for item in range(len(split_value)):
            if split_value[item] in current_node.children:
                current_node = current_node.children[split_value[item]]
            elif item == len(split_value) - 1 and split_value[item] == '':
                return current_node

            else:
                return None
        # print('f:',current_node.handler)
        return current_node


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None

    def insert(self, value):
        # Insert the node as before

        self.children[value] = RouteTrieNode()

# The Router class will wrap the Trie and handle

class Router:
    def __init__(self, handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!

        self.routeTrie = RouteTrie()
        self.add_handler("/", handler)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie

        self.routeTrie.insert(path, handler)

        # print('a: ',self.routeTrie.find(path).handler)


    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        value = self.routeTrie.find(path)

        if value == None:
            return None

        if value.handler == None:
            return 'Not found handler'
        return value.handler


    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        pass

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' 
print(router.lookup("/home/about/me")) # should print None 

# Answers Test 1
# root handler
# Not found handler
# about handler
# None
# None

router = Router("root handler") 
router.add_handler("/home/about/me/my_friend", "my friend handler")  


print(router.lookup("/")) 
print(router.lookup("")) 
print(router.lookup("/home")) 
print(router.lookup("/home/about/")) 
print(router.lookup("/home/about/me/my_friend"))

# root handler
# Not found handler
# Not found handler
# Not found handler
# my friend handler

router = Router("root handler") 
router.add_handler("/home/about/me/my_friend", "my friend handler")  
router.add_handler("/home/about/me/my_friend", "my friend handler 2")  
router.add_handler("/home/about/", "about handler")  


print(router.lookup("/")) 
print(router.lookup("/home/home")) 
print(router.lookup("/home")) 
print(router.lookup("/home/about/")) 
print(router.lookup("/home/about/me/my_friend"))
print(router.lookup("/home/about/me/my_friend/"))

# root handler
# None
# Not found handler
# about handler
# my friend handler 2
# my friend handler 2