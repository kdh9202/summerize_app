import streamlit as st
from openai import OpenAI

# Streamlit Cloud의 Secrets에서 API 키 가져오기
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def summarize_text(prompt):
    """ChatGPT를 사용하여 텍스트를 요약합니다."""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        summary = response.choices[0].message.content.strip()
        return summary
    except Exception as e:
        return f"오류 발생: {e}"

def main():
    # 페이지 구성
    st.set_page_config(page_title="텍스트 요약 앱")

    st.title("📋 텍스트 요약 프로그램")
    st.markdown("이 앱은 입력된 텍스트를 ChatGPT를 사용하여 3문장으로 요약합니다.")
    st.markdown('---')

    # 입력 영역
    text = st.text_area("요약할 텍스트를 입력하세요:")

    if st.button("요약하기"):
        if text.strip():
            # 요약 프롬프트 생성
            prompt = f"""
            다음 텍스트를 3문장으로 요약해주세요:
            {text}
            """
            # ChatGPT로 요약 요청
            summary = summarize_text(prompt)

            # 결과 표시
            st.subheader("요약 결과")
            st.success(summary)
        else:
            st.warning("요약할 텍스트를 입력해주세요.")

if __name__ == "__main__":
    main()
