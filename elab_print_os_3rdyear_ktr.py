import requests
import json
import argparse


def login(sess,user,pas):
    creds='userid=%s&password=%s' %(user,pas)
    url="http://care.srmist.edu.in/rmpds/student/questions"
    header={
        'Host': 'care.srmist.edu.in',
        'Content-Length': '42',
        'Accept': '*/*',
        'Origin': 'http://care.srmist.edu.in',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'http://care.srmist.edu.in/rmpds/student/questions',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Cookie': '%s' %(sess[0]),
        'Connection': 'close',
    }
    response = requests.request("POST", url, data=creds, headers=header,allow_redirects=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="eLab Request Handler")
    parser.add_argument('-u', '--username', type=str, help="Registration Number")
    parser.add_argument('-p', '--password', type=str, help="Elab password")
    args = parser.parse_args()
    
    url="http://care.srmuniv.ac.in/ktrstudentskill/index.php"
    ind = requests.request("GET", url)
    sess=ind.headers['Set-Cookie'].split(";")
    login(sess=sess,user=args.username,pas=args.password)

    for i in range (0,100):
        ref='http://care.srmist.edu.in/rmpds/student/questions'
        headers={
        'Host': 'care.srmist.edu.in',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Referer': '%s' %ref,
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Cookie': '%s' %sess[0],
        'Connection': 'close'
        }

        header2={
            'Host': 'care.srmuniv.ac.in',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Cookie': '%s' %(sess[0]),
            'Connection': 'close'
        }

        url1='http://care.srmist.edu.in/rmpds/student/questions.php?id=1&value=%d' %i
        url='http://care.srmuniv.ac.in/ktrstudentskill/login/studentnew/code/getReport.php'
        print("Dowloading Report:%d" %i )
        r=requests.request("GET",url1,headers=header2)
        response = requests.request("POST", url, headers=headers)
        open('repo%d.png' %i, 'wb').write(response.content)
