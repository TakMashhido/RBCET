from blockchain import Blockchain
from monitor import BlockchainMonitor
from double_spending import DoubleSpendingAttack
from ddos import DDoSAttack
from eclipse import EclipseAttack
from sybil import SybilAttack


def simulate_double_spending(blockchain):
    print("\n[Simulating Double-Spending Attack]")
    attack = DoubleSpendingAttack(blockchain)
    if attack.simulate_attack():
        print("Double-Spending Attack Resisted.")
    else:
        print("Double-Spending Attack Succeeded.")


def simulate_ddos(blockchain):
    print("\n[Simulating DDoS Attack]")
    attack = DDoSAttack(blockchain)
    attack.simulate_attack()
    print("DDoS Attack Simulation Completed.")


def simulate_eclipse(blockchain):
    print("\n[Simulating Eclipse Attack]")
    attack = EclipseAttack(blockchain)
    if attack.simulate_attack():
        print("Eclipse Attack Resisted.")
    else:
        print("Eclipse Attack Succeeded.")


def simulate_sybil(blockchain):
    print("\n[Simulating Sybil Attack]")
    attack = SybilAttack(blockchain)
    if attack.simulate_attack():
        print("Sybil Attack Resisted.")
    else:
        print("Sybil Attack Succeeded.")


def main():
    print("Initializing blockchain from file...")
    blockchain = Blockchain("vehicles.txt")
    monitor = BlockchainMonitor(blockchain)

    print("\n[Initial Blockchain State]")
    monitor.monitor_chain()

    # Simulate attacks
    simulate_double_spending(blockchain)
    monitor.monitor_chain()

    simulate_ddos(blockchain)
    monitor.monitor_chain()

    simulate_eclipse(blockchain)
    monitor.monitor_chain()

    simulate_sybil(blockchain)
    monitor.monitor_chain()

    print("\n[Final Blockchain State]")
    monitor.monitor_chain()


if __name__ == "__main__":
    main()
