import locale
locale.setlocale(locale.LC_MONETARY)
price_per_unit = locale.currency(2)
money = total_size * price_per_unit
print(money)
