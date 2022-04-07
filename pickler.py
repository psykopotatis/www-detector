import pickle


def dump(filename, obj):
    with open(filename, 'wb') as fobj:
        pickle.dump(obj, fobj)


def load(filename, default):
    try:
        with open(filename, 'rb') as fobj:
            return pickle.load(fobj)
    except IOError:
        return default
