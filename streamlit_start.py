import streamlit as st

st.title('첫번째 웹 만들기')
st.write('# 1. Markdown 텍스트 작성하기')
st.markdown(
    '''
    # 마크다운 헤더1
    - 마크다운 목록1. **굵게** 표시
    - 마크다운 목록2. *기울임* 표시
        - 마크다운 목록 2-1

    1. 마크다운 목록1
    2. 마크다운 목록2
        1. 마크다운 목록2-1
            1. 마크다운 목록2-1-1
    ''' )

st.write('''# 샵 한 개
## 샵 두 개
### 샵 세 개
#### 샵 네 개
##### 샵 다섯개
###### 샵 여섯개 ''')

st.title('타이틀')
st.header('헤더')
st.subheader('서브헤더')
st.text('텍스트')
st.markdown('## 마크다운 샵 두 개')
st.markdown('### 마크다운 샵 세 개')

st.divider()

st.markdown('[홍익대학교](https://www.hongik.ac.kr/kr/index.do)')
st.write('[홍익대학교](https://www.hongik.ac.kr/kr/index.do)')
st.title('[홍익대학교](https://www.hongik.ac.kr/kr/index.do)')
st.header('[홍익대학교](https://www.hongik.ac.kr/kr/index.do)')
st.subheader('[홍익대학교](https://www.hongik.ac.kr/kr/index.do)')
st.caption('[홍익대학교](https://www.hongik.ac.kr/kr/index.do)')
st.caption('캡션 작은 회색 글씨로 작성하기')

st.code(print('hello'))
st.code('print("hello")')
st.code('print("hello")',
        language='python', line_numbers=True)

st.write('#### 코드+결과: st.echo()')
with st.echo():
        name = 'chunghun ha'
        st.write("hello streamlit!", name)

with st.echo():
        name = 'chunghun ha'
        st.write(print(name))

st.latex('\sum_a^b f(x)dx')

st.write('#### Latax 수식 작성: Markdown')
st.markdown('''
            :green[본문에서 사용할 때에는] :red[$\int_a^b f(x)dx$] 이렇게 사용하고,
            별도의 행으로 만들고 싶을 때에는
            :blue[다음과 같이 사용한다.]
            :orange[$$\int_a^b f(x)dx$$]
            ''')

'''### Magic 적용
1. ordered item'''

st.image("https://cdn.icon-icons.com/icons2/2699/PNG/512/python_logo_icon_168886.png")


''' 오디오 넣으려면 mp3 sample'''
st.image("./Data/logo.webp", caption="파이썬 로고", width=500)
'''앞에 점 두 개는 상위폴더??'''

''' ## 콜아웃은 색상으로 표시 '''
st.info('This is a purely informational message', icon='🤖')
st.success('This is an success message', icon='💟')
st.warning('This is a warning message', icon='👽')
st.error('This is Error message', icon='☠')

# 데이터 테이블
### Pandas 데이터 프레임 출력
import pandas as pd
df = pd.DataFrame(
        {'id':123,
         'name':['A', 'B', 'C'],
         'age':[23, 24, 25]}
)
# 칼럼 세 개
df # 데이터프레임 출력


### 지표
col1, col2, col3 = st.columns(3) # 3개의 칼럼 생성
col1.metric("Temperature", "70F", "1.2F")
col2.metric("wind", "9 mph", "-8%")
col3.metric("asas", "24424234", "dsdsd")

st.divider()

'''# 그래프
### **Streamlit 제공 그래프**
'''

import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["a", "b", "c"]
)

st.area_chart(chart_data)
st.line_chart(chart_data)
st.bar_chart(chart_data)
st.scatter_chart(chart_data)

df = pd.DataFrame(
        np.random.randn(100, 2) / [100, 100] + [37.55, 126.92],
        columns=["lat", "lon"]
)
# 이게 뭐라고????????????????
st.map(df)

st.divider()

'''## 시각화 라이브러리 활용'''
import matplotlib.pyplot as plt
import numpy as np    # 이게 무슨 용도라고??????????

# 멧플로우는 기본적으로 다 배워야 됨, 가장 기초적이고 세부적인 것까지 컨트롤 가능
# 정적인 그래프 만드는 데 유용, 속도 빠름

# 플롯틀리는 화려하고 인터렉티브 디렉터임 다양한 동작이 가능함
# 캡쳐 확대 이동 같은 것이 기본적으로 가능

# 알테어는 전문적인 그래프 나이스하게 그려짐
# 기본적으로 스트림릿에서 제공하는 기능 있음

# 결론적으로 필요에 따라 다 사용하게 된다.

# 에러나는 이유
# no module named plotly >>> 안 깔랴있어서서