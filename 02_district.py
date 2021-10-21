# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# from district.central_street import house1
# from district.central_street import house2
# from district.soviet_street import house1
# from district.soviet_street import house2
# import district.central_street.house1.room1
# import district.central_street.house1.room2
# import district.central_street.house2.room1
# import district.central_street.house2.room2
# import district.soviet_street.house1.room1
# import district.soviet_street.house1.room2
# import district.soviet_street.house2.room1
# import district.soviet_street.house2.room2
from district.central_street.house1.room1 import folks as c1h1r1
from district.central_street.house1.room2 import folks as c1h1r2
from district.central_street.house2.room1 import folks as c1h2r1
from district.central_street.house2.room2 import folks as c1h2r2
from district.soviet_street.house1.room1 import folks as s1h1r1
from district.soviet_street.house1.room2 import folks as s1h1r2
from district.soviet_street.house2.room1 import folks as s1h2r1
from district.soviet_street.house2.room2 import folks as s1h2r2

print(c1h1r1 + c1h1r2 + c1h2r1 + c1h2r2 + s1h1r1 + s1h1r2 + s1h2r1 + s1h2r2)