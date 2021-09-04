from app.models import url,url_index
from app import db
import redis   # 导入redis 模块



cot={"max":None,"index":None}
ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
r = redis.Redis(host='localhost', port=6500, decode_responses=True)

def base62_encode(num, alphabet=ALPHABET):
    """
    10进制转62进制
    """
    if (num == 0):
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        rem = num % base
        num = num // base
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)

def get_max_index():
    '''
    获取拨号  +100
    :return: 最大拨号
    '''

    return r.incr( "index", amount=100)



def add_url(url1):
    '''

    :param url1: 长地址
    :return:  短地址
    '''
    if cot["max"] is None or cot["max"]+1==cot["index"]:  #判断还有没有拨号
        cot["max"]=get_max_index()
        cot["index"]=cot["max"]-100

    cot["index"]+=1
    token = base62_encode(cot["index"])
    ot= url(short_url=token, long_url=url1)  #长短映射
    db.session.add(ot)
    db.session.commit()
    return f'http://127.0.0.1:9000/{token}'

