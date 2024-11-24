
class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfString=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insertNode(self,word):
        current = self.root
        for i in word:
            ch=i
            node = current.children.get(ch)
            if node==None:
                node=TrieNode()
                current.children.update({ch:node})
            current=node
        current.endOfString=True
        print("String inserted")


    def search(self,word):
        currentNode=self.root
        for i in word:
            node=currentNode.children.get(i)
            if node == None:
                return False
            currentNode=node
        if currentNode.endOfString:
            return True
        else:
            return False


def deleteNode(current_root,word,index):
    ch=word[index]
    next_node = current_root.children.get(ch)
    canThisNodeBeDeleted=False

    #case:1 #checks if the root has more than 1 child
    if len(next_node.children)>1:
        deleteNode(next_node,word,index+1)
        return False

    #case:2 : basically we will be in the last node as we are taking the starting node as the next node
    if index == len(word) - 1:
        #case:2 scenario if there are still some children for the nodes and this is true as it is in
        #        the prefix of another string which we are making false so that it would be returning true as it fails search.
        if len(next_node.children) >= 1:
            next_node.endOfString = False
            return False
        #case:4 scenario
        else:
            current_root.children.pop(ch)
            return True

    # case:3 # checks if the root has some endOfString which means there is a string until this point
    if next_node.endOfString:
        deleteNode(next_node, word, index + 1)
        return False

    canThisNodeBeDeleted=deleteNode(next_node,word,index+1)
    if canThisNodeBeDeleted:
        current_root.children.pop(ch)
        return True
    else:
        return False

newTrie=Trie()
newTrie.insertNode("APIS")
newTrie.insertNode("K")
deleteNode(newTrie.root,'K',0)
print(newTrie.search("K"))



















