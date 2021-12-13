#Pembukaan
print("Hallo Selamat malam, selamat datang di Quiz Matematika dasar 1")
nama = input("Silahkan Masukan Nama kamu :")
NIM = input("Silahkan Masukan NIM kamu :")
print(f'Hallo {nama} ({NIM}) pada quiz hari ini kamu akan mengerjakan 3 soal')

print ("Apakah kamu siap Mengerjakan Quiz pada hari ini ? jika siap ketik YES, jika tidak ketik NO")  
while True:
    mulai = str(input(""))
    if mulai == str('YES') or mulai == str('yes') or mulai == str('Yes'):
        print("Selamat Mengerjakan")
        break
    elif mulai == str('NO') or mulai == str('No') or mulai == str('no'):
        print("silahkan persiapkan diri terlebih dahulu")
        exit()
    else:
        print("silahkan pilih jawaban antara YES dan NO")
        continue

#List pertanyaan
def main():
    score = 0
    #Pertanyaan nomor
    while True:
        print (" ")
        print("Pertanyaan Nomor 1")
        QuizA = str(input("1. 1+1 =" ))
        if QuizA == str('2'):
            print("Selamat kamu benar")
            score += 1
            break
        else:
            print("Kamu salah silahkan coba lagi")
            continue
    
    #Pertanyaan nomor 2
    while True:
        print (" ")
        print("Pertanyaan Nomor 2")
        QuizA = int(input("2. 2+2 =" ))
        if QuizA == int('4'):
            print("Selamat kamu benar")
            score += 1
            break
        else:
            print("Kamu salah silahkan coba lagi")
            continue
    
    #Pertanyaan nomor 3
    while True:
        print (" ")
        print("Pertanyaan Nomor 3")
        QuizA = int(input("3. 3+3 =" ))
        if QuizA == int('6'):
            print("Selamat kamu benar")
            score += 1
            break
        else:
            print("Kamu salah silahkan coba lagi")
            continue

    #END
    print("")
    print("Selamat kamu telah menyelesaikan Quiz matematika dasar 1 pada malam hari ini")
    print("Total score kamu adalah =", score)

main()

