'''

Teste básico de list comprehension
'''

nums = [1,2,3,4,5]

dobro_impares = [n*2 for n in nums if n%2 == 1]

print(dobro_impares)