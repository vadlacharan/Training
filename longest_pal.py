def longest_repeated_substring(s):
    n = len(s)
    # Create and initialize the table to store results of subproblems
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    longest = 0
    ending_index = n

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if (s[i - 1] == s[j - 1] and
                dp[i - 1][j - 1] < (j - i)):
                dp[i][j] = dp[i - 1][j - 1] + 1

                if dp[i][j] > longest:
                    longest = dp[i][j]
                    ending_index = max(i, ending_index)
            else:
                dp[i][j] = 0

    return s[ending_index - longest: ending_index]

# Example usage
s = "banana"
print(longest_repeated_substring(s))  # Output: "ana"
