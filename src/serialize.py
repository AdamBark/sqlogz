import cPickle as pickle

class Serialize(object):

  def serialize(self, blob):
    try:
      data = pickle.dumps(blob)

    except pickle.UnpickleableError:
      data = "unpickableerror"

    return data

  def deserialize(self, string):
    return pickle.loads(string)
