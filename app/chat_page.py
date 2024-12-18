import streamlit as st
import pandas as pd
from PIL import Image
import time

# 初始化消息
INIT_MSG = [{"role": "assistant", "content": "你好呀！我是你的视讯灵眸小助手，请输入文本或者在左侧选择上传图片，我将为你生成图片或短视频和摘要，快来向我提问吧~🕵️"}]    

# 侧边栏部分
with st.sidebar:
    st.title("🌟视讯灵眸小助手🌟")
    uploaded_image = st.file_uploader("上传本地图片", type=["png", "jpg", "jpeg"])
    if uploaded_image is not None:
        image_name = uploaded_image.name

# 初始化 session_state
def init():
    st.session_state.messages = INIT_MSG.copy()
    st.session_state.uploaded_images = []
    st.session_state.video_summaries = {}  # 用于存储视频对应的摘要
    st.session_state.image_summaries = {}  # 用于存储图片摘要

if "messages" not in st.session_state.keys():
    init()

# 清空当前对话
if st.sidebar.button("清空当前对话"):
    init()
    st.rerun()  # 刷新页面

# 展示消息历史
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.write(message["content"])
            if "image" in message:
                st.image(message["image"], caption=f"上传的图片：{message['name']}")
    elif message["role"] == "assistant":
        with st.chat_message("assistant"):
            st.write(message["content"])
            if "image_url" in message:
                st.image(message["image_url"], caption="生成的图像")
            if "video_url" in message:
                st.video(message["video_url"])

# 上传图片的逻辑
if uploaded_image:
    image_name = uploaded_image.name
    image = Image.open(uploaded_image)
    resized_image = image.resize((300, 300))  # 调整图片大小

    # 避免重复添加图片
    if not any(msg.get("name") == image_name for msg in st.session_state.messages):
        st.session_state.messages.append({
            "role": "user",
            "name": image_name,
            "image": resized_image,
            "content": f"[您上传的图片为: {image_name}]"
        })
    st.session_state.uploaded_images.append(image_name)  # 记录图片名称


    # 显示上传的图片
    with st.chat_message("user"):
        st.image(resized_image, caption=f"上传的图片：{image_name}")


# 模拟生成助手回复
def response(prompt_input):
    result = {
        "text": "",
        "image_url": None,
        "video_url": None
    }
    # 如果上传了图片，则根据用户输入生成视频
    if st.session_state.uploaded_images:  # 如果有图片上传
        result["text"] = "运行成功！生成的视频如下："
        result["video_url"] = r"D:\doc\sora_chat\result\圣诞节.mp4"
        result["summary"] = (
            "这个视频描绘了一个温馨的圣诞节场景。画面中的红色沙发上摆放着五颜六色的礼物，旁边是装饰精美的圣诞树，树上挂满了闪烁的灯饰和红色的圣诞球。窗外可以看到雪景，增添了一份冬日的氛围。房间内还有一个装饰着圣诞饰品的壁炉，火光温暖，营造出节日的温馨感。整体色调温暖，充满了圣诞节的欢乐气氛。"
        )
        # 清空已上传的图片
        st.session_state.uploaded_images.clear()
    elif "宁静的夜晚" in prompt_input:
        result["text"] = "运行成功！生成的视频如下："
        result["video_url"] = r"D:\doc\sora_chat\result\宁静的夜晚.mp4"
        # 假设每个视频生成后会生成相应的摘要
        result["summary"] = (
            "这个视频描绘了一个宁静的夜晚景象。画面中，璀璨的星空布满了闪烁的星星，银河清晰可见，从画面的上方延伸至中部，仿佛一条明亮的星河横跨天际。下方是一片平静的湖水，湖水在星光的映照下泛着微光，显得格外静谧。湖边和远处的山峦被夜色笼罩，呈现出深色调，只有轮廓隐约可见。湖边的植被也沉浸在黑暗中，只有一些微弱的反光显示出它们的存在。整个画面给人一种宁静、祥和的感觉，仿佛置身于远离喧嚣的世外桃源。"
        )
    elif "日落" in prompt_input:
        result["text"] = "运行成功！生成的图片如下："
        result["image_url"] = r"D:\doc\sora_chat\result\日落.png"
        result["summary"] = (
            "这个图片展现了一个壮丽的日落景象，阳光的射线向四周辐射，形成了戏剧性而温暖的效果。云朵散布在天空中，部分被阳光照亮，前景中的山丘和远处的山脉轮廓清晰，营造出一种宁静而宏伟的氛围。"
        )
    # elif "niko" in prompt_input:
    #     result["text"] = "运行成功！生成的图片如下："
    #     result["image_url"] = r"D:\doc\sora_chat\微信图片_20241217192705.jpg"
    #     result["summary"] = (
    #        "这是对 cs2 现役选手 niko 的照片，表达了他遗憾于从未获得 major 冠军的遗憾。"
    #     )

    else:
        result["text"] = "请正确输入文本或图片哦！"
    return result

# 处理用户输入的文本
if prompt := st.chat_input():
    # 追加用户输入到消息历史
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    header_placeholder = st.empty()
    header_placeholder.header("视讯灵眸小助手正在思考..", divider="rainbow")
    # 显示进度条
    progress_bar = st.progress(0)
    progress_text = st.empty()
    progress = 0
    progress_step = 5

    while progress < 80:
        time.sleep(0.1)
        progress += progress_step
        progress_bar.progress(progress)
        progress_text.text(f"{progress}% 完成")

    time.sleep(3)
    progress_bar.progress(100)
    progress_text.text("视讯灵眸小助手完成思考！")
    header_placeholder.empty()

    # 生成助手回复
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            resp = response(prompt)
            full_response = resp["text"]

            # 构建消息内容并追加到 session_state.messages
            message_content = {"role": "assistant", "content": full_response}
            if resp.get("image_url"):
                message_content["image_url"] = resp["image_url"]
                # 保存生成的图片对应的摘要
                if "summary" in resp:
                    st.session_state.image_summaries[resp["image_url"]] = resp["summary"]
            if resp.get("video_url"):
                message_content["video_url"] = resp["video_url"]
                # 保存生成的视频对应的摘要
                if "summary" in resp:
                    st.session_state.video_summaries[resp["video_url"]] = resp["summary"]

            st.session_state.messages.append(message_content)

            # 显示助手的回复内容
            st.write(full_response)
            if resp.get("image_url"):
                st.image(resp["image_url"], caption="生成的图像")
            if resp.get("video_url"):
                st.video(resp["video_url"])

with st.sidebar:
    # 视频摘要展示
    st.subheader("视频摘要")
    if st.session_state.video_summaries:
        for video_url, summary in st.session_state.video_summaries.items():
            with st.expander(f"该视频的摘要描述为:"):
                st.write(summary)

    # st.write(st.session_state.image_summaries)
    # 图片摘要展示
    st.subheader("图片摘要")
    if st.session_state.image_summaries:
        for image_name, summary in st.session_state.image_summaries.items():
            with st.expander(f"该图片的摘要描述为:"):
                st.write(summary)
