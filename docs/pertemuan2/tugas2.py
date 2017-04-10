graph = {
             'Rumah': ['Brebes'],
             'Brebes': ['Tegal'],
             'Tegal': ['Cirebon'],
             'Cirebon': ['Sumedang'],
             'Sumedang': ['Jatinangor'],
             'Jatinangor': ['LeuwiPanjang'],
             'LeuwiPanjang': ['PasarBaru'],
             'PasarBaru': ['Sariasih'],
             'Sariasih': ['Sarijadi'],
             'Sarijadi': ['Kost'],
             'Kost': ['Sarijadi','Sariasih']
        }

def mencari_jalur_terpendek(graph, jalanawal, jalantujuan, jalur=[]):
        jalur = jalur + [jalanawal]
        if jalanawal == jalantujuan:
            return jalur
            if not graph.has_key(jalanawal):
                    return None
        jalurpendek = None
        for node in graph[jalanawal]:
            if node not in jalur:
                newjalur = mencari_jalur_terpendek(graph, node, jalantujuan, jalur)
                if newjalur:
                    if not jalurpendek or len(newjalur) < len(jalurpendek):
                        jalurpendek = newjalur
        return jalurpendek
print("Jalur Jalan Raya Dari Rumah Sampai Kost")
print("(Rumah, Brebes, Tegal, Cirebon, Sumedang, Jatinangor)")
print("(LeuwiPanjang, PasarBaru, Sariasih, Sarijadi, Kost)")
print("\n")
jalanawal = raw_input("Masukan jalanawal : ")
jalantujuan = raw_input("Masukan jalantujuan : ")
hasil = mencari_jalur_terpendek(graph, jalanawal, jalantujuan, jalur=[])
print "Jalur Terpendek", hasil