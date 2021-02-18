#Aureaninta TNKP (XI MIPA 5/06)

#dengan dictionary
vowels = 'aiueo'

ip_str = 'Halo nama saya Aureannta Talitha, saya sedang belajar python'

ip_str = ip_str.casefold()

count = {}.fromkeys(vowels,0)

for char in ip_str:
    if char in count:
        count[char] += 1

print(count)
