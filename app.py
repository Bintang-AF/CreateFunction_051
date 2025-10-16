#input 
try :
    suhu = float(input ("inputkan besaran suhu :"))
except ValueError as e :
    print("error :", e)
    exit()
format_suhu = input ("format suhu (c/f/k) :")
konversi_suhu = input ("konversi suhu (c/f/k) :")
hasil = ""

#x = suhu
#y = format suhu
def konversisuhu(x, y, z) :
    global hasil
    #cek kondisi untuk celsius ke fahrenheit
    if y == 'c' and z == 'f' :
        f = (9/5) * x + 32
        hasil = f'{f}{z.upper()}'
#cek kondisi utk celcius ke kevin

    elif y == 'c' and z == 'k' :
        k = x + 273.15      
        hasil = f'{k}{z.upper()}'
    elif y == 'f' and z == 'c' :
        c = (x - 32) * (5/9)
        hasil = f'{c}{z.upper()}'
    elif y  == 'f' and z == 'k' :
        k = (5/9) * x + 459.67
        hasil = f'{k}{z.upper()}'
    elif y == 'k' and z == 'c' :
        c = x - 273.15
    elif y == 'k' and z == 'f' :
        f = (x - 273.15) * (9/5) + 32
        hasil  = f'{f}{z.upper()}'
    else :
        hasil = "konversi nilai tidak valid "

if (format_suhu == konversi_suhu) :
    hasil = f'{suhu} {format_suhu.upper()}'
else :  
    konversisuhu(suhu, format_suhu, konversi_suhu)

print(hasil)
