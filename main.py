import streamlit as st
import requests
import json


url="http://localhost:11434/api/generate"

st.header("Code Pro")
st.subheader("Musician 9DX")

headers={

    "Content-Type":"application/json"
}

def getResponse(prompt):

    st.info(prompt)

    data={

        "model":"codepro",
        "prompt":prompt,
        "stream":False

    }

    response=requests.post(url,headers=headers,data=json.dumps(data))

    st.info(json.loads(response.text)["response"])


text_input=st.text_input("Give Input")
btn=st.button("Yes")

if btn:

    getResponse(text_input)