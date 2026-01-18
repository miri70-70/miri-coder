import json
from difflib import get_close_matches as comes


def dowloand():
    with open('traning.json', 'r') as f:
        return json.load(f)

def write(veriables):
    with open('traning.json', 'w') as f:
        json.dump(veriables, f, indent=2)


def find_close(q,qs):
    smilars = comes(q, qs, n=1, cutoff=0.6)
    return smilars[0] if smilars else None


def finds(q, data):
    for i in data["sorular"]:
        if i["soru"] == q:
            return i["cevap"]



def chat_bot():
    veritabani = dowloand()


    while True:
        soru = input("Siz: ")
        if soru == 'enter':
            break

        gelen_sonuc = find_close(soru, [soru_cevaplar["soru"] for soru_cevaplar in veritabani["sorular"]])
        if gelen_sonuc:
            verilecek_cevap = finds(gelen_sonuc, veritabani)
            print(f"Bot: {verilecek_cevap}")
        else:
            print("Bot: i did not understand can you teach me? ")
            yeni_cavap = input("traning $ ")

            if yeni_cavap != 'geç':
                veritabani["sorular"].append({
                    "soru": soru,
                    "cevap": yeni_cavap
                })
                write(veritabani)
                print(f"Bot: Thanks i learnt that {yeni_cavap} ")

if __name__ == '__main__':
    chat_bot()
