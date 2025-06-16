import streamlit as st
import pandas as pd
import numpy as np

st.title('🍴:green[맛따라, 멋따라, 민수따라]')
st.write('[ 자칭 :orange[\'미식가\'] 김민수의 :orange[서울 맛집 리스트] 모음집, 지금 시작합니다. ]')

st.image('KakaoTalk_20250605_011230439.jpg', caption='서울토박이의 숨은 맛집 대공개', width=500)
st.markdown('#### BGM이 빠질 순 없지.')
st.audio('good-night-lofi-cozy-chill-music-160166.mp3')
st.divider()
st.subheader(':blue[맛집 장소 한눈에 보기]')
st.write('📍서촌  /  문래  /  까치산역')

locations = {
    '서촌 - 토속촌 삼계탕': [37.5778, 126.9750],
    '서촌 - 인왕산 대충유원지': [37.5734, 126.9730],
    '문래 - 레트로스펙터': [37.5105, 126.9054],
    '까치산역 - 심원생고기': [37.5186, 126.8602],
}


df = pd.DataFrame(locations.values(), columns=['lat', 'lon'], index=locations.keys())

st.map(df)

st.divider()

# 토속촌
st.write('')
st.write('')
st.header(':green[1. 서촌 토속촌 삼계탕]🐔')
st.image('KakaoTalk_20250605_022714010.jpg', caption='국물의 깊이에 우리네 인생이 담겼다.', width=500)

st.write("""
    **서촌의 토속촌 삼계탕**은 사실 이미 유명한 삼계탕 맛집입니다.
         
    초등학교 시절, 할아버지의 손에 이끌려 자주 갔던 그 때의 향수를 불러일으키는 의미있는 장소입니다.
    녹진하게 우려진 삼계탕 국물은 목에 코팅이 되는 느낌이 들 정도로 그 맛이 깊으며, 잘 삶아진 닭고기는 젓가락으로 살짝 건드리기만 해도 바로 발라집니다. 
         
    기말고사가 끝나가고 여름이 다가오는 지금, 힐링이 필요한 분들에게 **보양식**으로 제격입니다.
""")
st.write('')
st.write('')
st.write('''### :blue[대표 메뉴] 
         토속촌 삼계탕       20,000원
    옻계탕             20,000원
    오골계 삼계탕       25,000원
             ''')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')

columns = ['맛', '가격', '대기시간']
num = [5, 4, 4.5]

df = pd.DataFrame({'만족도': num}, index=columns)

st.bar_chart(df)

st.success('**美味!** 맛은 완벽합니다! 진한 국물은 보양이 되고, 잘 익은 깍두기는 kick입니다.', icon='🤌')
st.warning('돈이 없는 대학생에겐 **특별한 날 먹는 고급식**입니다. 하지만, 돈이 아깝지 않은 맛입니다!', icon='💵')
st.error('**웨이팅 거의 없는 맛집**, 귀하죠?  본관, 별관, vip관까지 자리가 많으니 걱정마세요:)', icon='🕝')
st.write('')
st.write('')
st.info('총점은 **4.5점**! 더할 나위 없는 완벽한 한 끼를 보장합니다!')
st.write('')
st.write('')
st.write('')
st.write('')

st.divider()


# 인왕산 유원지
st.header(':green[2. 서촌 인왕산 대충유원지]☕')
st.image('KakaoTalk_20250605_023452749_06.jpg', caption='요즘 말로 분좋카-!', width=500)
st.write("""
    **인왕산 대충유원지**는 서촌의 고즈넉한 분위기와 어울리는 감각적인 인테리어의 카페입니다.
     
    바테이블에서는 도란도란 얘기 나누고, 창문 앞 테이블에서는 사진을 찍으며 분위기를 즐길 수 있습니다.  
    카페를 좋아하는 분들이라면 강력추천합니다.
    토속촌 삼계탕에서 보양한 후, 후식을 즐기고 예쁜 사진까지 얻을 수 있는 최적의 코스입니다!  
""")
st.write('')
st.write('')
st.write('')
st.write('#### #사진 맛집')
col1, col2= st.columns(2) # 3개의 칼럼 생성
col1.image('KakaoTalk_20250605_023452749.jpg', width=300)
col2.image('KakaoTalk_20250605_023452749_02.jpg', width=300)
st.write("""카페에서 사진 찍기 좋아하는 분들은, **저녁**에 가는 것을 추천드립니다.  
         해가 지고나서의 카페 분위기는 마치 와인바같습니다.  
         은은한 조명과 차분한 음악이 마치 여유로운 예술가가 된 것 같은 느낌을 줍니다.\n\n서촌에
         특별한 애정이 있는 이유는 바로 이 **고즈넉함**입니다. 멀리 보이는 인왕산과 여유로운 사람들, 미적으로 세련되고 정돈되어있는 건물들.
         :orange[**사랑하지 않을 수 없습니다.**] 
         """)

st.write('')
st.write('')
st.write('#### #나도 MZ')
video_file = open('KakaoTalk_20250612_130422742.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
st.write("""
         :gray[일본의 유명한 브륄레 아이스크림이 생각났던 달달하고 부드러운 브륄레.  
         (양이 적어 아쉬웠습니다...)]""")
st.write('')
st.write('')
st.write('')
st.write('')
st.write('### :blue[메뉴 평점]')
col1, col2, col3 = st.columns(3) 
col1.metric('버터스카치 브륄레', '★★★★★', '한 바가지로 먹고싶은 맛')
col2.metric('필터커피', '☆★★★★', '산미있는 커피의 정석')
col3.metric('시소 레몬에이드', '☆☆★★★', '-맛있지만 잘 섞이지않음')
st.info('메뉴는 **총점 4점!** 하지만 분위기가 다했으니 **총점 4.5**로 승격!')
st.write('')
st.write('')
st.write('')

st.divider()


# 문래의 레트로문래
st.header(':green[3. 문래 레트로스펙터]🍸')
st.image('KakaoTalk_20250612_120707608_01.jpg', caption='느좋바, 레트로스펙터', width=500)

st.write("""
    **문래의 레트로스펙터**는 유명해지지 않았으면 하는 저만의 숨은 맛집입니다.  
    작은 와인바지만, 사장님이 직접 요리해주시는 신기한 요리들이 고급 레스토랑 코스요리를 먹는 듯한 기분을 느끼게 해줍니다.
    높은 건물들과 대비되는 문래동 골목의 단란한 분위기와 어우러지는 작은 와인바입니다.  
         
    가게가 크지 않아 연인과 조용하게 데이트하기 딱 좋은 장소입니다.  
    사장님이 혼자 요리하시는 것을 구경하는 재미도 있습니다:)
""")
st.error('자리가 좁아 4명 이상의 인원은 앉기 힘들 수 있습니다!', icon='💑')

st.write('')
st.write('')
st.write('#### #사장님, 흑백요리사에서 뵙죠.')
st.image('KakaoTalk_20250612_120707608.jpg', caption='낯설지만 입이 즐거운 메뉴들', width=500)
st.write('')
st.write(""":orange[레몬]과 :green[바질]이 이렇게 어울리는 줄 몰랐던 신기한 파스타. 처음 느껴보는 맛이지만 계속 먹게 되고 
        집가서도 계속 생각났던 맛.  
        :red[버섯조림]을 곁들여 먹는 크림치즈와 크래커. 고급레스토랑에서 에피타이저로 내어줄 법한 바삭한 크래커와 짜고 달달한 버섯조림의 조합은 환상이었습니다.""")
st.write('')
st.write('')
st.write('')
st.write('')
st.write('### :blue[메뉴 평점]')
col1, col2, col3 = st.columns(3) 
col1.metric('레몬 바질 콜드 파스타', '★★★★★', '1년동안 생각나는 맛')
col2.metric('크림치즈와 크래커', '★★★★★', '클래식한데 새로운 맛')
col3.metric('안테라, 모스카토', '★★★★★', '달달하고 뒷맛이 깔끔')
st.info('**총점 만점!** 한 마디로, 완벽했던 식사.')
st.error('와인까지 곁들이다 보면 통장의 출혈이 클 수 있음. 기념일에 먹을 것!',icon='⛔')
st.write('')
st.write('')
st.write('')
st.write('')

st.divider()



# 까치산 심원생고기
st.header(':green[4. 까치산 심원생고기]🥩')
st.image('KakaoTalk_20250612_134543721.jpg', caption='살살 녹는 소갈비살, 넘치는 반찬', width=500)
st.write('')
st.write("""
    **심원생고기**는 까치산역 근처에서 많은 사랑을 받고 있는 고깃집입니다.  
    법대 02학번 선배님께서 항상 이곳에서 밥을 사주시는데, 눈물날 정도로 맛있습니다.  
    일반 고깃집의 맛과 확연한 차이를 느낄 수 있는 **엄청난 고기의 질**을 자랑합니다.
""")
st.write('')
st.warning('**주의!** 술이 너무 잘 들어가서 다음 날 숙취에 시달릴 수 있음.', icon='⚠')
st.write('')
st.write('')
st.write('#### 양웅상쟁, 소갈비살과 목살')
col1, col2= st.columns(2) # 3개의 칼럼 생성
col1.image('KakaoTalk_20250612_134611067.jpg', width=300)
col2.image('KakaoTalk_20250612_134305187_02.jpg', width=300)

st.write("""고기는 언제 옳지만, 심원생고기의 **소갈비살**은 급이 다릅니다.  
         입에 넣자마자 살살 녹으며 기분 좋은 포만감을 줍니다. **목살**도 이에 뒤지지 않습니다.  
         목살은 저렴한 부위, 저렴한 맛이라는 저의 편견을 깨부신 심원생고기의 목살은 저의 최애 부위입니다.\n\n""",

         """또한 고기는 구워먹는 음식이므로, **굽는 사람의 스킬**에 따라 맛이 달라질 수 있습니다. 
         너무 타지않을 정도로 고르게 고기를 굽는 것이 핵심입니다.""")
st.write('')
st.success("""고기의 양 너무 푸짐해서, 한 사람은 굽느라 바빠 많이 못 먹을 수도도 있어요!  
           수시로 친구의 입에 고기를 넣어주세요:)""", icon='💓')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('### :blue[메뉴 평점]')
col1, col2, col3 = st.columns(3) 
col1.metric('소갈비살', '★★★★★', '-너무 맛있어서 짜증남')
col2.metric('목살', '★★★★★', '목살은 이제부터 고급부위')
col3.metric('술과의 페어링', '★★★★★', '잡내없이 깔끔해 술을 부름')
st.write('')
st.write('')
st.write('')
st.write('')
columns = ['맛', '가격', '선배사랑']
num = [5, 3.5, 5]

df = pd.DataFrame({'만족도': num}, index=columns)

st.bar_chart(df)

st.info('**맛은 만점!!** 이 정도의 고기를 이 정도의 가격으로 만나기 어려워요.', icon='🍀')
st.warning('가엾은 대학생들은 선배의 **드넓은 사랑**으로만 경험할 수 있는 정도의 가격이에요.', icon='😭')
st.error("""선배님에게 은혜를 갚기 위해,   
         내 돈으로 배부르게 먹을 수 있도록, **돈을 열심히 벌어야 겠다**는 생각이 드는 맛!!""", icon='🔥')
st.write('')
st.write('')
st.write('')

st.divider()
# 평점 총정리
st.write('### 평점 총정리')
import pandas as pd

df = pd.DataFrame({
    '맛집': ['토속촌 삼계탕', '인왕산 대충유원지', '레트로스펙터', '심원생고기'],
    '평점': [4.5, 4.5, 5, 4.5],
    '비고': ['힐링이 필요할 때', '감각적인 사진을 원할 때', '크림치즈크래커 강추!!', '돈 많이 벌어 매일 가야지.'],
})

df
st.write('')
st.write('')


df = pd.DataFrame({
    '맛집': ['토속촌 삼계탕', '인왕산 대충유원지', '레트로스펙터', '심원생고기'],
    '평점': [4.5, 4.5, 5, 4.5]
})


# 한글 폰트로 변경해서 배포하면 무슨 짓을 해도 자꾸 깨져서
# 영어로 그래프 만들었습니다ㅠㅠ

import matplotlib.pyplot as plt

st.subheader("맛집 평점 그래프")

df = pd.DataFrame({
    'Best': ['tosokchon', 'Daechung park', 'Retrospector', 'simwon'],
    'Rating': [4.5, 4.5, 5, 4.5]
})

fig, ax = plt.subplots()
ax.bar(df['Best'], df['Rating'], color='g')
ax.plot(df['Best'], df['Rating'], c='c', marker='o', mfc='w', mew=2, linewidth=2, linestyle='--')
plt.ylim(0, 5.5)
plt.ylabel('Rating')
plt.title('Rating Comparison')

st.pyplot(fig)



st.write('')
st.write('')
st.write('')
st.write('')

st.header('*:green[맺으며]*')
st.markdown(""":green[
    제가 사랑하는 **서울의 맛집 4곳**을 소개해보았는데요,   
    날씨가 맑고 나들이 나가기 더없이 좋은 요즘, 더 북적여지기 전에 꼭 방문해보세요!]
""")

st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write("""
    ### ⬇맛집 링크⬇
    1. [서촌 - 토속촌 삼계탕](https://naver.me/FW6hFEuf)
    2. [서촌 - 인왕산 대충유원지](https://naver.me/GdymsoSW)
    3. [문래 - 레트로스펙터](https://naver.me/FY3ysNbi)
    4. [까치산 - 심원생고기](https://naver.me/GyY2nMbb)
""")
st.write('')
