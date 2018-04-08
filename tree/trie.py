""" Python Implementation of Trie """

import json


class Trie(object):

    def __init__(self):
        self.trie = {}

    def __repr__(self):
        return json.dumps(self.trie, indent=4)

    def add(self, word: str):
        word = word.strip()
        p = self.trie
        for char in word:
            if char not in p:
                p[char] = {}
            p = p[char]
        p[' '] = ' '

    def search(self, word):
        """ Search words with prefix """
        p = self.trie
        for char in word:
            if char not in p:
                return False
            p = p[char]
        if ' ' in p:
            return True
        return False

    def getItems(self, prefix):
        p = self.trie
        for char in prefix:
            if char not in p:
                return
            p = p[char]
        self._getItemsRec(p, prefix)

    def _getItemsRec(self, p, prefix):
        if ' ' in p:
            print(prefix)
        for char in p:
            if char != ' ':
                self._getItemsRec(p[char], prefix + char)


trie = Trie()
trie.add('abc')
trie.add('abd')
trie.add('acd')
trie.add('ace')
r = trie.search('abd')
print(trie)
print(r)
trie.getItems('ae')
