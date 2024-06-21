
class TrieNode():
    def _init_(self):
        self.dict={}
        self.flag=False
class Trie:
    def _init_(self):
        self.root=TrieNode()
    def insert(self,word):
        node=self.root
        for i in word:
            if i not in node.dict:
                node.dict[i]=TrieNode()
            node=node.dict[i]
        node.flag=True
    def display(self):
        node=self.root
        res=[]
        def dfs(node,word):
            if node.flag==1:
                res.append(word[:])
            for i in node.dict.keys():
                dfs(node.dict[i],word+i)
        dfs(node,"")
        print(res)
    def search_word(self,word):
        node=self.root
        for i in word:
            if i not in node.dict:
                return False
            node=node.dict[i]
        if node.flag==1:
            return True
        return False
    def prefix(self,word):
        node=self.root
        for i in word:
            if i not in node.dict:
                return False
            node=node.dict[i]
        return True
                
t1=Trie()
t1.insert("word")
t1.insert("apple")
t1.insert("words")
t1.display()
print(t1.search_word("words"))
print(t1.search_word("world"))
print(t1.prefix("app"))
