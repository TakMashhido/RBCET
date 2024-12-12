import time

class DDoSAttack:
    def __init__(self, blockchain):
        self.blockchain = blockchain
        self.rate_limit = 10  # Maximum number of transactions allowed in a short period

    def simulate_attack(self):
        """Simulate a DDoS attack by overwhelming the blockchain with transactions."""
        sender = "Vehicle1"
        recipient = "Vehicle2"
        charge = 5  # Small charge value for the attack
        start_time = time.time()

        print("Simulating DDoS attack...")
        for i in range(50):  # Attempt to flood the blockchain with 50 transactions
            try:
                if i >= self.rate_limit and time.time() - start_time < 5:
                    raise Exception("Rate limit exceeded. Request dropped.")
                self.blockchain.add_transaction(sender, recipient, charge)
                print(f"Transaction {i + 1}: {sender} -> {recipient} | Charge: {charge}")
            except Exception as e:
                print(f"Transaction {i + 1} failed: {e}")
