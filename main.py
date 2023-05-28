from fastapi import FastAPI
from wallet import Wallet

app = FastAPI()
wallet_list = [
    {
        "id": 1,
        "brand": "boss",
        "colour": "black",
        "price": 500
    },
    {
        "id": 2,
        "brand": "don",
        "colour": "green",
        "price": 400
    },

]


@app.get("/")
async def wallet_shop():
    print(f"inside wallet_shop")
    return {"message": "Welcome to the wallet Shop"}


@app.get("/wallet")
async def get_wallet():
    print(f"Get all wallet list")
    return {"available _wallet": wallet_list}


@app.post("/new-wallet")
def add_new_wallet(wallet: Wallet):
    wallet_list.append(wallet.dict())
    return wallet_list


@app.get("/wallet/{id}")
def get_wallet_by_id(id: int):
    for wallet in wallet_list:
        if wallet['id'] == id:
            return wallet


@app.delete("/wallet/{id}")
def delete_wallet_by_id(id: int):
    for wallet in wallet_list:
        if wallet['id'] == id:
            wallet_id = wallet_list.index(wallet)
            wallet_list.pop(wallet_id)
            return wallet_list

# if __name__ == "__main__":
#     print(f"startup |")