"""Utils module."""
from beartype import beartype
import numpy.typing as npt
import os
from typing import Any

def load_env_var():
    os.environ['SECRET_KEY'] = 'password'  # ruff will warn of a hard-coded password.

def func(a: int) -> str:  # mypy will raise an error - bad type hints.
    """Function that adds one to an integer."""
    b = 7  # ruff will raise an error - variable assigned but unused.
    return a + 1

# The function below will raise an error if anything other than an integer is passed/returned thanks to beartype.
@beartype
def func2(a: int) -> int:
    """Function that adds two to an integer."""
    return a + 2

def patchify_images(x_BCHW: npt.NDArray[Any], patch_size: int) -> npt.NDArray[Any]:
    """Function that reshapes images into patches e.g. for a Vision Transformer.

    Rearranges images from : B C H W -> B P F, where P is the number of patches and F is the resulting feature dimension.
    Each 'patch' is a flattened vector of all channels for a small, non-overlapping p x p image region.
	
	THE CODE IN THIS FUNCTION WAS GENERATED BY COPILOT AND IS NOT CORRECT.
    
	A correct implementation should pass the simple tests defined in tests/test_utils.py.
    e.g. https://github.com/lucidrains/vit-pytorch/blob/9f49a31977688fd05b5c87b7d25fdce2498ec419/vit_pytorch/vit.py#L96
    """
    num_patches = (x_BCHW.shape[2] // patch_size) * (x_BCHW.shape[3] // patch_size)
    x_BPF = x_BCHW.reshape(x_BCHW.shape[0], num_patches, -1)
    return x_BPF