import requests
import execjs
cookies = {
    '__bid_n': '187385d55219a699254207',
    'P_INFO': 'zawaludo@126.com|1680361713|0|mail126|00&99|null&null&null#gud&440100#10#0#0|&0|mail126|zawaludo@126.com',
    '_ntes_nnid': 'e320573ab9dcf82fee6ce0bd1fde46ec,1680829462419',
    '_ntes_nuid': 'e320573ab9dcf82fee6ce0bd1fde46ec',
    'NMTID': '00OUohNvG-YwixOHkjphD1aA8XEaIMAAAGHWT43ng',
    'WEVNSM': '1.0.0',
    'WNMCID': 'dqynhy.1680829463077.01.0',
    'WM_TID': 'YxDMEHuuqf9AEFUBVFaFahSqWDiMFV5d',
    'FPTOKEN': 'TEpkUNAlvL799rywt8p/wL+wbG3UFmPCbFrC15If76oI0WjsW/HPO/WO2QcAqOFiDgcjB4iT/tuNBG357ZCoDLUwUl3uE8KOA3MZAalIMQFAdWYrepeiOVcAqP2yiBjJoMsxLTI2+yBYhKPs5i2EPtR4ZZMAj3QJXPs0HblxaovvgTYrHmilWXM9DE7drNF3dYmOtZ8FT6mTBagVSK0vriYxAFwpwXJdVOj6H5hYiBfTSE5T06twUOv4X45kTfV21cNSSMY4/OLO+21y8E9xgFRSleQkFbO+AVj3fNxwht38wtgsYq/rblOd+4JjeP7u7PljS/Euiw66M6j1nxdoc1s3P5LlD17UyoUrLUwdqdZc2ce0JKYC2hTIPIPptfSn3cUIaGSopnHqJj/h/A/Zyw==|MruS1jHKnpk5EZtETC+sysjuswKYAkknLHPIxTGkGzI=|10|2233f5d8e7da6c6ae8b6e9d9c39fdd03',
    'JSESSIONID-WYYY': '%2Fhyyfb7gwZjJVISqZPHJkcdQ0R7FFJ1kG%2Bztl%5CKYS5%2Fquh%5CCalpmX%2Bkv7kInXgHOynRjGKxql57GKMY1lOQPqt6sUa6cH747DoeWUhYvHHOZ7ijmqqg5T9xOkfPe15Y1DrHxnNTst5EPrTFRmVOZc9IvoWURlFsjZXFlUtufemhlP3i3%3A1683041701991',
    '_iuqxldmzr_': '33',
    'WM_NI': 'retX5IaF0w5CuNoJ0uyy72yG%2FsYSEKYdC2p6pkpMAH7Q4VMYGuUSyPEk25YdmRftP8ILyD4y2sHimkOycQRYkjqqlpVqB7YYQ33OwAkdyQopGLMm6KkF6%2BaaURjzjG6LdDQ%3D',
    'WM_NIKE': '9ca17ae2e6ffcda170e2e6eeb3d63a9c99e5a4c64f8d9e8bb6c14f879e9f87c46bb2bfffccb663aab1be86d12af0fea7c3b92ab2bbbcb9b843a39a0098b849b792a1abb37fbba7f9d3fc4dedad97b4c8419bbc8dd3f33eb4b5c0aec444f58ffcb7d05385ab9bb4fc5c87b5fed6dc70af8eaa95d3348b94b7a5b773f2ad888af0618da7adb2d153a9b6bf92ef7c96af8ed8dc5393edfdb0f64ba9bcb7b2ee7c8594838eb541a99afacce46b978ea69be94df694aca5d437e2a3',
}

headers = {
    'authority': 'music.163.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '__bid_n=187385d55219a699254207; P_INFO=zawaludo@126.com|1680361713|0|mail126|00&99|null&null&null#gud&440100#10#0#0|&0|mail126|zawaludo@126.com; _ntes_nnid=e320573ab9dcf82fee6ce0bd1fde46ec,1680829462419; _ntes_nuid=e320573ab9dcf82fee6ce0bd1fde46ec; NMTID=00OUohNvG-YwixOHkjphD1aA8XEaIMAAAGHWT43ng; WEVNSM=1.0.0; WNMCID=dqynhy.1680829463077.01.0; WM_TID=YxDMEHuuqf9AEFUBVFaFahSqWDiMFV5d; FPTOKEN=TEpkUNAlvL799rywt8p/wL+wbG3UFmPCbFrC15If76oI0WjsW/HPO/WO2QcAqOFiDgcjB4iT/tuNBG357ZCoDLUwUl3uE8KOA3MZAalIMQFAdWYrepeiOVcAqP2yiBjJoMsxLTI2+yBYhKPs5i2EPtR4ZZMAj3QJXPs0HblxaovvgTYrHmilWXM9DE7drNF3dYmOtZ8FT6mTBagVSK0vriYxAFwpwXJdVOj6H5hYiBfTSE5T06twUOv4X45kTfV21cNSSMY4/OLO+21y8E9xgFRSleQkFbO+AVj3fNxwht38wtgsYq/rblOd+4JjeP7u7PljS/Euiw66M6j1nxdoc1s3P5LlD17UyoUrLUwdqdZc2ce0JKYC2hTIPIPptfSn3cUIaGSopnHqJj/h/A/Zyw==|MruS1jHKnpk5EZtETC+sysjuswKYAkknLHPIxTGkGzI=|10|2233f5d8e7da6c6ae8b6e9d9c39fdd03; JSESSIONID-WYYY=%2Fhyyfb7gwZjJVISqZPHJkcdQ0R7FFJ1kG%2Bztl%5CKYS5%2Fquh%5CCalpmX%2Bkv7kInXgHOynRjGKxql57GKMY1lOQPqt6sUa6cH747DoeWUhYvHHOZ7ijmqqg5T9xOkfPe15Y1DrHxnNTst5EPrTFRmVOZc9IvoWURlFsjZXFlUtufemhlP3i3%3A1683041701991; _iuqxldmzr_=33; WM_NI=retX5IaF0w5CuNoJ0uyy72yG%2FsYSEKYdC2p6pkpMAH7Q4VMYGuUSyPEk25YdmRftP8ILyD4y2sHimkOycQRYkjqqlpVqB7YYQ33OwAkdyQopGLMm6KkF6%2BaaURjzjG6LdDQ%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb3d63a9c99e5a4c64f8d9e8bb6c14f879e9f87c46bb2bfffccb663aab1be86d12af0fea7c3b92ab2bbbcb9b843a39a0098b849b792a1abb37fbba7f9d3fc4dedad97b4c8419bbc8dd3f33eb4b5c0aec444f58ffcb7d05385ab9bb4fc5c87b5fed6dc70af8eaa95d3348b94b7a5b773f2ad888af0618da7adb2d153a9b6bf92ef7c96af8ed8dc5393edfdb0f64ba9bcb7b2ee7c8594838eb541a99afacce46b978ea69be94df694aca5d437e2a3',
    'origin': 'https://music.163.com',
    'referer': 'https://music.163.com/search/',
    'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39',
}

params = {
    'csrf_token': '',
}


def search_music(song):
    global cookies, headers, params
    jscode = execjs.compile(open('./param_encSeckey(search_music).js', 'r', encoding='utf-8').read()).call('get_info', song)
    data = {
        # 'params': 'qcmGOmNTiR7q0qRyMLTaTupGxxFx7xRO4SVXpDk9E3fGmw5kxD9rP1mlPXsGPPTM2RQngXRKqcJknuhAa22FK96fVX2/7hSneAH6vBt1AwPrKQsaZUVb1DldBEioO1WnHmGQy5IsYyziFx20onvUHf71/hyeX31VobQE4dplNzm+o/mERYyKq/H9xXoNwEcXoRJ4rZA05qiXzQH2KMc0zzwapbgG3Tg6skv9O44kxW1iGm4Av0HqD5yGjkm4ULPGKD9Wa/+jeR0/03BqHzorsoweTC+3paB8bixKPdt0Cxw=',
        # 'encSecKey': 'd2d7cac9076735c7b649baaf52d8fd84c6f559dfd7cae887a8d300fe7ba02fd660e1db9b38add3a2713d88a4bab460bcff2ddab18c711c5d539b20c3be3cba458d25586b78ad02e33f4c3bb803853fde8fa56837dbcabf94094c723ec45a2536c871662c517ef50fa567d43547562f93e890bd01e6282d20dd30177692adeb71',
        'params': jscode['encText'],
        'encSecKey':jscode['encSecKey']
    }
    try:
        response = requests.post(
            'https://music.163.com/weapi/cloudsearch/get/web',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        ).json()
        # print(response['result']['songs'])
        ss = response['result']['songs']
        id_list = []
        for s in ss:
            # print(s['id'],s['name'],s['ar'][0]['name'])
            id_list.append(dict(id=s['id'], name=s['name'], arname=s['ar'][0]['name']))

        print(id_list)
    except Exception as e:
        print('Error', e, sep='\n')


if __name__ == '__main__':
    s_name = input('歌曲名:')
    search_music(s_name)
