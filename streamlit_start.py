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
