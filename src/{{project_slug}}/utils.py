"""Utilities module."""

from beartype import beartype
import numpy.typing as npt
from typing import Any


def add_one(a: int) -> int:
    """Function that adds one to an integer."""
    return a + 1


@beartype
def add_two(a: int) -> int:
    """Function that adds two to an integer."""
    return a + 2


def patchify_images(x_BCHW: npt.NDArray[Any], patch_size: int) -> npt.NDArray[Any]:
    """Function that reshapes images into patches e.g. for a Vision Transformer.

    Rearranges images from : B C H W -> B P F, where P is the number of patches and F is the resulting feature dimension.
    Each 'patch' is a flattened vector of all channels for a small, non-overlapping p x p image region.

    Based on: https://github.com/lucidrains/vit-pytorch/blob/9f49a31977688fd05b5c87b7d25fdce2498ec419/vit_pytorch/vit.py#L96
    """
    B, C, H, W = x_BCHW.shape
    p = patch_size

    # Number of patches in height and width dimensions
    H_patches = H // p
    W_patches = W // p

    # Reshape to extract patches
    # First reshape to (B, C, H_patches, p, W_patches, p)
    x_reshaped = x_BCHW.reshape(B, C, H_patches, p, W_patches, p)

    # Then transpose to (B, H_patches, W_patches, C, p, p)
    x_transposed = x_reshaped.transpose(0, 2, 4, 1, 3, 5)

    # Finally reshape to (B, H_patches * W_patches, C * p * p)
    x_BPF = x_transposed.reshape(B, H_patches * W_patches, C * p * p)

    return x_BPF
