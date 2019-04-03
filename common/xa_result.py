#coding:utf-8
from flask import jsonify

#平台账号不存在或被禁用 10010
#参数错误  10020
#验证签名错误  10030
#无权访问,未提供token  10040
#无权访问，无效的token  10050
#无权访问，token过期    10060
#未提供refreshToken    10070
#无效的refreshToken    10080
#参数错误   10090


success_res = dict(code=1)
error_res = dict()


class XaResult(object):
    @staticmethod
    def success(data=None):
        success_res['data'] = data
        return jsonify(success_res)

    @staticmethod
    def error(code, msg):
        error_res['code'] = code
        error_res['msg'] = msg
        return jsonify(error_res)
