param_paiming={'queryId': '327|3569521|575-575-card-1530697353164-grid',
            'cubeId': '4fecd9ce-ef5d-48cb-aa17-fd924e652f8b',
            'queryDetail': False,
            'pageId': '575',
            'pageComponentId': 58,
            'timeType': 1,
            'sign': None,
            'limit': 100,
            'row': '[{"name":"日期","isMeasure":false}]',
            'measure': '[{"name":"转人工率","isMeasure":true},{"name":"转人工率类目top3商家值","isMeasure":true},{"name":"首问语uv点击率","isMeasure":true},{"name":"首问语uv点击率类目top3商家值","isMeasure":true},{"name":"智能服务占比","isMeasure":true},{"name":"智能服务占比类目top3商家值","isMeasure":true},{"name":"店小蜜询单转化","isMeasure":true},{"name":"店小蜜询单转化类目top3商家值","isMeasure":true},{"name":"人工询单转化率","isMeasure":true},{"name":"所有指标总得分排名","isMeasure":true}]',
            'column': '[]',
            'orders': '[{"name":"日期","isMeasure":false,"order":"DESC"}]',
            'filter': '[{"name":"是否当天使用","type":"dimension","isMeasure":false,"values":[1],"oper":"="}]',
            'extra': None}#转人工率E|F, #卡片点击率J|K, #全自动接待占比U|V, #人工参与询单转化率Q,  #店小蜜参与询单转化率P|S, 行业排名C

param_zhuanhua={'queryId': '198|62498350|undefined',
               'cubeId': 'e776823b-5ce7-4e25-9130-544633b7bbe1',
               'queryDetail': False,
               'pageId': '557',
               'pageComponentId': 63,
               'forceDay': 30,
               'sign': None,
               'limit': 5000,
               'row': '[{"name":"日期","isMeasure":false}]',
               'measure': '[{"name":"全自动纯店小蜜询单转化率","isMeasure":true},{"name":"全自动接待UV","isMeasure":true},{"name":"全自动参与询单UV","isMeasure":true},{"name":"店小蜜接待后转人工询单UVnew","isMeasure":true},{"name":"店小蜜接待后转人工下单UVnew","isMeasure":true}]',
               'column': '[]',
               'orders': '[{"name":"日期","isMeasure":false,"order":"ASC"}]',
               'filter': '[]',
               'extra': None}# 纯店小蜜询单转化率O|接待人数X|小蜜参与询单人数W|人工衔接后下单率H=店小蜜接待后转人工下单UVnew/店小蜜接待后转人工询单UVnew

headers={'accept':'*/*',
         'accept-encoding':'gzip, deflate, br',
         'accept-language':'zh-CN,zh;q=0.8',
         'content-length':'1086',#1324
         'origin':'https://dianxiaomi.taobao.com',
         'referer':'https://dianxiaomi.taobao.com/',
         'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}

ddict={'operate':'query','scope':'cntaobao'}

url='https://alphax.taobao.com/xinsight/XinsightManager.do?operate=query'




