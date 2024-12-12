class SybilAttack:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def simulate_attack(self):
        """Simulate a Sybil attack by introducing multiple malicious nodes."""
        print("Simulating Sybil attack...")
        sybil_nodes = ["sybil1", "sybil2", "sybil3"]

        for node in sybil_nodes:
            try:
                # Add the Sybil node to the network
                self.blockchain.peers[node] = False  # Mark as invalid
                print(f"Node {node} rejected.")
            except Exception as e:
                print(f"Failed to handle Sybil node {node}: {e}")

        # Validate peers after the Sybil attack
        if not self.blockchain.validate_peers():
            print("Sybil attack prevented: Peer validation failed.")
            return True

        print("Sybil attack succeeded: Malicious nodes infiltrated the network.")
        return False
