import streamlit as st

st.header("💞欢迎来到视讯灵眸——智能视频生成与摘要平台", divider="rainbow")
st.write("### 🌈项目简介")
st.write(
    "视讯灵眸通过结合现有的先进技术（Open Sora 同源架构模型和 GPT-4o），实现了图片或视频生成与摘要的功能，可以显著提升视频生成的体验。"
)

st.write("### 🌟功能介绍")
st.write(
    "1. **图片生成视频**：用户上传图片后，输入文字进行提问，系统会使用 GPT-4o 来优化用户输入，并使用经过我微调后的 Open Sora 同源架构模型生成相应的短视频。"
)

st.write(
    "2. **文字生成视频**：用户输入文字后，系统会使用 GPT-4o 来优化用户输入的文本，并使用经过我微调后的 Open Sora 同源架构模型生成相应的短视频。"
)
st.write(
    "3. **图片或视频摘要**：系统生成图片视频后，会根据其生成相应的美观摘要描述。"
)
st.write(
    "4. **支持下载生成后的视频**"
)

st.write("## 🌞欢迎使用视讯灵眸，祝您使用愉快！")
