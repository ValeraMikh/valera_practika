suma_klienta = int(input())
if suma_klienta%10 != 0: 
    print 'Nekorektnaiy summa:', suma_klienta  
else:
    kolichestvo_1000=suma_klienta//1000
    print'kolichestvo 1000 grn.: ', kolichestvo_1000
    ostatok_ot_1000=suma_klienta%1000
    #print(ostatok_ot_1000)
    kolichestvo_500=ostatok_ot_1000//500
    print'kolichestvo 500 grn.: ', kolichestvo_500
    ostatok_ot_500=ostatok_ot_1000%500
    #print(ostatok_ot_500)
    kolichestvo_200=ostatok_ot_500//200
    print'kolichestvo 200 grn.: ', kolichestvo_200
    ostatok_ot_200=ostatok_ot_500%200
    #print(ostatok_ot_200)
    kolichestvo_100=ostatok_ot_200//100
    print'kolichestvo 100 grn.: ', kolichestvo_100
    ostatok_ot_100=ostatok_ot_200%100
    #print(ostatok_ot_100)
    kolichestvo_50=ostatok_ot_100//50
    print'kolichestvo 50 grn.: ', kolichestvo_50
    ostatok_ot_50=ostatok_ot_100%50
    #print(ostatok_ot_50)
    kolichestvo_20=ostatok_ot_50//20
    print'kolichestvo 20 grn.: ', kolichestvo_20
    ostatok_ot_20=ostatok_ot_50%20
    #print(ostatok_ot_20)
    kolichestvo_10=ostatok_ot_20//10
    print'kolichestvo 10 grn.: ', kolichestvo_10
    ostatok_ot_10=ostatok_ot_20%10
    #print(ostatok_ot_10)
