satu = 1;
dua = 2;
tiga = 3;
empat = 4;
lima = 5;
enam = 6;
tujuh = 7;
delapan = 8;
sembilan = 9;

loop = 1

import time
start_time = time.time()
while loop == 1:
    print "PROGRAM OPERASI ARITMATIKA LEBIH DARI 1 OPERATOR "
    print (nama)
    print (npm)
    print (kelas)
    print
    print ("Example - (satu + lima) x (Dua / Satu)")
    print "Masukan operan dalam format kata (angka) seperti inputan di atas"
    pilih = 1;

    if pilih == 1:
        operan_a = input("Input :")
        operan_b = input("+ ")
        operan_c = input("x ")
        operan_d = input("/ ")
        hasil = (operan_a + operan_b) * (operan_c / operan_d)
        totalTime = format((time.time() - start_time), '.5f')
        print "hasil dari", "(",operan_a, "+", operan_b,")", "*", "(",operan_c, "/", operan_d,")", "adalah", hasil, ", dengan delta t :", totalTime

        loop = 0;
