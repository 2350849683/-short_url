from app.service import service
from app.models import url,url_index
from app import db,create_app
from flask import request, redirect
from sqlalchemy.orm import sessionmaker
ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
app = create_app()
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


def get_long_url(token):
    obj = url.query.filter_by(short_url=token).first()
    if not obj:
        return None

    return obj.long_url
@service.route('/<token>')
def long_url(token):
    url = get_long_url(token)
    if not url:
        return "参数错误"

    return redirect(url)  # 我这里简单的实现，返回字符串ok，你需要根据token从url表里查出对应的长地址，并进行302跳转

def get_bohao_index():
    user1 = url_index(index=0)
    db.session.add(user1)
    db.session.commit()
    return user1.id
@service.route('/short_url', methods=['POST'])
def short_url():
    """
    你需要从url_index 表里获得最新的可用的index,根据这个index生成短地址，同时，你需要将
    url_index 里的index 增加1 ，这样下一次请求时，就可以获得最新的可用的index
    :param token:
    :return:
    """
    url1 = request.get_json()["url"]
    index=get_bohao_index()
    token = base62_encode(index)
    user2 = url(short_url=token, long_url=url1)
    db.session.add(user2)
    db.session.commit()
    return 'http://127.0.0.1:9000/{token}'.format(token=token)
