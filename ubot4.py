from pyrogram import Client, filters, idle
import pickle
import time

group =  -1002133302351
channel = -1001639582891


apiId =27208665 # //
apiHash ="64518c75c44675eb1c8066a349fe83d8" # //
bot_n = "4"

app = Client("ubot4",
                api_id=apiId, api_hash=apiHash)

@app.on_message()
def from_ch(client,message):

    if message.chat.id == channel:
        f = open("./g0", "rb")
        gc = pickle.load(f)
        f.close()
        fm = open("./g0m", "rb")
        gm = pickle.load(fm)
        fm.close()

        if gc == bot_n and str(message.id) != gm:
            f = open("./g0", "wb")
            pickle.dump("1", f)
            f.close()
            fm = open("./g0m", "wb")
            pickle.dump(str(message.id), fm)
            fm.close()
            message.copy(group)
            print("message g0")


app.run()
