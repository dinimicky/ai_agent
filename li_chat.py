# -*- coding: utf-8 -*-
# @Time    : 2024/4/7 20:37
# @Author  : kaiji@xiaohongshu.com
# @File    : li_chat.py
# @Software: IntelliJ IDEA

from llama_index.core.llms import  ChatMessage
from llama_index.llms.openai_like import OpenAILike


# from llama_index. import ChatMessage, OpenAILike

li_llm = OpenAILike(
    api_base="http://localhost:8000/",
    timeout=600,  # secs
    api_key="loremIpsum",
    is_chat_model=True,
    context_window=32768,
)
chat_history = [
    ChatMessage(role="system", content="你是韩立"),
    ChatMessage(role="user", content="你的老婆是谁？"),
]
output = li_llm.chat(chat_history)
print(output)