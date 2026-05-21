# === Bitcoin Mining · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @MonitSharma.

# Import hashing library and timer
from hashlib import sha256
import time

# Set the maximum nonce attempts allowed
MAX_NONCE = 100000000000


# Hash a text string using SHA-256
def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


# Try nonces until the hash starts with enough zeros
def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = "0" * prefix_zeros
    for nonce in range(MAX_NONCE):
        # Build the block data string with current nonce
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        # Return the hash if it meets the difficulty target
        if new_hash.startswith(prefix_str):
            print(f"Yay! Successfully mined bitcoins with nonce value:{nonce}")
            return new_hash

    raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")


if __name__ == "__main__":
    # Define sample transactions for the block
    transactions = """
    Player1->Player2->200,
    Player3->Player4->450
    """
    # Set mining difficulty (more zeros = harder)
    difficulty = 6

    # Time how long mining takes
    start = time.time()
    print("start mining")
    new_hash = mine(
        5,
        transactions,
        "0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7",
        difficulty,
    )
    total_time = str((time.time() - start))
    print(f"end mining. Mining took: {total_time} seconds")
    print(new_hash)
