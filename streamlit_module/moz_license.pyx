import streamlit as st
import markdown2
import streamlit.components.v1 as components
def render_license_tab():
    # LICENSES.mdファイルを読み込む
    with open("LICENSES.md", "r", encoding="utf-8") as file:
        markdown_text = file.read()

    # markdown2を使用してMarkdownをHTMLに変換
    html_content = markdown2.markdown(markdown_text, extras=["tables"])

    # HTMLをStreamlitで表示
    st.components.v1.html(html_content, scrolling=True)




