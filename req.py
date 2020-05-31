import requests
import json
import params
import time


params.headers['cookie']='_samesite_flag_=true; sgcookie=ERtwzwsecPoiB%2BWElpDRM; unb=3951819162; sn=%E8%87%AA%E7%84%B6%E4%B9%8B%E5%90%8D%E6%97%97%E8%88%B0%E5%BA%97%3A%E4%B8%AB%E4%B8%AB; csg=3feb652a; t=17675128b1061e00e9c162ee46f0e98f; skt=46249cf48cd3f8c1; cookie2=1f4f251088e504ddf2468855fc6533bb; _cc_=VFC%2FuZ9ajQ%3D%3D; _tb_token_=e871745deb169; tfstk=cYVCBvqGmHxQ-yVe_u_ZU6_0GihPZI8jP9i3RRviE3BNiPzCM1c4ukKp2WNrS; cna=RjpxFiVteBwCAWX1SOhbsFEH; uc1=cookie14=UoTUM2YcNuNttA%3D%3D&cookie21=UtASsssmfufd; l=eBOqyU3Vqt4f6SKNmOfZnurza779TIRfguPzaNbMiOCP_j_M8KRRWZAAzQdHCnGVHsGHR3WdDRV4BOPe2yC4UHrNLVik9jMmndC..; isg=BKurR4YXcTJfTa5I_1Byfs_FOs-VwL9C2Oi7xx0o1epbvMoepZAqk3paFvzSnBc6'


t1 = time.localtime(time.time() - 3600 * 24 * 30)
t2 = time.localtime(time.time() - 3600 * 24)
params.param_paiming['startTime'] = f'{t1[0]}-{"%02d" % t1[1]}-{"%02d" % t1[2]} 23:59:59'
params.param_paiming['endTime'] = f'{t2[0]}-{"%02d" % t2[1]}-{"%02d" % t2[2]} 23:59:59'
params.ddict['_tb_token_']='e871745deb169'
params.ddict['_dxm_token_']='e871745deb169'
params.ddict['param']=json.dumps(params.param_paiming) #json.loads(str)


res = requests.post(params.url,headers=params.headers,data=params.ddict)
e=res.json()
e1=json.loads(e['data']['xinsight'])
e11=e1['data']['cellset']
for i in e11[0]:
    print(i['properties']['caption'])
print('*****************************')
for i in range(1,len(e11)):
    for j in e11[i]:
        print(j['properties']['raw'])
    print('------------------------------')



