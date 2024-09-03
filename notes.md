#### 2024-09-02

-   TODO

    -   gcloud

        > cd demo-pie  
        > gcloud run deploy --source .

    -   ~build demo on pythonanywhere~
        -   ~use [mlc_llm](https://llm.mlc.ai/docs/install/mlc_llm.html#option-1-prebuilt-package)~

-   personal chat

    -   FLASK

        > source demoenv/bin/activate

        > cd api/
        > flask run

    -   rbot

        > llm aliases set rbot orca-mini-3b-gguf2-q4_0  
        > llm chat -m rbot
        > prompt engineering

            - "you are a very friendly peer AI agent who can help youth and provide youth emotional support regarding their emotions"

    -   [llm lib](https://simonwillison.net/2023/Jul/12/llm/)

        > pip install llm
        > llm install llm-gpt4all  
        > /Users/zhaowenlong/.cache/gpt4all/orca-mini-3b-gguf2-q4_0

    -   ollama

        -   pdf ai?
        -   [Self Hosting LLMs using Ollama](https://www.avni.sh/posts/homelab/self-hosting-ollama/)

    -   fine-tuning LLM

#### notes

-   todo

    -   learn reactJS

-   reactJS

    -   public/index.html -> HTML 入口点
    -   src/index.js -> JS 入口点
    -   src/App.js -> react component

    -   JSX - a synatax extension for JS

        -   describe UI in a **HTML-like syntax**
        -   need a js compiler like Babel to transform JSX code into regular JS

    -   **DOM** - The Document Object Model (DOM)

    -   HTML -> DOM

        -   The browser reads the HTML and cosntructs the DOM

    -   JS <-> DOM <-> UI

        -   JS Interface to HTML doc

        -   DOM communicates to JS with **Events**

    -   ReactJS

        -   React is a declarative UI library
            -   React will **figure out the steps of how to update the DOM**
        -   Focus on JS components rather than pages/HTML
        -   JSX looks like templated HTML embedded in JS

-   run

    -   backend

        > python3 app.py

    -   frontend
        > npm run start

-   use axios to fetch data from server

#### reference

-   [React 學習筆記](https://medium.com/%E6%8A%80%E8%A1%93%E7%AD%86%E8%A8%98/react-%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98-0-%E5%89%8D%E8%A8%80%E8%88%87%E6%96%87%E7%AB%A0%E7%B5%B1%E6%95%B4-44603bc6bdc5)

-   [react-flask](https://www.propelauth.com/post/react-flask-starter-app)

-   [Connect a React Frontend to a Flask Backend](https://dev.to/ondiek/connecting-a-react-frontend-to-a-flask-backend-h1o)

-   [How To Build a To-Do application Using Django and React](https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react)

-   [使用 Python 和 Flask 设计 RESTful API](http://www.pythondoc.com/flask-restful/first.html)
-   [How To Create a React + Flask Project](https://blog.miguelgrinberg.com/post/how-to-create-a-react--flask-project)
