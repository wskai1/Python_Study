import requests


def test_crack_feedback(self):
    """
    反馈页面刷的测试
    :return:
    """
    url_para = {
        'proType': 5,
        'platType': 1,
        'referer': 'https://www.google.com/',
        'content': '看你们是否存在此漏洞',
        'tel': '123144',
        'email': 'adsf@11',
        'qq': '123544',
        'location': '北京市',
        'ip-location': '北京市',
        'ip-service': '联通',
    }

    post_url = 'http://x.xxx.xx/ugc/out/feedback/?act=add'

    res = requests.post(post_url, data=url_para)
    glog.debug(res.text)

