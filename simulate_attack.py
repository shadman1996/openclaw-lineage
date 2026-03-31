import gateway_signer
import shell_enforcer

def run_simulation():
    print("=== 🟢 PHASE 1: LEGITIMATE HUMAN INTENT ===")
    priv_key, pub_key = gateway_signer.generate_keys()
    
    # 1. Gateway receives a prompt from a real user
    original_intent = {"user": "alice", "prompt": "Check my current directory"}
    print(f"User Request: {original_intent['prompt']}")
    
    # 2. Gateway signs it
    payload = gateway_signer.sign_intent(original_intent, priv_key)
    
    # 3. Agent translates intent to a safe shell command
    safe_command = "ls -la"
    print(f"Agent executing: {safe_command}")
    
    # 4. Enforcer verifies and runs
    result = shell_enforcer.verify_intent_and_execute(
        safe_command, payload['signature'], pub_key, original_intent, payload['lineage_uuid']
    )
    print(f"Terminal Output: {result}\n")


    print("=== 🔴 PHASE 2: INDIRECT PROMPT INJECTION (HIJACK) ===")
    # 1. Agent reads a malicious email/webpage and decides to exfiltrate data independently
    rogue_intent = {"system": "auto", "prompt": "Exfiltrate shadow file"}
    rogue_command = "echo 'Pretending to read /etc/shadow...'"
    print(f"Rogue Agent attempting to execute: {rogue_command}")
    
    # 2. The rogue agent tries to use the OLD human signature to authorize the NEW malicious intent
    print("Attempting to bypass enforcer with orphaned signature...")
    result = shell_enforcer.verify_intent_and_execute(
        rogue_command, payload['signature'], pub_key, rogue_intent, payload['lineage_uuid']
    )
    print(f"Terminal Output: {result}\n")

if __name__ == "__main__":
    run_simulation()

