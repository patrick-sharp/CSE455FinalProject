#https://github.com/etown/dl1/blob/master/UrbanSoundClassification.ipynb

import os
import glob
import shutil
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.pyplot import specgram
import librosa
import numpy as np
from fastai import *
from fastai.vision import *



labels  = ['air_conditioner','car_horn','children_playing',
           'dog_bark','drilling','engine_idling','gun_shot','jackhammer','siren','street_music']

