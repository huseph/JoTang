'''
* Download pics from https://worldcosplay.net/member/
* classify by characters
* made by Huseph
'''
import urllib.request
import os

url1 = 'https://worldcosplay.net/member/Itsuki-chan/characters/'


def url_open(url):
    print('这是url::',url)
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 YaBrowser/19.9.3.314 Yowser/2.5 Safari/537.36')
    
    print("req.add_header succeeded")
    
    response = urllib.request.urlopen(req)
    
    print("urlopen succeeded")
    
    html = response.read()
    print("read succeeded")
    return html
    

def get_img(img_num):
    img_name = str(img_num) + '.jpg'
    if os.path.exists(img_name):
        print(img_name, ' exist! skipping...')
        return
    url_aim = 'https://worldcosplay.net/photo/' + str(img_num)
    html = str(url_open(url_aim), encoding = 'utf-8')
    img_num1 = 0
    img_num1 = int(html.find('"image" src="', img_num1)) + 13
    img_num2 = int(html.find('"></div>\n\t\t\t</div>\n\t\t\t', img_num1))
    #print('我在get_img里：', type(img_num1), img_num1,type(img_num2), img_num2)
    if img_num2 > 0 :
        url_img = html[img_num1: img_num2]
        img = url_open(url_img)
        with open(img_name, 'wb') as f:
            f.write(img)
            

def character(ch_num, ch_name):
    ch_name = str(ch_num) + ch_name;
    if not os.path.exists(ch_name):
        os.mkdir(ch_name)
    os.chdir(ch_name)
    #print(type(ch_num))
    url_ch = 'https://worldcosplay.net/api/member/126641/characters/' + ch_num + '/photos.json?limit=16&p3_photo_list=true&page='
    html = ''
    for i in range(1,6):
        html += str(url_open(url_ch + str(i)), encoding = 'utf-8')
    #print('这是分页的代码！！:',html)
    img_num1 = 0
    img_num1 = int(html.find('"id":', img_num1))
    while img_num1 != -1:
        img_num1 += 5
        img_num2 = int(html.find(',"url', img_num1))
        get_img(html[img_num1: img_num2])
        img_num1 = int(html.find('"id":', img_num1))
    
    os.chdir('..')
    
def lets_roll():
    print('正在爬取图片...')
    if not os.path.exists('Itsuki-chan'):
        os.mkdir('Itsuki-chan')
    os.chdir('Itsuki-chan')
    ch_num1 = 0
    html = str(url_open(url1), encoding = 'utf-8')
    ch_num1= int(html.find('href="/member/Itsuki-chan/characters/', ch_num1))
    while ch_num1 != -1:
        ch_num1 += 37
        ch_num2= int(html.find('">', ch_num1))
        ch_name1 = int(html.find('<div class="photo_title">', ch_num1)) + 25;
        ch_name2 = int(html.find('<', ch_name1))
        character(html[ch_num1: ch_num2], html[ch_name1: ch_name2].replace("/", " "))
        ch_num1 = html.find('href="/member/Itsuki-chan/characters/', ch_num1)
    

    
if __name__ == '__main__':
    lets_roll()
   