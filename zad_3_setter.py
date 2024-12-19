class IP:
    def __init__(self, ip):
        self.ip = self.__check_ip(ip)

    def __str__(self):
        return f"{self.ip[0]}.{self.ip[1]}.{self.ip[2]}.{self.ip[3]}"

    def __repr__(self):
        return f"IPAddress('<{self.ip[0]}.{self.ip[1]}.{self.ip[2]}.{self.ip[3]}>')"

    @staticmethod
    def __check_ip(ip):
        if isinstance(ip, str):
            ip = list(map(int, ip.split('.')))
        elif not isinstance(ip, (list, tuple)) or len(ip) != 4:
            raise ValueError("IP-адрес должен быть строкой из четырех чисел или списком/кортежем из четырех чисел.")

        if any(not (0 <= num <= 255) for num in ip):
            raise ValueError("Каждое число в IP-адресе должно быть в диапазоне от 0 до 255.")
        return ip


p1 = IP('123.34.56.78')
p2 = IP([34, 56, 78, 90])
p3  = IP((0, 255, 180, 170))

print(p1)
print(repr(p1))
print()
print(p2)
print(repr(p2))
print()
print(p3)
print(repr(p3))





