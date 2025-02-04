"""
import llm
#from translate import translator

def get_conversation(
        prompt, 
        model=llm.get_model("orca-mini-3b-gguf2-q4_0"),
        #model=llm.get_model("/Users/zhaowenlong/.cache/gpt4all/llama-2-7b-chat.Q6_K"),
        system = "Answer like a very understanding  and supportive Cognitive behavioral Therapist to provide emotional relief and support regarding their emotions. Always answer as helpfully as possible, while being safe. This is very important to their emotions" 
        ):
    
    conv = model.conversation()
    response = conv.prompt(prompt, system=system)
    #zh_response = translator('en', 'zh', response.text())
    return response.text()
"""

"""
from langchain.prompts import PromptTemplate
from langchain.llms import LlamaCpp
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import (
    StreamingStdOutCallbackHandler
)
"""

from llama_cpp import Llama
llm = Llama.from_pretrained(
    repo_id="lordjia/Llama-3-Cantonese-8B-Instruct",
    filename="llama3-cantonese-8b-instruct-q4_0.gguf",
)

messages = [
    {
        "role": "system",
        "content": "像一位非常理解和支持的認知行為治療師一樣回答，為他們的情緒提供情緒緩解和支持。在確保安全的情況下，始終盡可能提供有幫助的答案。這對他們的情緒非常重要" 
    },
]

user_history = []
def get_user_prompt(prompt):
    user_prompt = {
        "role": "user",
        "content": prompt
    }
    return user_prompt


def get_conversation(prompt):
    user_prompt = get_user_prompt(prompt)
    user_history.append(user_prompt)
    #print(user_history)
    messages.extend(user_history) 
    print(messages)

    response = llm.create_chat_completion(messages)
    """
        messages = 
        [
            {
                "role": "system",
                "content": "像一位非常理解和支持的認知行為治療師一樣回答，為他們的情緒提供情緒緩解和支持。在確保安全的情況下，始終盡可能提供有幫助的答案。這對他們的情緒非常重要" 
            },
            {
                "role": "user",
                "content": prompt
            },
        ]
        #print(messages)
    """
    #)
    
    print(response)
    answer = response["choices"][0]["message"]["content"]
    #print(f'response: answer')
    print(f'history: {user_history}')
    if answer:
        return answer
    else:
        return prompt + "?"

if __name__ == "__main__":
    #prompt="I feel a bit tired today"
    prompt1="我感到很難放鬆自己"
    prompt2="我對任何事也沒有熱衷"
    """
    messages = [
            {
                "role": "system",
                "content": "像一位非常理解和支持的認知行為治療師一樣回答，為他們的情緒提供情緒緩解和支持。在確保安全的情況下，始終盡可能提供有幫助的答案。這對他們的情緒非常重要" 
            },
            {
                "role": "user",
                "content": prompt1
            },
            {
                "role": "user",
                "content": prompt2
            },
        ]
    """

    get_conversation(prompt1)
