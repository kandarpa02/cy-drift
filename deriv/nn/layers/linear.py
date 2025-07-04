from deriv.Array.backend import get_backend
from deriv.Array.array_object import array
from deriv.nn.module import Parameter, Module

class dense(Module):
    """
    Fully connected (dense) neural network layer.

    This layer performs a linear transformation on the input: `output = x @ W + b`.

    Attributes:
        w (Parameter): Weight matrix of shape (in_features, out_features), trainable.
        b (Parameter): Bias vector of shape (out_features,), trainable.

    Methods:
        __call__(x): Applies the linear transformation to the input tensor.
    """

    def __init__(self, in_features, out_features, var_name=''):
        xp = get_backend()
        """
        Initialize the dense layer with given input and output feature sizes.

        Args:
            in_features (int): Number of input features.
            out_features (int): Number of output features.
            var_name (str): Optional, use to see the graph put the name of the variable you used.
        """
        super().__init__()
        w = array(xp.random.randn(in_features, out_features) * 0.1, need_grad=True, var_name=f"{var_name}w")
        b = array(xp.zeros(out_features), need_grad=True, var_name=f"{var_name}b")
        self.w = Parameter(w)
        self.b = Parameter(b)

    def __call__(self, x):
        """
        Apply the linear transformation to the input.

        Args:
            x (array or np.ndarray): Input tensor of shape (batch_size, in_features).

        Returns:
            array: Output tensor of shape (batch_size, out_features).
        """
        if not isinstance(x, array):
            x = array(x)
        return x @ self.w.data + self.b.data
