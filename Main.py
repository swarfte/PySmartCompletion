import PSCTool.kyeboardListener as PSCTKL
def start():
    listener = PSCTKL.ListenerThread()
    listener.start()

if __name__ == "__main__":
    start()