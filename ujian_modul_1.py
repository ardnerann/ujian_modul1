# no 1
# principal = int(input('enter your principal: '))
# interest = float(input('enter the bank interest: '))
# tax = float(input('enter the amount of tax: '))
# desired = int(input('enter your desired return: '))

# tax_interest = tax * interest * principal
# interest_principal = interest * principal

# import math


# years = (desired - principal) / (interest_principal - tax_interest)



# print('you will get ' + str(desired) + ' after ' + str(math.ceil(years)) + ' years ')

# # no 2 

# import math
# total_angka = int(input('masukkan angka: '))
# if total_angka < 100 :
#     puluhan = str(math.floor(total_angka/10)) + '0'
#     puluhan_int = int(puluhan)
#     satuan = str(total_angka - puluhan_int)
#     print(str(puluhan) + ' + ' + str(satuan))
# elif total_angka >= 10000:
#     puluh_ribuan = str(math.floor(total_angka/10000)) + '0000'
#     puluh_ribuanint = int(puluh_ribuan)
#     ribuan = str((total_angka - puluh_ribuanint)//1000) + '000'
#     ratusan = str((total_angka - puluh_ribuanint - int(ribuan))//100) + '00'
#     puluhan = str((total_angka - puluh_ribuanint - int(ribuan) - int(ratusan))//10) + '0'
#     satuan = str((total_angka - puluh_ribuanint - int(ribuan) - int(ratusan) - int(puluhan)))
#     print(str(puluh_ribuan) + ' + ' + str(ribuan) + ' + ' + str(ratusan) + ' + ' + str(puluhan) + ' + ' + str(satuan))
# else:
#     print('wrong number')

# # no 3

# z=''
# for item in range(3):
#     for item1 in range(6):
#         if item1 >= 4:
#             z += '*'
#         else:
#             z += ' '
#     z += '\n'
# for item in range(3):
#     for item1 in range(6+2):
#         if item1 >= 2:
#             z += '*'
#         else:
#             z += ' '

#     z += '\n'
# for item in range(3):
#     for item1 in range(2+4+4):
#         z += '*'
#     z += '\n'
# print(z)
