import tensorflow as tf

class Model:
    __init__(self, session, input_size, output_size, name):
        self.sess = session
        self.input_size = input_size
        self.output_size = output_size
        self.net_name = name

        _build_network()

    _build_network(self):
        