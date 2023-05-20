'''
Secure Triplet Loss Project Repository (https://github.com/jtrpinto/SecureTL)

File: face_test_triplet_model.py
- Uses the face test data to evaluate models trained with the original triplet loss.

  REQUIRES:
  - facenet_pytorch package by Tim Esler
    (https://github.com/timesler/facenet-pytorch)

"Secure Triplet Loss: Achieving Cancelability and Non-Linkability in End-to-End Deep Biometrics"
João Ribeiro Pinto, Miguel V. Correia, and Jaime S. Cardoso
IEEE Transactions on Biometrics, Behavior, and Identity Science

joao.t.pinto@inesctec.pt  |  https://jtrpinto.github.io
'''

import os
import torch
import numpy as np
import pickle as pk
from models import TripletModel, TripletFaceNetwork, TripletIrisNetwork
from losses import TripletLoss
from dataset import TripletFaceDataset
from facenet_pytorch import InceptionResnetV1
from torch.utils.data import DataLoader
from eval import evaluate_triplet_model

import facenet_pytorch
from facenet_pytorch.models.inception_resnet_v1 import InceptionResnetV1
from facenet_pytorch.models.inception_resnet_v1 import BasicConv2d


DEVICE = 'cuda:0' if torch.cuda.is_available() else 'cpu'

MODEL = 'triplet_iris_model'
TEST_DATA = 'face_test_data.npy'

BATCH_SIZE = 32

print('Testing model: ' + MODEL)

# Preparing the dataset
testset = TripletFaceDataset(TEST_DATA)
test_loader = DataLoader(testset, batch_size=BATCH_SIZE, shuffle=False, num_workers=4)


# Creating the model
# pretrained = InceptionResnetV1(pretrained='vggface2')
# pretrained.conv2d_1a = BasicConv2d(1, 32, kernel_size=3, stride=2)

network = TripletIrisNetwork(dropout_prob = 0.5).to(DEVICE)
model = TripletModel(network)

# Loading saved weights
model.load_state_dict(torch.load(MODEL + '.pth', map_location=DEVICE))
model = model.to(DEVICE)

# Evaluating the model on test data
output = evaluate_triplet_model(model, test_loader, BATCH_SIZE, DEVICE, N=10000, debug=True)

# Saving the results to a pickle
with open(os.path.basename(MODEL) + '_results.pk', 'wb') as hf:
    pk.dump(output, hf)

# Printing the main results
print('EER {:.4f} at threshold {:.4f}'.format(output[0]['eer'][1], output[0]['eer'][0]))
print('Privacy Leakage Rate {:.4f}'.format(output[1]['plr']))

