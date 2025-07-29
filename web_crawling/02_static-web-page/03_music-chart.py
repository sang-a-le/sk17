# 노래 제목, 가수, 앨범 커버 이미지
# 앨범 커버 이미지 -> album_images 디렉토리에 저장
# 30위까지 출력 

import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve    # 사진 저장
from datetime import datetime 

class musicEntry : 
    def __init__(self, title, artist, img_path):
        self.title = title
        self.artist = artist
        self.img_path = img_path

    def __repr__(self):           # 보여주는 형태를 변형
        return f'musicEntry<title={self.title}, artist={self.artist}>'
    
url = 'https://music.bugs.co.kr/chart'

response = requests.get(url)

html = response.text
print(html)


bs = BeautifulSoup(html,'html.parser')

music_contents_box = bs.select_one('.innerContainer')  # 요소 확인하기 
#print(music_contents_box)

music_contents = bs.select('.CHARTrealtime table tbody td')

#print(music_contents)
#print(bs)

music_list = []


for idx, music_content in enumerate(music_contents):
    title_tag = music_content.select_one('.title')
    #print(music_content)
    artist_tag = music_content.select_one('.a')
    #print(artist_tag)
    img_tag = music_content.select_one('thumbnail')
    
    title = title_tag.text
    artist = artist_tag['title']
    img_path = ''
    

    # 이미지 경로 추출 + 이미지 저장
    if img_tag.has_attr('src'):
        img_path = img_tag['src']

        img_dir = 'album_images'
        file_name = datetime.now().strftime('%y%m%d_%H%M%S_') + str(idx + 1) + '.jpg'
        urlretrieve(img_path, f'{img_dir}/{file_name}')
    
    music_entry = musicEntry(title, artist, img_path)   # 객체 만들기
    music_list.append(music_entry)       

# 결과 출력
for music in music_list : 
    print(music)
