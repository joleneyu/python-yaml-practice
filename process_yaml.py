import yaml

if __name__ == '__main__':

    stream = open("foo.yaml", 'r')
    dictionary = yaml.load(stream, Loader=yaml.FullLoader)
    for key, value in dictionary.items():
        print (key + " : " + str(value))