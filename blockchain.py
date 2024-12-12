import hashlib
import time


class Block:
    def __init__(self, index, previous_hash, transactions, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions if isinstance(transactions, list) else [transactions]
        self.timestamp = timestamp or time.time()
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.transactions}{self.timestamp}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        target = '0' * difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()


class Blockchain:
    def __init__(self, vehicles_file="vehicles.txt"):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4
        self.pending_transactions = []
        self.vehicles = self.initialize_vehicles_from_file(vehicles_file)
        self.peers = {}
        self.rate_limit = {}  # Rate-limiting data structure

    def initialize_vehicles_from_file(self, vehicles_file):
        """Initialize vehicles from the provided file."""
        vehicles = {}
        try:
            with open(vehicles_file, "r") as file:
                for line in file:
                    vehicle_data = line.strip().split(",")
                    if len(vehicle_data) != 4:
                        raise ValueError(f"Invalid vehicle data: {line}")
                    vehicle, reputation, charge, reward = vehicle_data
                    vehicles[vehicle] = {
                        "Reputation Score": int(reputation),
                        "Electric Charge": int(charge),
                        "Electric Charge Trading Reward": float(reward),
                    }
        except FileNotFoundError:
            raise FileNotFoundError(f"File {vehicles_file} not found.")
        return vehicles

    def create_genesis_block(self):
        """Create a genesis block with an empty transaction."""
        return Block(0, "0", [], time.time())

    def get_latest_block(self):
        return self.chain[-1]

    def calculate_reward(self, sender, charge):
        """Calculate the trading reward based on the reputation score and charge given."""
        max_reputation = max(vehicle["Reputation Score"] for vehicle in self.vehicles.values())
        max_charge = 100  # Electric charge is capped at 100
        sender_reputation = self.vehicles[sender]["Reputation Score"]

        reward = (sender_reputation / max_reputation) * (charge / max_charge)
        return reward

    def validate_peers(self):
        """Validate the peers to ensure no malicious nodes are present and the network isn't isolated."""
        if len(self.peers) <= 1:
            print("Eclipse attack detected: Network isolation or insufficient peers.")
            return False

        for peer, is_valid in self.peers.items():
            if not is_valid:
                print(f"Invalid peer detected: {peer}")
                return False

        print("All peers are valid.")
        return True


    def add_transaction(self, sender, recipient, charge):
        """Add a transaction between two vehicles."""
        # DDoS rate limiting
        if sender not in self.rate_limit:
            self.rate_limit[sender] = {"count": 0, "timestamp": time.time()}
        if time.time() - self.rate_limit[sender]["timestamp"] < 5:  # 5-second window
            if self.rate_limit[sender]["count"] >= 10:  # Maximum 10 transactions in 5 seconds
                raise ValueError("Rate limit exceeded for this sender.")
        else:
            # Reset the counter and timestamp
            self.rate_limit[sender]["count"] = 0
            self.rate_limit[sender]["timestamp"] = time.time()
        self.rate_limit[sender]["count"] += 1

        # Validate peers
        if sender in self.peers and not self.peers[sender]:
            raise ValueError(f"Transaction rejected: Invalid peer {sender}.")

        # Ensure double-spending is prevented
        for tx in self.pending_transactions:
            if tx["from"] == sender and tx["Electric Charge"] == charge:
                raise ValueError(f"Double-spending attempt detected for vehicle {sender}.")

        if not self.is_vehicle_eligible(sender):
            raise ValueError(f"Vehicle {sender} is not eligible to trade due to low Reputation Score.")
        if self.vehicles[sender]["Electric Charge"] < charge:
            raise ValueError(f"Vehicle {sender} does not have enough electric charge to trade.")
        if not (0 <= charge <= 100):
            raise ValueError("Electric charge must be between 0 and 100.")
        if self.vehicles[sender]["Electric Charge"] <= self.vehicles[recipient]["Electric Charge"]:
            raise ValueError(f"Vehicle {sender} cannot trade with Vehicle {recipient} as it has equal or lower charge.")

        # Deduct charge from sender
        self.vehicles[sender]["Electric Charge"] -= charge

        # Add charge to recipient
        self.vehicles[recipient]["Electric Charge"] = min(
            100, self.vehicles[recipient]["Electric Charge"] + charge
        )

        # Calculate reward for the sender
        reward = self.calculate_reward(sender, charge)

        # Add trading reward to sender's Electric Charge Trading Reward
        self.vehicles[sender]["Electric Charge Trading Reward"] += reward

        # Create the transaction
        transaction = {
            "from": sender,
            "to": recipient,
            "Electric Charge": charge,
            "Trading Reward": reward,
        }
        self.pending_transactions.append(transaction)

    def is_vehicle_eligible(self, vehicle):
        """Check if a vehicle's Reputation Score is greater than 80."""
        return self.vehicles[vehicle]["Reputation Score"] > 80

    def mine_pending_transactions(self, miner_address):
        """Mine the pending transactions into a new block."""
        if not self.pending_transactions:
            print("No transactions to mine.")
            return
        block = Block(len(self.chain), self.get_latest_block().hash, self.pending_transactions)
        block.mine_block(self.difficulty)
        self.chain.append(block)
        self.pending_transactions = []

    def get_vehicle_status(self):
        """Get the current status of all vehicles."""
        return self.vehicles

    def is_chain_valid(self):
        """Validate the integrity of the blockchain."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True
