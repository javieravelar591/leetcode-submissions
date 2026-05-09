class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            word_len = str(len(word))
            encoded_word = word_len +"#" + word
            encoded_string += encoded_word
        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded_arr = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            i = j + 1
            j = i + length
            decoded_arr.append(s[i:j])
            i = j
        return decoded_arr