import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Stereanlit入門")


latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f"Interation {i+1}%")
    bar.progress(i+1)
    time.sleep(0.02)


left_column,right_column=st.columns(2)
button = left_column.button("右カラムに文字表示")
if button:
    right_column.write("hello world")

expander1 = st.expander("問い合わせ1")
expander1.write("問い合わせ内容を書く1")
expander2 = st.expander("問い合わせ2")
expander2.write("問い合わせ内容を書く2")
expander3 = st.expander("問い合わせ3")
expander3.write("問い合わせ内容を書く3")
# text = st.text_input("何か入力してください")
# condition = st.slider("あなたの調子は?",0,100,0)

# "あなたは『 ",text," 』と入力しました。"
# "コンディション：",condition

# number = st.selectbox(
#     "数字を選択してください",
#     list(range(1,11))#1~10
# )
# "あなたが選択した数字は",number,"です。"


if st.checkbox("Show Image"):
    img=Image.open("image.png")
    st.image(img,caption="欅カフェ",use_column_width=True)
