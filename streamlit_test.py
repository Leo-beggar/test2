import streamlit as st

# 创建标题
st.title("简单的 Streamlit 应用")

# 创建文本输入框
user_input = st.text_input("请输入一些文本:")

# 创建提交按钮
if st.button("提交"):
    # 显示用户输入的文本
    st.write("你输入的文本是:", user_input)