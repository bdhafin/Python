#bentuk dasar dari string
text1 = 'jalan - jalan di hari ahad'

#menyambung jika memakai kutip 1 dan ada kutip lain di dalam nya
text2 = 'jalan - jalan di hari jum\'at'

#Cara kedua menyambung jika ada kutip 1 di dalam kata
text3 = "jalan - jalan di hari jum'at"

text4 = 'dhafin berkata. "kemarin kemana bro?"'

#Cara menyambung bila ada kutip 2 di dalam kutip 2
text5 = "rizqullah menjawab, \"jalan - jalan bro\" "

#cara membuat baris baru
text6 = 'dhafin: "kemarin kemana bro?" \nrizqullah: "jalan - jalan bro" '

#Cara membuat string multi baris (memakai kutip 3)
text7 = """
dhafin: "kemarin kemana bro?"
rizqullah: "jalan - jalan bro"
dhafin: "jalan - jalan kemana bro?"
rizqullah: "ke Bandung bro"
"""
#untuk membuat path (raw string)
text8 = r'C:\ndhafin'

print(text8)

#cara membuat string yang sama berkali kali
print(5 * "wk")

#cara menyambung 2 string atau lebih
print('dhafin' 'rizqullah')
print(text1 + text2)
