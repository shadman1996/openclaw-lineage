import hashlib
import uuid
import json
from cryptography.hazmat.primitives.asymmetric import ed25519

def generate_keys():
    # Generate the private/public key pair using the modern library
    private_key = ed25519.Ed25519PrivateKey.generate()
    public_key = private_key.public_key()
    return private_key, public_key

def sign_intent(intent_payload: dict, private_key):
    # 1. Generate a universally unique identifier for this specific request
    lineage_uuid = str(uuid.uuid4())
    
    # 2. Reconstruct the string and hash it
    intent_string = json.dumps(intent_payload, sort_keys=True)
    message = f"{intent_string}{lineage_uuid}".encode('utf-8')
    message_hash = hashlib.sha256(message).digest()
    
    # 3. Sign the hashed intent
    signature = private_key.sign(message_hash)
    
    print(f"[*] Intent Signed. Lineage UUID: {lineage_uuid}")
    
    return {
        "intent": intent_payload,
        "lineage_uuid": lineage_uuid,
        "signature": signature.hex()
    }

if __name__ == "__main__":
    # Quick test execution
    priv_key, pub_key = generate_keys()
    sample_intent = {"action": "scan_network", "target": "10.0.0.1"}
    signed_payload = sign_intent(sample_intent, priv_key)
    print(f"[*] Generated Payload: {signed_payload}")
