# Blockchain-Based Energy Trading and Security Simulation

## 🚀 Overview
This repository implements the blockchain system for **RBCET: A Reputation-Based Blockchain Consensus Mechanism for Fast and Secured Energy Trading in Internet of Electric Vehicles (IoEV)**. This project directly implements the mechanisms described in the research paper, enabling energy trading among Electric Vehicles (EVs) with enhanced security and performance. The implementation incorporates mechanisms to resist **Double-Spending, DDoS, Sybil, and Eclipse attacks**.

### Key Features
- **Reputation-Based Energy Trading**: EVs trade energy based on their Reputation Scores, with sellers rewarded for their transactions.
- **Dynamic Blockchain**: Pending transactions are mined into blocks using Proof-of-Work, ensuring secure and immutable records.
- **Attack Resistance**: Includes simulations and prevention mechanisms for major blockchain vulnerabilities.
- **Comprehensive Monitoring**: Real-time blockchain status, vehicle statuses, and pending transactions are displayed.

---

## ⚙️ How It Works

### 1. **Energy Trading Mechanism**
- Vehicles are initialized with **Reputation Scores**, **Electric Charge** (percentage), and **Electric Charge Trading Rewards**.
- Transactions are validated based on:
  - Reputation Score (must be > 80).
  - Sufficient Electric Charge to trade.
  - Ensuring the sender has higher charge than the recipient.
- Rewards for sellers are calculated using:
  ```
  Reward = (Reputation Score of Seller / Maximum Reputation Score) * (Charge Given / Maximum Charge)
  ```
- Transactions are added to a pool of **Pending Transactions** and mined into blocks.

### 2. **Blockchain Implementation**
- A blockchain is initialized with a **Genesis Block** (empty transaction block).
- Each block includes:
  - **Index**
  - **Hash**
  - **Previous Hash**
  - **Transactions**
  - **Nonce** 
- The system ensures:
  - **Integrity**: Blocks are validated with hashes.
  - **Efficiency**: Mining occurs only if there are pending transactions.

### 3. **Attack Simulations**
#### 🛡️ Security Mechanisms:
- **Double-Spending Attack**:
  - Validates pending transactions to detect duplicate spending by the same sender.
- **DDoS Attack**:
  - Implements rate limiting (max 10 transactions per 5 seconds per sender).
- **Sybil Attack**:
  - Detects and rejects nodes marked as invalid.
- **Eclipse Attack**:
  - Validates peers and prevents isolation by malicious nodes.

### 4. **Monitoring System**
The `monitor.py` tool provides real-time visibility into:
- **Blockchain Details**: Block hashes, transaction counts, and contents.
- **Vehicle Status**: Reputation Scores, Electric Charge, and Trading Rewards.
- **Pending Transactions**: Displays transactions awaiting mining.

---

## 🗂️ File Structure

| File                   | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| `blockchain.py`        | Core blockchain implementation, including mining and transaction validation.|
| `monitor.py`           | Real-time monitoring of the blockchain, vehicles, and pending transactions.|
| `main.py`              | Simulates energy trading with random transactions and block mining.        |
| `simulate_attacks.py`  | Simulates and resists Double-Spending, DDoS, Sybil, and Eclipse attacks.    |
| `vehicles.txt`         | Input file containing initial vehicle data.                                |
| `ddos.py`              | DDoS attack simulation.                                                    |
| `double_spending.py`   | Double-spending attack simulation.                                         |
| `eclipse.py`           | Eclipse attack simulation.                                                 |
| `sybil.py`             | Sybil attack simulation.                                                   |

---

## 🛠️ Installation and Setup

### Prerequisites
- Python 3.8+

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/TakMashhido/RBCET.git
   cd rbcet-energy-trading
   ```

2. Ensure `vehicles.txt` is present with vehicle data in the format:
   ```
   Vehicle1,85,60,0
   Vehicle2,90,40,0
   Vehicle3,95,30,0
   ```

---

## 🚦 Usage

### 1. **Run the Blockchain System**
Simulate energy trading and monitor the blockchain:
```bash
python main.py
```

### 2. **Simulate Security Attacks**
Test the blockchain's resistance to common attacks:
```bash
python simulate_attacks.py
```

---

## 📊 Output Examples

### Blockchain Monitor Output
```text
=== Blockchain Monitor ===

[Blockchain Details]
Block 0:
  Hash: abc123...
  Previous Hash: 0
  Transactions (0):

Block 1:
  Hash: def456...
  Previous Hash: abc123...
  Transactions (2):
    From: Vehicle1 | To: Vehicle2 | Electric Charge: 20 | Trading Reward: 1.8
    From: Vehicle3 | To: Vehicle4 | Electric Charge: 15 | Trading Reward: 1.5

[Vehicle Status]
  Vehicle1: Reputation Score: 85, Electric Charge: 60, Electric Charge Trading Reward: 1.8
  Vehicle2: Reputation Score: 90, Electric Charge: 80, Electric Charge Trading Reward: 0.0
  Vehicle3: Reputation Score: 95, Electric Charge: 15, Electric Charge Trading Reward: 1.5

[Pending Transactions]
  From: Vehicle5 | To: Vehicle6 | Electric Charge: 10 | Trading Reward: 0.9

=========================
```

### Attack Simulation Output
```text
[Simulating Double-Spending Attack]
Legitimate transaction added: Vehicle1 -> Vehicle2 | Charge: 30
Double-spending attack prevented: Duplicate transaction detected.
Double-Spending Attack Resisted.

[Simulating DDoS Attack]
Transaction 1: Vehicle3 -> Vehicle4 | Electric Charge: 10
Transaction 2 failed: Rate limit exceeded. Request dropped.
DDoS Attack Simulation Completed.

[Simulating Eclipse Attack]
Eclipse attack detected: Network isolation or insufficient peers.
Eclipse Attack Resisted.

[Simulating Sybil Attack]
Node sybil1 rejected.
Node sybil2 rejected.
Sybil Attack Resisted.
```

---

## 🔒 Security Highlights
- **Rate Limiting**: Protects against transaction spamming (DDoS).
- **Transaction Validation**: Prevents double-spending and ensures legitimate trades.
- **Peer Validation**: Detects malicious nodes and ensures network integrity.
- **Reputation-Based Eligibility**: Only trusted nodes participate in trading.

---

<!-- ## 📚 References
- Amritesh Kumar et al., *"RBCET: A Reputation-Based Blockchain Consensus Mechanism for Fast and Secured Energy Trading in Internet of Electric Vehicles (IoEV)",* IEEE Transactions on Consumer Electronics, 2024. -->

---

## 📈 Future Enhancements
- Integration of cryptographic privacy mechanisms for transactions.
- Expansion to larger networks with dynamic peer-to-peer interactions.
- Implementation of machine learning for adaptive Reputation Score adjustments.

---

## 🤝 Contributing
Feel free to fork this repository and submit pull requests for improvements or additional features.

---

## 📜 License
This project is licensed under the MIT License. See `LICENSE` for more details.