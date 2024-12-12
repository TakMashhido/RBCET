class DoubleSpendingAttack:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def simulate_attack(self):
        """Simulate a double-spending attack."""
        sender = "Vehicle1"
        recipient1 = "Vehicle2"
        recipient2 = "Vehicle3"
        charge = 30  # Arbitrary charge value for the transactions

        # Add the first transaction (legitimate)
        try:
            self.blockchain.add_transaction(sender, recipient1, charge)
            print(f"Legitimate transaction added: {sender} -> {recipient1} | Charge: {charge}")
        except Exception as e:
            print(f"Failed to add legitimate transaction: {e}")
            return True

        # Attempt the double-spending transaction
        try:
            self.blockchain.add_transaction(sender, recipient2, charge)
            print(f"Malicious transaction added: {sender} -> {recipient2} | Charge: {charge}")
        except Exception as e:
            print(f"Double-spending attack prevented: {e}")
            return True

        return False
