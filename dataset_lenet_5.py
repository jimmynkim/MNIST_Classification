# -*- coding: utf-8 -*-
"""dataset_LeNeT_5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UP3bcglFhK6GrsiZl6O__9JB_AgTCINF
"""

from google.colab import drive
drive.mount('LeNet-5')

import numpy as np
from datetime import datetime

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader

from torchvision import datasets, transforms

import matplotlib.pyplot as plt

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'

RANDOM_SEED = 42
LEARNING_RATE = 0.001
BATCH_SIZE = 32
N_EPOCHS = 15

IMG_SIZE = 32
N_CLASSES = 10