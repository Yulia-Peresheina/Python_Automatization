# В модуль с проверкой даты добавьте возможность запуска
# в терминале с передачей даты на проверку.

from Check_year_date import check_date
from sys import argv

print(check_date(argv[1]))
