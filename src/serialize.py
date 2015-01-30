import cPickle as pickle

class Serialize(object):

  def serialize(self, blob):
    try:
      data = pickle.dumps(blob)

#    except cPickle.UnpickleableError:
#      data UnpickleableError
    return data

  def deserialize(self, string):
    return pickle.loads(string)
