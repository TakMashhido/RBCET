import random
from blockchain import Blockchain
from monitor import BlockchainMonitor


def add_random_transactions(blockchain, num_transactions=5):
    """Simulate random valid transactions with randomized charge values."""
    print(f"\n[Adding {num_transactions} Random Transactions]")
    vehicles = list(blockchain.get_vehicle_status().keys())
    for _ in range(num_transactions):
        sender = vehicles[random.randint(0, len(vehicles) - 1)]  # Random sender
        recipient = vehicles[random.randint(0, len(vehicles) - 1)]  # Random recipient
        while sender == recipient:  # Ensure sender and recipient are not the same
            recipient = vehicles[random.randint(0, len(vehicles) - 1)]
        charge = random.randint(5, 25)  # Random charge between 5 and 25

        try:
            blockchain.add_transaction(sender, recipient, charge)
            print(f"  Transaction Added: From {sender} to {recipient} | Electric Charge: {charge}")
        except Exception as e:
            print(f"  Failed to add transaction: {e}")


def main():
    print("Initializing blockchain from file...")
    blockchain = Blockchain("vehicles.txt")
    monitor = BlockchainMonitor(blockchain)

    print("\n[Initial Blockchain State]")
    monitor.monitor_chain()

    batch_size = 5  # Process transactions in batches of 5
    total_transactions = 15  # Total transactions to simulate

    for i in range(0, total_transactions, batch_size):
        add_random_transactions(blockchain, num_transactions=batch_size)

        # Only mine a block if there are pending transactions
        if blockchain.pending_transactions:
            print("\nMining Pending Transactions...")
            blockchain.mine_pending_transactions("Vehicle1")
            monitor.monitor_chain()
        else:
            print("\nNo pending transactions to mine.")

    print("\n[Final Blockchain State]")
    monitor.monitor_chain()


if __name__ == "__main__":
    main()
