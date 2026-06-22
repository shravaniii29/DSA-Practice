class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # Assume the first string is the common prefix initially
        prefix = strs[0]

        # Compare the prefix with every other string
        for s in strs[1:]:

            # Keep shortening the prefix until
            # the current string starts with it
            while not s.startswith(prefix):

                # Remove the last character
                prefix = prefix[:-1]

                # If prefix becomes empty,
                # no common prefix exists
                if prefix == "":
                    return ""

        # Final common prefix
        return prefix