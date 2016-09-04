import random
from pymongo import MongoClient
def gen_code(id_i):
    num="%08d"%id_i
    code=random.sample('abcdefghijklmnopqrstuvwxyz',8)
    i=0;
    a=''
    while i<8:
        a=a+num[i]+code[i]
        i=i+1
    return a
if __name__ == '__main__':
    conn = MongoClient(host='192.168.1.113',port=27017)
    db = conn.cypdb
    cl=db.actcode
    #a=[ gen_code(i) for i in range(0,100,15)]
    codegen=dict()
    for i in range(0,105,15):
        codegen[str(i)]=gen_code(i)
    #print(codegen)
    cl.save(codegen)
    #remove all
    #cl.remove({})
    print(list(cl.find()))
#    cl.insert_one()
#    cl.insert_many()
    
# mongodb   sqlite 