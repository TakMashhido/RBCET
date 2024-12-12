class BlockchainMonitor:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def display_chain(self):
        """Displays the blockchain with transaction details."""
        print("\n[Blockchain Details]")
        for block in self.blockchain.chain:
            print(f"Block {block.index}:")
            print(f"  Hash: {block.hash}")
            print(f"  Previous Hash: {block.previous_hash}")
            print(f"  Transactions ({len(block.transactions)}):")
            for tx in block.transactions:
                print(f"    From: {tx.get('from')} | To: {tx.get('to')} | Electric Charge: {tx.get('Electric Charge')} | Trading Reward: {tx.get('Trading Reward')}")
        print("\n")

    def display_vehicle_status(self):
        """Display the current status of all vehicles."""
        print("\n[Vehicle Status]")
        for vehicle, status in self.blockchain.get_vehicle_status().items():
            print(f"  {vehicle}: Reputation Score: {status['Reputation Score']}, Electric Charge: {status['Electric Charge']}, Electric Charge Trading Reward: {status['Electric Charge Trading Reward']}")

    def display_pending_transactions(self):
        """Display the current pending transactions."""
        print("\n[Pending Transactions]")
        if not self.blockchain.pending_transactions:
            print("  No pending transactions.")
        else:
            for tx in self.blockchain.pending_transactions:
                print(f"  From: {tx.get('from')} | To: {tx.get('to')} | Electric Charge: {tx.get('Electric Charge')} | Trading Reward: {tx.get('Trading Reward')}")

    def monitor_chain(self):
        """Runs all monitoring checks and displays detailed information."""
        print("\n=== Blockchain Monitor ===")
        self.display_chain()
        self.display_vehicle_status()
        self.display_pending_transactions()
        print("\n=========================\n")
