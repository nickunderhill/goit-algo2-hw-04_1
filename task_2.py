from trie import Trie


class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not all(
            isinstance(s, str) for s in strings
        ):
            raise TypeError("Input must be a list of strings.")

        if not strings:  # Handle empty input
            return ""

        # Insert all strings into the trie
        for string in strings:
            self.put(string)

        # Find the longest common prefix
        def find_prefix(node):
            prefix = []
            current = node

            while current and len(current.children) == 1 and current.value is None:
                char, child = next(iter(current.children.items()))
                prefix.append(char)
                current = child

            return "".join(prefix)

        return find_prefix(self.root)


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    trie = LongestCommonWord()
    strings = []
    assert trie.find_longest_common_word(strings) == ""
