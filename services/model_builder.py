
from model import TinyVGG


class BuildModel():
    """BuildModel Builds model based on model class in model.py

    Arguments:
    device -- device where the model will we allocated (cuda-cpu)
    input_shape -- number of channels for image (3, 1)
    output_shape -- number of classes
    hidden_units -- number of hidden units per layer
    """

    def __init__(self, device: str,
                 input_shape: int,
                 output_shape,
                 hidden_units: int):
        self.device = device
        self.input_shape = input_shape
        self.output_shape = output_shape
        self.hidden_units = hidden_units

    def build_model(self):
        """build_model builds model.

        Returns:
            model: returns model with given parameters
        """
        model = TinyVGG(input_shape=self.input_shape,
                        output_shape=self.output_shape,
                        hidden_units=self.hidden_units).to(self.device)
        return model
