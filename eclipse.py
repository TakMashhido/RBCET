class EclipseAttack:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def simulate_attack(self):
        """Simulate an eclipse attack by isolating the blockchain's peers."""
        print("Simulating eclipse attack...")

        # Replace all peers with a single malicious peer
        self.blockchain.peers = {"malicious_peer": True}

        # Validate peers to detect if the network has been isolated
        if not self.blockchain.validate_peers():
            print("Eclipse attack prevented: Peer validation failed.")
            return True

        # Check if only one peer exists and it's the malicious one
        if len(self.blockchain.peers) == 1 and "malicious_peer" in self.blockchain.peers:
            print("Eclipse attack succeeded: Malicious peer isolated the network.")
            return False

        print("Eclipse attack resisted: Network integrity maintained.")
        return True
