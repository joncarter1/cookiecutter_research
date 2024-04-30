#!/usr/bin/env python

"""Tests for example package."""
import beartype
import os
import numpy as np
import pytest

from {{cookiecutter.project_slug}}.utils import func, func2, patchify_images

@pytest.fixture(scope='function')  # https://docs.pytest.org/en/6.2.x/fixture.html#fixture-scopes
def my_fixture():
    """Example fixture.

    Fixtures are used to create pre-conditions, set-up
    and tear down a test. For example, to prepare some
    data or the system environment before the actual test.
    """
    # Fixtures can be used to configure the test environment.
    os.environ['MY_VAL'] = '1'
    # Fixtures can provide data to a test.
    yield 2
    # Tear-down can be performed after a yield to restore state.
    del os.environ['MY_VAL']


def test_env_var_is_set(my_fixture):
    assert os.environ['MY_VAL'] == '1'
    assert my_fixture == 2
    assert func(my_fixture) == 3


def test_func2():
    """Check func2 explodes when not given an integer."""
    with pytest.raises(beartype.roar.BeartypeCallHintParamViolation):
        func2("Not an integer")
		
# Parametrize over batch, channels, height, width, patch size
@pytest.mark.parametrize("B, C, H, W, p", [
    (2, 3, 8, 8, 2),
    (1, 1, 4, 4, 2),
    (4, 2, 4, 4, 4),
    (1, 1, 4, 4, 1),
]) # https://docs.pytest.org/en/6.2.x/parametrize.html
def test_patchification_shape(B, C, H, W, p):
    """Check that the shape of the patched output is as expected."""
    x_BCHW = np.random.normal(size=(B, C, H, W))
    x_BPF = patchify_images(x_BCHW, p)
    assert x_BPF.shape == (B, H//p * W//p, p*p*C)

# Parametrize over batch, channels, height, width, patch size
@pytest.mark.parametrize("B, C, H, W, p", [
    (2, 3, 8, 8, 2),
    (8, 2, 32, 32, 4),
    (7, 1, 4, 4, 2),
    (9, 7, 4, 4, 1),
]) # https://docs.pytest.org/en/6.2.x/parametrize.html
def test_first_top_corner_patch_contents(B, C, H, W, p):
    """Check that the top-left corner of the first image in the batch has the
    same contents as the first patch-level feature vector."""
    x_BCHW = np.random.normal(size=(B, C, H, W))
    x_BPF = patchify_images(x_BCHW, p)
    assert set(x_BPF[0, 0, :].flatten()) == set(x_BCHW[0, :, :p, :p].flatten())

# Parametrize over batch, channels, height, width, patch size
@pytest.mark.parametrize("B, C, H, W, p", [
    (2, 3, 8, 8, 2),
    (8, 2, 32, 32, 4),
    (7, 1, 4, 4, 2),
    (9, 7, 4, 4, 1),
]) # https://docs.pytest.org/en/6.2.x/parametrize.html
def test_last_bottom_corner_patch_contents(B, C, H, W, p):
    """Check that the bottom-right corner of the last image in the batch has the
    same contents as the last patch feature vector."""
    x_BCHW = np.random.normal(size=(B, C, H, W))
    x_BPF = patchify_images(x_BCHW, p)
    assert set(x_BPF[-1, -1, :].flatten()) == set(x_BCHW[-1, :, -p:, -p:].flatten())