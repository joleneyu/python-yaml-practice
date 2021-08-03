import yaml

if __name__ == '__main__':

    stream = open("string_type.yaml", 'r')
    dictionary = yaml.load(stream, Loader=yaml.FullLoader)
    for key, value in dictionary.items():
        print (key + " : " + str(value))