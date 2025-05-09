import collections

class TrieNode:
    """Represents a single node in the Trie."""
    def __init__(self):
        # Using collections.defaultdict simplifies child creation
        self.children = collections.defaultdict(TrieNode)
        # Flag to mark the end of a complete word
        self.is_end_of_word = False

class Trie:
    """Trie data structure implementation."""
    def __init__(self):
        """Initializes the Trie with an empty root node."""
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Inserts a word into the Trie."""
        node = self.root
        for char in word:
            # If char not in node.children, defaultdict creates a new TrieNode
            node = node.children[char]
        # Mark the end of the word
        node.is_end_of_word = True
        # print(f"Inserted '{word}'") # Optional: for tracing

    def search(self, word: str) -> bool:
        """Searches for an exact word match in the Trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                # Character path doesn't exist
                return False
            node = node.children[char]
        # Word path exists, check if it's marked as a complete word
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        """Checks if any word in the Trie starts with the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                # Prefix path doesn't exist
                return False
            node = node.children[char]
        # Prefix path exists
        return True

if __name__ == "__main__":
    # --- Example Usage ---
    trie = Trie()

    # Insert words
    words_to_insert = ["apple", "app", "apricot", "banana", "bat", "batch"]
    for word in words_to_insert:
        trie.insert(word)

    # Search for exact words
    print(f"Search 'apple': {trie.search('apple')}")       # Output: True
    print(f"Search 'app': {trie.search('app')}")         # Output: True
    print(f"Search 'appl': {trie.search('appl')}")        # Output: False (it's a prefix, not a full word)
    print(f"Search 'banana': {trie.search('banana')}")     # Output: True
    print(f"Search 'ban': {trie.search('ban')}")          # Output: False
    print(f"Search 'batman': {trie.search('batman')}")     # Output: False

    print("-" * 10)

    # Check for prefixes
    print(f"StartsWith 'app': {trie.startsWith('app')}")     # Output: True (apple, app, apricot)
    print(f"StartsWith 'apl': {trie.startsWith('apl')}")     # Output: False
    print(f"StartsWith 'ban': {trie.startsWith('ban')}")     # Output: True (banana)
    print(f"StartsWith 'ba': {trie.startsWith('ba')}")      # Output: True (banana, bat, batch)
    print(f"StartsWith 'batch': {trie.startsWith('batch')}")   # Output: True (batch)
    print(f"StartsWith 'batman': {trie.startsWith('batman')}") # Output: False
