# For this exercise, you will need to create a helper to generate a pretty field name for our errors. Most of our field names are in camel case format (e.g. `amountDue`).

# Some of our field names have an error descriptions that span across multiple words (e.g. `Business EIN`)

# Hence, we want to create an agnostic helper function that can take in a string and output a pretty error field name (see input/output examples below).

# Input -> Output
# 1. itemPrice -> Item price
# 2. itemPrice incorrectType -> Item price incorrect type
# 3. Business EIN number -> Business EIN number

# Bonus:
# hasEINPresent -> Has EIN present

# current implementation only works for simple camelcase strings
def camel_case_split(str):
    words = [[str[0]]]

    print(words)

    for c in str[1:]:
        if words[-1][-1].islower() and c.isupper():
            words.append(list(c))
        else:
            words[-1].append(c)

    return [''.join(word) for word in words]


str = "GeeksForGeeks"
print(camel_case_split(str))