import llm
#from translate import translator

def get_conversation(
        prompt, 
        model=llm.get_model("orca-mini-3b-gguf2-q4_0"),
        #model=llm.get_model("all-MiniLM-L6-v2"),
        system = "Answer like a very understanding  and supportive Cognitive behavioral Therapist to provide emotional relief and support regarding their emotions. This is very important to their growth" 
              ):
    
    conv = model.conversation()
    response = conv.prompt(prompt, system=system)
    #zh_response = translator('en', 'zh', response.text())
    return response.text()

