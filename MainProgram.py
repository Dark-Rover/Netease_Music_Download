import os
import traceback

import execjs
import requests

cookies = {
    'WM_TID': '%2BXq3UQoVXFDTbYS%2Bz7FIfJJ2ba5VB6Us',
    '_ntes_nuid': 'aa976aeaebcb6ce1d6e06841c28b8361',
    'NTES_P_UTID': 'Xj56DglO4lw23wOVQrEWBLMZ4Yt3JBe8|1665506437',
    'P_INFO': 'zawaludo@126.com|1667570667|0|mail126|00&99|null&null&null#gud&440100#10#0#0|&0||zawaludo@126.com',
    'FPTOKEN': 'eVnFqX8NCtN21+OTxj7CdiXnH70FkZ834Wqi6qUibQNbkq+24HEDux4TMUA+EQY538RiPmBLYSY7z0FWrgYDXtgSVDBC/8bprhkoKQ/meXGcRaggmiTwRxiL3FpGT1Qi8HQyF+9iNDoBZM9qgyxTqBxNxfSF+QEhbmmO5G4g51aqRWFcWcgsXQAKYUgdR638slJ36MXDV7mJLpK4bvXs/vwATd34P02Hl+Ecw/uEkYz2JE+UFi09y1nWMnWM6H/L+2w1F7RYjfnz/N5HrN5xWJKrHsf0DWhoErhvlyH8PSLfQE2dE8092G2aldfVjxLzGwrlPQz89oSOJkfgwouIfYyzfiZszb8xEu9pvsJmI19HxCu5DY52few5338XG6O6DbLPK1EbUXE3/dvaZa624w==|H+plIZV8jJyp6lcu2b312MdWPGRygExW6MqMgS8H7bU=|10|e58cf226c60abdf4cd6d1c05d9b16922',
    '_ntes_nnid': 'aa976aeaebcb6ce1d6e06841c28b8361,1676775425704',
    'NMTID': '00OEmGeeJc32OwIXEzZufM_xp_EDJwAAAGGZ5qG6g',
    'WEVNSM': '1.0.0',
    'WNMCID': 'uhpsor.1676775426459.01.0',
    'JSESSIONID-WYYY': 'eo6OA1ctSOhigp6wgcp12D9%2B2llEji7N%2FWF1DmN2c%2BiQDZwws%2FmUnRH49uqSKQm8v2C9Nt0eWj7VCScMz%2BSDB72GiFUVZsdaVNnfIFof0U%2FXhZ5Bg4Zm%5CEh5%2FDnHKT%2FqDZSls243mwtHSdTNAliy%5CrNn6PoN7el9W3KhslIehDg9MUmO%3A1677593117192',
    '_iuqxldmzr_': '33',
    'WM_NI': 'UKORbMl4049KH2O%2FC2OZ1%2FAPwOTaB9xg2WoljVlP6ruMggC1W4%2BpImGAFO%2F%2FI7R5JHJahClt%2BE95rS6LjjpsaRI6EDVidUqxzmVZOKPomzIQMDxuBx%2BXpUTPnmrBFGJLTEY%3D',
    'WM_NIKE': '9ca17ae2e6ffcda170e2e6eeaadb48b2888694cf2582ef8ab6c15f968e8fb0d46b8e908ab4ae4a96edb797e92af0fea7c3b92a979581b3e147b0ec00d5bc418cee81d0c23a8d86ffd0c45cb5919c82c133bcb9feb8ee68aa8aa4b1b57ab793a988c23b95ece591cc67859f8ab0ae258be99ed6c9448abfa8a4ef80e99bf7d6f159f694a68bf379a38e87d7c85096b7acb6f474bab39abbce4194b1a39bcc5b8f9cb896c174e988c0b6d75caeb3bea3c54d8a949ca6dc37e2a3',
    'playerid': '92343383',
}

headers = {
    'authority': 'music.163.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
    'content-length': '440',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://music.163.com',
    'referer': 'https://music.163.com/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.69',
    'x-forwarded-for': '8.8.4.4',
    'x-music-loc-site': '100_https://music.163.com/',
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
        'encSecKey': jscode['encSecKey']
    }
    try:
        response = requests.post(
            'https://music.163.com/weapi/cloudsearch/get/web',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        ).json()

    except Exception as e:
        print('Error', e, sep='\n')
    else:
        # print(response['result']['songs'])
        ss = response['result']['songs']
        id_list = []
        for i, s in enumerate(ss):
            # 创作人有多个，需要使用字符串拼接列表元素，展示出来  例如 / Name: Infinity (PRETTY YOUNG Remix) / Artist -- Jaymes Young/PRETTY YOUNG
            artists = ' / '.join([x['name'] for x in s['ar']])
            print(i, '/ Name: '+s['name'], f'/ Artist -- {artists}')
            id_list.append(dict(num=i, id=s['id'], name=s['name'], arname=s['ar'][0]['name']))
        # print(id_list)
        s_num = int(input('请选择上述哪一首歌曲进行下载(输入编号)'))
        try:
            download_music(id_list[s_num]['id'], name=id_list[s_num]['name'], artist=id_list[s_num]['arname'])
        except Exception:
            tb = traceback.format_exc()
            print(tb)


def download_music(s_id, **kwargs):
    global params, cookies, headers
    jscode = execjs.compile(open('param_encSeckey.js', 'r', encoding='utf-8').read()).call('get_info', s_id)
    data = {
        'params': jscode['encText'],
        'encSecKey': jscode['encSecKey']
    }
    try:
        response = requests.post(
            'https://music.163.com/weapi/song/enhance/player/url/v1',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data
        ).json()
        # print(response)
    except Exception as e:
        print('Get music_url Failed', e, sep='\n')
    else:
        m_url = response['data'][0]['url']
        print('url:', m_url)
        name, singer = kwargs['name'], kwargs['artist']
        # print(name, singer)
        try:
            song_resp = requests.get(m_url)
            form = m_url.split('.')[-1]
            print('response_status--', song_resp.status_code, sep='\n')
        except Exception as e:
            print("Can't Download '{0}', Please try other way to download music".format(name), e, sep='\n')

        else:
            file_path = f'E:/Python/Spiders/JS_Reverse/NetEaseMusicDownload/Audio/{name}'
            # 文件去重
            if os.path.exists(f'{file_path}.{form}'):
                print(f"{name + singer} already exists, skipping downlAsoad.")
                return
            try:
                with open(f'{file_path}.{form}', mode='wb') as f:
                    f.write(song_resp.content)
                print(f'Song:{name}, Artist:{singer}, Downloaded!!!', sep='\t')
            except Exception:
                tb = traceback.format_exc()
                print(tb)


if __name__ == '__main__':
    s_name = input('输入要搜索的歌曲名: ')
    search_music(s_name)
