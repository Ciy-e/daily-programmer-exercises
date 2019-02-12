/*
* A special palindrome is defined as a string where all characters are the same except for the middle one
* ex : aa, aaaa, aba
*/

// finds all of the special palindrome substrings contained in a string s.
function substrCount(n, s) {
    var totalSubstrings = 0;
    for (var i = 0; i < n; i++) { 
        var differentCharFound = false;
        var charsBeforeMiddleChar = 0;
        var charsAfterMiddleChar = 0;
        for (var j = i; j < n; j++) { 

            if (s[i] === s[j] && !differentCharFound) {
                totalSubstrings++;
                charsBeforeMiddleChar++;
            } else if (s[i] === s[j] && differentCharFound) {
                charsAfterMiddleChar++;
            } else if (differentCharFound) {
                break;
            } else { 
                differentCharFound = true;
            }

            if (charsAfterMiddleChar === charsBeforeMiddleChar
                && charsBeforeMiddleChar != 0) {
                totalSubstrings++;
                break;
            }
        }

    }
    return totalSubstrings;
}