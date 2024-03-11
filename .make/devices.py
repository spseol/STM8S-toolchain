URL = "https://www.st.com/resource/en/datasheet/{device}.pdf"

DEVICES = {
    "Value line (00X)": {
        "STM8S001J3": "stm8s001j3",
        "STM8S003K3": "stm8s001f3",
        "STM8S003K3": "stm8s001f3",
        "STM8S005C6": "stm8s001c6",
        "STM8S005K6": "stm8s001c6",
        "STM8S007C8": "stm8s001c8",
    },
    "Access line (103/105)": {
        "STM8S103F2": "stm8s103f2",
        "STM8S103F3": "stm8s103f2",
        "STM8S103K3": "stm8s103f2",
        "STM8S103C4": "stm8s105c4",
        "STM8S103C6": "stm8s105c4",
        "STM8S103K4": "stm8s105c4",
        "STM8S103K6": "stm8s105c4",
        "STM8S103S4": "stm8s105c4",
        "STM8S103S6": "stm8s105c4",
    },
    "Performance line (207/208)": {
        "STM8S207C6": "stm8s207mb",
        "STM8S207C8": "stm8s207mb",
        "STM8S207CB": "stm8s207mb",
        "STM8S207K6": "stm8s207mb",
        "STM8S207K8": "stm8s207mb",
        "STM8S207M8": "stm8s207mb",
        "STM8S207MB": "stm8s207mb",
        "STM8S207R6": "stm8s207mb",
        "STM8S207R8": "stm8s207mb",
        "STM8S207RB": "stm8s207mb",
        "STM8S207S6": "stm8s207mb",
        "STM8S207S8": "stm8s207mb",
        "STM8S207SB": "stm8s207mb",
        "STM8S208C6": "stm8s207mb",
        "STM8S208C8": "stm8s207mb",
        "STM8S208CB": "stm8s207mb",
        "STM8S208MB": "stm8s207mb",
        "STM8S208R8": "stm8s207mb",
        "STM8S208RB": "stm8s207mb",
        "STM8S208S6": "stm8s207mb",
    },
}

datasheets = {}
for familly in DEVICES:
    for device in DEVICES[familly]:
        datasheets[device] = URL.format(device=DEVICES[familly][device])

if __name__ == "__main__":
    print(datasheets)
