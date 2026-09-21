import streamlit as st
import streamlit.components.v1 as components

# 페이지 기본 설정
st.set_page_config(
    page_title="나의 캘린더 📅",
    page_icon="📅",
    layout="wide"
)

# index.html 읽기 및 화면 출력
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # HTML 컴포넌트로 렌더링 (높이 지정)
    components.html(html_content, height=1000, scrolling=True)

except FileNotFoundError:
    st.error("`index.html` 파일을 찾을 수 없습니다. main.py와 같은 폴더에 놓아주세요.")
