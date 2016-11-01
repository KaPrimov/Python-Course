
ORD_DIFF = ord('Z') - ord('A') + 1

cypher_key = input()
user_input = input()

if cypher_key.isdigit() and user_input:
    cypher_key = int(cypher_key)
    result = []
    for letter in user_input:
        letter_ord = ord(letter)
        if ord('A') <= letter_ord <= ord('Z'):
            encrypted_ord = letter_ord + cypher_key
            if encrypted_ord > ord('Z'):
                encrypted_ord = encrypted_ord - ORD_DIFF
            result.append(chr(encrypted_ord))
        else:
            result.append(letter)
    print(''.join(result))
else:
    print("INVALID INPUT")

