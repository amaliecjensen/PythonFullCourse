import hashlib

# Tekststreng, der skal hashes
tekst = "Hello, World! ammalie"

# Opret en SHA-256 hash-objekt
hash_objekt = hashlib.sha3_384()

# Opdater hash-objektet med tekststrengen (skal være bytes)
hash_objekt.update(tekst.encode('utf-8'))

# Generer hashværdien i hexadecimal format
hash_vaerdi = hash_objekt.hexdigest()

print(f"Hashværdi for '{tekst}' er: {hash_vaerdi}")
