from html.parser import HTMLParser  
from urllib.parse import urlparse  
#from urllib.parse import urllib2  
  
#import HTMLParser  
#import urlparse  
#import urllib2  
#import cookielib  
  
import urllib  
import urllib.request  
import http.cookiejar  
import string  
import re  
  
#��¼����ҳ��  
hosturl = '****' #�Լ���д  
#post���ݽ��պʹ����ҳ�棨����Ҫ�����ҳ�淢�����ǹ����Post���ݣ�  
posturl = '****' #�����ݰ��з�����������post�����url  
  
#����һ��cookie��������������ӷ���������cookie�����أ������ڷ�������ʱ���ϱ��ص�cookie  
cj = http.cookiejar.LWPCookieJar()  
cookie_support = urllib.request.HTTPCookieProcessor(cj)  
opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler)  
urllib.request.install_opener(opener)  
  
#�򿪵�¼��ҳ�棨����Ŀ���Ǵ�ҳ������cookie����������������post����ʱ����cookie�ˣ������Ͳ��ɹ���  
h = urllib.request.urlopen(hosturl)  
  
#����header��һ��header����Ҫ����һ������������Ǵ�ץ���İ�������ó��ġ�  
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',  
           'Referer' : '******'}  
#����Post���ݣ���Ҳ�Ǵ�ץ��İ�������ó��ġ�  
postData = {'op' : 'dmlogin',  
            'f' : 'st',  
            'user' : '***', #����û���  
            'pass' : '***', #������룬������������Ĵ���Ҳ���������ģ������������Ҫ������Ӧ�ļ����㷨����  
            'rmbr' : 'true',   #�������ݣ���ͬ��վ���ܲ�ͬ  
            'tmp' : '0.7306424454308195'  #�������ݣ���ͬ��վ���ܲ�ͬ  
  
            }  
  
#��Ҫ��Post���ݱ���  
postData = urllib.parse.urlencode(postData).encode('utf-8')  
  
#ͨ��urllib2�ṩ��request��������ָ��Url�������ǹ�������ݣ�����ɵ�¼����  
request = urllib.request.Request(posturl, postData, headers)  
print(request)  
response = urllib.request.urlopen(request)  
text = response.read()  
print(text)  
  
save_path="D:\\snatch2.txt"   
# save_path 's file unnecessary to be exist  
f_obj = open(save_path,'wb')  
f_obj.write(text)  
print("snatch successfully.") 