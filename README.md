# NaiveAlgorithm

# Task:

To implement the specified algorithm for finding the substrate in the tape.

# Solving of the problem:

First, the beginning and end of the tape function was created, in the parameters of which the definition was passed that any record will be displayed in "string" format.
An array of substrings has been created, which is not yet filled with data. Below are created variables that are assigned a function that determines the length of records.
There is a check for the presence of when the length of the trim is zero. If this is present, the empty array initialized above will be returned.
The algorithm checks the possible coincidence of letters or words, which can be formed from the tape. If some part of the substring corresponds to some entry in the sentence, in the word that forms the substring, the initial and final elements of this tape are added to the list of found substrings in sentences and words that are available.
On the other hand, when there are no matches, the loop is interrupted and at the same time there is a transition to the next available word in a given array of elements. A match that is not found matches the end of the list. Word search will occur as long as the length of the tape allows.

# The complexity of this algorithm:

This algorithm uses two loops to match and match the letters in the tape that can be displayed in the substring. All available tapes in the word array are checked. This check is supplemented by finding the location of a certain element, as an incentive. As a result, you can get the product of lengths: tape and substring. So, O(N x M).

