# TODO Найдите количество книг, которое можно разместить на дискете
disk_capacity_bite=float(1.44)*1024**2
pages=100
lines=50
symbol=25
one_symbol_bite=4
book_bite=pages*lines*symbol*one_symbol_bite
result=disk_capacity_bite//book_bite
print("Количество книг, помещающихся на дискету:",int(result) )
