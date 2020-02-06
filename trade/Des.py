from Cryptodome.Cipher import DES

key = b'abcdefgh'  # 密钥 8位或16位,必须为bytes


def pad(text):
    """
    # 加密函数，如果text不是8的倍数【加密文本text必须为8的倍数！】，那就补足为8的倍数
    :param text:
    :return:
    """
    while len(text) % 8 != 0:
        text += ' '
    return text


des = DES.new(key, DES.MODE_ECB)  # 创建一个DES实例
text = 'Python rocks!'
padded_text = pad(text)
encrypted_text = des.encrypt(padded_text.encode('utf-8'))  # 加密
print(encrypted_text)
# rstrip(' ')返回从字符串末尾删除所有字符串的字符串(默认空白字符)的副本
plain_text = des.decrypt(encrypted_text).decode().rstrip(' ')  # 解密
print(plain_text)
#
