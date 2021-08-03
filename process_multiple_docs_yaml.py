import yaml

if __name__ == '__main__':
    stream = open("arrays.yaml", 'r')
    dictionary = yaml.load_all(stream, Loader=yaml.FullLoader)

    for doc in dictionary:
        print("New document:")
        for key, value in doc.items():
            print(key + " : " + str(value))
            if type(value) is list:
                print(str(len(value)))