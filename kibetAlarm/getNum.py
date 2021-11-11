
import uuid


if __name__ == '__main__':
    mac_num = hex(uuid.getnode()).replace('0x', '').upper()
    
    mac = '-'.join(mac_num[i: i + 2] for i in range(0, 11, 2))
    print(mac)
