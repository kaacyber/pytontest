def camel_case(string):
    # Pisahkan string menjadi kata-kata dengan memisahkan berdasarkan tanda - , _ , atau spasi
    words = string.replace('-', ' ').replace('_', ' ').split()

    # Ubah huruf pertama pada setiap kata menjadi huruf besar
    for i in range(len(words)):
        words[i] = words[i].capitalize()

    # Gabungkan semua kata menjadi satu string tanpa spasi
    camel_case_string = ''.join(words)

    # Ubah huruf pertama menjadi huruf kecil
    camel_case_string = camel_case_string[0].lower() + camel_case_string[1:]

    return camel_case_string


string_1 = "InI-aDalaH-sTrinG"
string_2 = "InI_aDalaH_sTrinG"
string_3 = "InI aDalaH sTrinG"

print(camel_case(string_1))  # Output: "iniAdalahString"
print(camel_case(string_2))  # Output: "iniAdalahString"
print(camel_case(string_3))  # Output: "iniAdalahString"
