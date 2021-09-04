from app.service import service
from app.service.fun import add_url
from app.models import url
from app import db,create_app
from flask import request, redirect

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

    return redirect(url)


@service.route('/short_url', methods=['POST'])
def short_url():
    """
    你需要从url_index 表里获得最新的可用的index,根据这个index生成短地址，同时，你需要将
    url_index 里的index 增加1 ，这样下一次请求时，就可以获得最新的可用的index
    :param token:
    :return:
    """
    url1 = request.get_json()["url"]
    token= add_url(url1)
    return token
