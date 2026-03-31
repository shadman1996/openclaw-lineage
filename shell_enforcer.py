import hashlib
import subprocess
import json
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.exceptions import InvalidSignature

def verify_intent_and_execute(command: str, signature_hex: str, public_key, original_intent: dict, uuid_str: str):
    # Reconstruct the expected message hash
    intent_string = json.dumps(original_intent, sort_keys=True)
    message = f"{intent_string}{uuid_str}".encode('utf-8')
    message_hash = hashlib.sha256(message).digest()

    try:
        # Convert hex signature back to bytes and verify
        signature_bytes = bytes.fromhex(signature_hex)
        public_key.verify(signature_bytes, message_hash)
        
        print("[+] Lineage mathematically verified. Executing command...")
        # Execute command if lineage is proven
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout
        
    except InvalidSignature:
        return "[-] CRITICAL ERROR: Lineage verification failed. Orphaned intent detected. Execution blocked."
    except Exception as e:
        return f"[-] Error during verification: {str(e)}"
