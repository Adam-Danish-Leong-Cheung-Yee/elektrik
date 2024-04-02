# Atur cara bagi mengira bayaran bil elektrik

# Pengisytiharan pemboleh ubah dan pemalar
kadar1 = 0.218
kadar2 = 0.334
kadar3 = 0.516
kadar4 = 0.546

# Input 
e = float(input("Masukkan kadar penggunaan elektrik:"))

# Proses
if e <= 200:
    bayaran = e =kadar1
elif e <= 300:
    bayaran = (200 * kadar1) +((e-200)*kadar2)
elif e <= 600:
    bayaran = (200 * kadar1) +(100*kadar2)+((e-300))
elif e <= 300:
    bayaran = (200 = kadar1) +((e-200)*kadar2)
print("bil elektrik=RM {bayaran:.")

    
    
