str = 'X-DSPAM-Confidence:0.8475'
vitri = str.find(':')
print(vitri)
cat_chuoi = str[vitri + 1 : ]
print(cat_chuoi, type(cat_chuoi))
ket_qua = float(cat_chuoi)
print(ket_qua, type(ket_qua))