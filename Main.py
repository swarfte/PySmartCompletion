import PSCTool.KBListener as PK

def setup(config):
    test = PK.KBListener(config)
    test.start()

if __name__ == "__main__":
    path = "./config/setting.json"
    setup(path)