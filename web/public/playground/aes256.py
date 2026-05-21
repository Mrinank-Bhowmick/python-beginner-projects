# === AES 256 Encryption and Decryption · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @oyeanmol.

# Import hashing and encryption libraries
import hashlib
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


# Encrypt plain text using a password
def encrypt(plain_text, password):
    if not password:
        raise ValueError("Password cannot be empty.")

    # Generate a random salt and derive a 256-bit key
    salt = get_random_bytes(AES.block_size)
    private_key = hashlib.scrypt(
        password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32
    )
    # Create AES cipher and encrypt the message
    cipher_config = AES.new(private_key, AES.MODE_GCM)
    cipher_text, tag = cipher_config.encrypt_and_digest(bytes(plain_text, "utf-8"))
    # Return all parts needed for decryption as base64 strings
    return {
        "cipher_text": b64encode(cipher_text).decode("utf-8"),
        "salt": b64encode(salt).decode("utf-8"),
        "nonce": b64encode(cipher_config.nonce).decode("utf-8"),
        "tag": b64encode(tag).decode("utf-8"),
    }


# Decrypt an encrypted dictionary back to plain text
def decrypt(enc_dict, password):
    if not password:
        raise ValueError("Password cannot be empty.")

    try:
        # Decode all base64 parts from the encrypted dict
        salt = b64decode(enc_dict["salt"])
        cipher_text = b64decode(enc_dict["cipher_text"])
        nonce = b64decode(enc_dict["nonce"])
        tag = b64decode(enc_dict["tag"])
        # Rebuild the key and decrypt the message
        private_key = hashlib.scrypt(
            password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32
        )
        cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)
        decrypted = cipher.decrypt_and_verify(cipher_text, tag)
        return decrypted.decode("utf-8")
    except (ValueError, KeyError) as e:
        raise ValueError("Invalid encrypted message format.") from e


def main():
    # Show the program title
    print("\t\tAES 256 Encryption and Decryption Algorithm")
    print("\t\t-------------------------------------------\n\n")
    # Ask the user to choose encrypt or decrypt
    x = input("Enter 1 to encrypt and 2 to decrypt: ")
    if x == "1":
        # Gather password and message, then encrypt
        password = input("Enter the Password: ")
        secret_mssg = input("\nEnter the Secret Message: ")

        encrypted = encrypt(secret_mssg, password)
        # Print each part of the encrypted result
        print("\n\nEncrypted:")
        print("---------------\n")
        for k, v in encrypted.items():
            print(f"{k}: {v}")

    elif x == "2":
        try:
            # Collect all encrypted parts from the user
            encrypted = {}
            encrypted["cipher_text"] = input("Enter the cipher text: ")
            encrypted["salt"] = input("Enter the salt: ")
            encrypted["nonce"] = input("Enter the nonce: ")
            encrypted["tag"] = input("Enter the tag: ")
            password = input("Enter the password: ")

            # Decrypt and display the original message
            decrypted = decrypt(encrypted, password)
            print("\n\nDecrypted:")
            print("-----------------\n")
            print(decrypted)
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
