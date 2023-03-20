def kembalian(harga, kembalian_tersedia):
    sisa = sum(kembalian_tersedia) - harga
    if sisa < 0:
        return "Loket tidak memiliki kembalian"
    elif sisa == 0:
        return "Tidak ada kembalian yang diperlukan"
    else:
        kembalian = []
        for uang in sorted(kembalian_tersedia, reverse=True):
            while sisa >= uang:
                kembalian.append(uang)
                sisa -= uang
        if sisa == 0:
            return "Kembalian: " + ' + '.join(map(str, kembalian))
        else:
            return "Loket tidak memiliki kembalian yang cukup"


# contoh penggunaan
kembalian_tersedia = [20, 20, 50, 5, 5, 100]
harga_tiket = 25
print(kembalian(harga_tiket, kembalian_tersedia))
