from count_min_sketch import get_random_hash_function, hash_string


class BloomFilter:
    def __init__(self, nbits, nhash):
        self.bits = [False]*nbits # Initialize all bits to fals
        self.m = nbits
        self.k = nhash
        # get k randdom hash functions
        self.hash_fun_reps = [get_random_hash_function() for i in range(self.k)]
    
    # Function to insert a word in a Bloom filter.
    def insert(self, word):
        # your code here
        for i in range(self.k):
            idx = hash_string(self.hash_fun_reps[i], word)
            self.bits[idx%self.m] = True
        
    # Check if a word belongs to the Bloom Filter
    def member(self, word):
        # your code here
        for i in range(self.k):
            idx = hash_string(self.hash_fun_reps[i], word)
            if not self.bits[idx%self.m]:
                return False
        return True

filename = './great-gatsby-fitzgerald.txt'
file = open (filename,'r')
txt = file.read()
txt = txt.replace('\n',' ')
words= txt.split(' ')
longer_words_gg = list(filter(lambda s: len(s) >= 5, words))

all_words_gg = set(longer_words_gg)
exact_common_wc = 0
filename = './war-and-peace-tolstoy.txt'
file = open (filename,'r')
txt = file.read()
txt = txt.replace('\n',' ')
words= txt.split(' ')
longer_words_wp = list(filter(lambda s: len(s) >= 5, words))

for word in longer_words_wp:
    if word in all_words_gg:
        exact_common_wc = exact_common_wc + 1
print(f'Exact common word count = {exact_common_wc}')

bf = BloomFilter(100000, 5)
for word in longer_words_gg:
    bf.insert(word)
    
for word in longer_words_gg:
    assert (bf.member(word)), f'Word: {word} should be a member'

common_word_count = 0
for word in longer_words_wp:
    if bf.member(word):
        common_word_count= common_word_count + 1
print(f'Number of common words of length >= 5 equals : {common_word_count}')
assert ( common_word_count >= exact_common_wc)
print('All Tests Passed: 10 points')