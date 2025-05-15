
def create_polybius_square(key=None):
    """
    Generates a 5x5 Polybius square. Optionally shuffles using a keyword.
    
    Args:
        key (str, optional): Keyword to shuffle the alphabet. Defaults to None.
    
    Returns:
        list: 5x5 Polybius square
    """
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    if key:
        # Remove duplicate letters and non-alphabetic characters
        key = "".join([c.upper() for c in key if c.isalpha()])
        key = "".join(dict.fromkeys(key.upper()))  # Remove duplicates
        # Replace J with I in key to maintain 25-letter alphabet
        key = key.replace("J", "I")
        # Append remaining alphabet letters
        alphabet = key + "".join([c for c in alphabet if c not in key])
    
    # Convert into 5x5 grid
    square = [list(alphabet[i*5:(i+1)*5]) for i in range(5)]
    return square

def bifid_encrypt(plaintext, square, padding='X'):
    """
    Encrypts plaintext using the Bifid Cipher.
    
    Args:
        plaintext (str): Message to encrypt
        square (list): Polybius square
        padding (str, optional): Character for odd-length padding. Defaults to 'X'.
    
    Returns:
        str: Encrypted ciphertext
    """
    # Preprocess: uppercase, remove non-alphabet, handle J
    plaintext = "".join([c.upper() for c in plaintext if c.isalpha()])
    plaintext = plaintext.replace("J", "I")
    
    # Add padding if odd length
    if len(plaintext) % 2 != 0:
        plaintext += padding
    
    # Step 1: Convert letters to coordinates
    rows, cols = [], []
    for char in plaintext:
        for i, row in enumerate(square):
            if char in row:
                rows.append(i + 1)
                cols.append(row.index(char) + 1)
                break
    
    # Step 2: Combine and regroup
    combined = rows + cols
    ciphertext = ""
    for i in range(0, len(combined), 2):
        if i + 1 < len(combined):
            r, c = combined[i], combined[i + 1]
            ciphertext += square[r - 1][c - 1]
    
    return ciphertext

def bifid_decrypt(ciphertext, square):
    """
    Decrypts ciphertext using the Bifid Cipher.
    
    Args:
        ciphertext (str): Message to decrypt
        square (list): Polybius square
    
    Returns:
        str: Decrypted plaintext
    """
    # Step 1: Convert ciphertext to coordinates
    digits = []
    for char in ciphertext.upper():
        if not char.isalpha():
            continue
        for i, row in enumerate(square):
            if char in row:
                digits.append(i + 1)
                digits.append(row.index(char) + 1)
                break
    
    # Step 2: Split into rows and columns
    mid = len(digits) // 2
    rows = digits[:mid]
    cols = digits[mid:]
    
    # Step 3: Reconstruct plaintext
    plaintext = ""
    for r, c in zip(rows, cols):
        plaintext += square[r - 1][c - 1]
    
    return plaintext

def print_square(square):
    """Prints the Polybius square in readable format."""
    print("Polybius Square:")
    print("  1 2 3 4 5")
    for i, row in enumerate(square, 1):
        print(f"{i} {' '.join(row)}")

def main():
    """Interactive demo of the Bifid Cipher."""
    print("Bifid Cipher Implementation\n")
    
    # Square configuration
    use_key = input("Use custom key? (y/n): ").lower() == 'y'
    key = input("Enter keyword (leave blank for default): ").strip() if use_key else None
    square = create_polybius_square(key)
    print_square(square)
    
    # Encryption/Decryption loop
    while True:
        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Select operation: ")
        
        if choice == '1':
            plaintext = input("Enter plaintext: ")
            ciphertext = bifid_encrypt(plaintext, square)
            print(f"\nCiphertext: {ciphertext}")
        elif choice == '2':
            ciphertext = input("Enter ciphertext: ")
            plaintext = bifid_decrypt(ciphertext, square)
            print(f"\nPlaintext: {plaintext}")
        elif choice == '3':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()