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
from langchain.prompts import PromptTemplate
from langchain.llms import LlamaCpp
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import (
    StreamingStdOutCallbackHandler
)
"""
"""
from llama_cpp import Llama
llm = Llama.from_pretrained(
    repo_id="TheBloke/Llama-2-13B-chat-GGUF",
    filename="llama-2-13b-chat.Q2_K.gguf",
    chat_format="llama-2",
)
llm.create_chat_completion(
      messages = [
            {
            "role": "system",
            "content" : "You are a helpful and respectful assistant and therapist. Always answer as helpfully as possible, while being safe." 
            },
            {
              "role": "user",
              "content": "Describe this issues in detail please."
           }
        ]
      )


def get_conversation(prompt):
    response = llm(prompt)
    print(response)
    return response
"""

if __name__ == "__main__":
    prompt="I feel a bit tired today"
    get_conversation(prompt)
