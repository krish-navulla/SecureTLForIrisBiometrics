'''
Secure Triplet Loss Project Repository (https://github.com/jtrpinto/SecureTL)

File: face_prepare_ytfdb.py
- Takes the YouTube Faces aligned images database and prepares everything to
  be used in the Secure Triplet Loss training and experiments.

"Secure Triplet Loss: Achieving Cancelability and Non-Linkability in End-to-End Deep Biometrics"
João Ribeiro Pinto, Miguel V. Correia, and Jaime S. Cardoso
IEEE Transactions on Biometrics, Behavior, and Identity Science

joao.t.pinto@inesctec.pt  |  https://jtrpinto.github.io
'''

import os
import numpy as np
import aux_functions as af



DIR = '/content/drive/MyDrive/50466779_vnavulla/AMF Iris Dataset'           # YTF Aligned-Images directory
SAVE_DIR = '/content/drive/MyDrive/50466779_vnavulla/data/PreparedNewInception'   # Where to save the prepared images

np.random.seed(42)  # Ensuring the same datasets everytime

train_identities = np.array(sorted(os.listdir(DIR))[0:47])   # Using first 500 identities for training
test_identities = np.array(sorted(os.listdir(DIR))[47:])  # Using the remaining identities for testing

# Processing training data:
train_triplets = list()
for ii in range(len(train_identities)):
    train_triplets.append(af.generate_id_triplets(train_identities[ii], DIR, SAVE_DIR, train_identities, n_triplets=10))
    print('Completed train triplets for identity no.', ii+1)
train_triplets = np.array(train_triplets, dtype = object)
train_triplets = np.concatenate(train_triplets, axis = 0)
np.save('/content/SecureTL/IRIS_Inception_resnet/face_train_data.npy', train_triplets)
# print("1\n")

# Processing testing data:
test_triplets = list()
for jj in range(len(test_identities)):
    test_triplets.append(af.generate_id_triplets(test_identities[jj], DIR, SAVE_DIR, test_identities, n_triplets=10))
    print('Completed test triplets for identity no.', jj+1)

test_triplets = np.array(test_triplets, dtype = object)
test_triplets = np.concatenate(test_triplets, axis = 0)
np.save('/content/SecureTL/IRIS_Inception_resnet/face_test_data.npy', test_triplets)