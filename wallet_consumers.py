from threading import Thread
from infrastructure.create_new_wallet_listener import CreateNewWalletListener
from infrastructure.set_money_in_account_listener import SetMoneyAccountListener

def start_consumer():
    Thread(target=SetMoneyAccountListener).start()
    Thread(target=CreateNewWalletListener).start()


if __name__ == "__main__":
    start_consumer()
