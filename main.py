import requests
import copy
import json

history = list()
while True:
    inputStr = input(">>> ")
    historyTmp = copy.deepcopy(history)
    history.append({"role":"user","content":inputStr})
    result = requests.post("https://cursor.sh/api/chat/stream", data=json.dumps({"prompt":json.dumps({"history":history}), "history":historyTmp})).content.decode("utf-8")
    history.append({"role":"system","content":result})
    print(result)
