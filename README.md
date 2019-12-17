# Intent-Classification

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
embedding_layer (Embedding)  (None, 25, 50)            20000000  
_________________________________________________________________
bidirectional_3 (Bidirection (None, 256)               183296    
_________________________________________________________________
dense_5 (Dense)              (None, 32)                8224      
_________________________________________________________________
dropout_3 (Dropout)          (None, 32)                0         
_________________________________________________________________
dense_6 (Dense)              (None, 21)                693       
=================================================================
Total params: 20,192,213
Trainable params: 192,213
Non-trainable params: 20,000,000
_________________________________________________________________
Train on 890 samples, validate on 223 samples
Epoch 1/100
890/890 [==============================] - 8s 9ms/step - loss: 2.9512 - acc: 0.1247 - val_loss: 2.8631 - val_acc: 0.1614

Epoch 00001: val_loss improved from inf to 2.86313, saving model to model.h5
Epoch 2/100
890/890 [==============================] - 3s 3ms/step - loss: 2.8350 - acc: 0.1742 - val_loss: 2.7171 - val_acc: 0.1614

Epoch 00002: val_loss improved from 2.86313 to 2.71712, saving model to model.h5
Epoch 3/100
890/890 [==============================] - 3s 3ms/step - loss: 2.6233 - acc: 0.2090 - val_loss: 2.4071 - val_acc: 0.2870

Epoch 00003: val_loss improved from 2.71712 to 2.40714, saving model to model.h5
Epoch 4/100
890/890 [==============================] - 3s 3ms/step - loss: 2.4148 - acc: 0.2820 - val_loss: 2.1029 - val_acc: 0.3274

Epoch 00004: val_loss improved from 2.40714 to 2.10293, saving model to model.h5
Epoch 5/100
890/890 [==============================] - 3s 3ms/step - loss: 2.1107 - acc: 0.3449 - val_loss: 1.8114 - val_acc: 0.4933

Epoch 00005: val_loss improved from 2.10293 to 1.81136, saving model to model.h5
Epoch 6/100
890/890 [==============================] - 3s 3ms/step - loss: 1.9726 - acc: 0.4000 - val_loss: 1.7013 - val_acc: 0.5247

Epoch 00006: val_loss improved from 1.81136 to 1.70128, saving model to model.h5
Epoch 7/100
890/890 [==============================] - 3s 3ms/step - loss: 1.7589 - acc: 0.4629 - val_loss: 1.4608 - val_acc: 0.5561

Epoch 00007: val_loss improved from 1.70128 to 1.46077, saving model to model.h5
Epoch 8/100
890/890 [==============================] - 3s 3ms/step - loss: 1.6002 - acc: 0.5090 - val_loss: 1.3149 - val_acc: 0.5964

Epoch 00008: val_loss improved from 1.46077 to 1.31488, saving model to model.h5
Epoch 9/100
890/890 [==============================] - 3s 3ms/step - loss: 1.4543 - acc: 0.5618 - val_loss: 1.1934 - val_acc: 0.6861

Epoch 00009: val_loss improved from 1.31488 to 1.19345, saving model to model.h5
Epoch 10/100
890/890 [==============================] - 3s 3ms/step - loss: 1.3589 - acc: 0.5989 - val_loss: 1.0676 - val_acc: 0.7085

Epoch 00010: val_loss improved from 1.19345 to 1.06757, saving model to model.h5
Epoch 11/100
890/890 [==============================] - 3s 3ms/step - loss: 1.2015 - acc: 0.6315 - val_loss: 0.9536 - val_acc: 0.7534

Epoch 00011: val_loss improved from 1.06757 to 0.95357, saving model to model.h5
Epoch 12/100
890/890 [==============================] - 3s 3ms/step - loss: 1.1300 - acc: 0.6427 - val_loss: 0.9399 - val_acc: 0.7220

Epoch 00012: val_loss improved from 0.95357 to 0.93993, saving model to model.h5
Epoch 13/100
890/890 [==============================] - 3s 3ms/step - loss: 1.0574 - acc: 0.6708 - val_loss: 0.8644 - val_acc: 0.7444

Epoch 00013: val_loss improved from 0.93993 to 0.86437, saving model to model.h5
Epoch 14/100
890/890 [==============================] - 3s 3ms/step - loss: 0.9993 - acc: 0.6910 - val_loss: 0.7862 - val_acc: 0.7713

Epoch 00014: val_loss improved from 0.86437 to 0.78621, saving model to model.h5
Epoch 15/100
890/890 [==============================] - 3s 3ms/step - loss: 0.9176 - acc: 0.7157 - val_loss: 0.7527 - val_acc: 0.7713

Epoch 00015: val_loss improved from 0.78621 to 0.75265, saving model to model.h5
Epoch 16/100
890/890 [==============================] - 3s 3ms/step - loss: 0.8644 - acc: 0.7258 - val_loss: 0.7245 - val_acc: 0.7892

Epoch 00016: val_loss improved from 0.75265 to 0.72453, saving model to model.h5
Epoch 17/100
890/890 [==============================] - 3s 3ms/step - loss: 0.8191 - acc: 0.7303 - val_loss: 0.7257 - val_acc: 0.7668

Epoch 00017: val_loss did not improve from 0.72453
Epoch 18/100
890/890 [==============================] - 3s 3ms/step - loss: 0.7452 - acc: 0.7584 - val_loss: 0.7403 - val_acc: 0.7713

Epoch 00018: val_loss did not improve from 0.72453
Epoch 19/100
890/890 [==============================] - 3s 3ms/step - loss: 0.7282 - acc: 0.7753 - val_loss: 0.6822 - val_acc: 0.7982

Epoch 00019: val_loss improved from 0.72453 to 0.68217, saving model to model.h5
Epoch 20/100
890/890 [==============================] - 3s 3ms/step - loss: 0.6680 - acc: 0.8022 - val_loss: 0.6433 - val_acc: 0.8072

Epoch 00020: val_loss improved from 0.68217 to 0.64329, saving model to model.h5
Epoch 21/100
890/890 [==============================] - 3s 3ms/step - loss: 0.6311 - acc: 0.7978 - val_loss: 0.6722 - val_acc: 0.7758

Epoch 00021: val_loss did not improve from 0.64329
Epoch 22/100
890/890 [==============================] - 3s 3ms/step - loss: 0.6636 - acc: 0.7843 - val_loss: 0.6183 - val_acc: 0.8161

Epoch 00022: val_loss improved from 0.64329 to 0.61830, saving model to model.h5
Epoch 23/100
890/890 [==============================] - 3s 3ms/step - loss: 0.6623 - acc: 0.7921 - val_loss: 0.5702 - val_acc: 0.8161

Epoch 00023: val_loss improved from 0.61830 to 0.57021, saving model to model.h5
Epoch 24/100
890/890 [==============================] - 3s 3ms/step - loss: 0.5973 - acc: 0.8079 - val_loss: 0.6161 - val_acc: 0.8027

Epoch 00024: val_loss did not improve from 0.57021
Epoch 25/100
890/890 [==============================] - 3s 3ms/step - loss: 0.5672 - acc: 0.8180 - val_loss: 0.5712 - val_acc: 0.8341

Epoch 00025: val_loss did not improve from 0.57021
Epoch 26/100
890/890 [==============================] - 3s 3ms/step - loss: 0.5630 - acc: 0.8303 - val_loss: 0.5447 - val_acc: 0.8386

Epoch 00026: val_loss improved from 0.57021 to 0.54468, saving model to model.h5
Epoch 27/100
890/890 [==============================] - 3s 3ms/step - loss: 0.5172 - acc: 0.8371 - val_loss: 0.5817 - val_acc: 0.8206

Epoch 00027: val_loss did not improve from 0.54468
Epoch 28/100
890/890 [==============================] - 3s 3ms/step - loss: 0.5439 - acc: 0.8135 - val_loss: 0.6455 - val_acc: 0.8117

Epoch 00028: val_loss did not improve from 0.54468
Epoch 29/100
890/890 [==============================] - 3s 3ms/step - loss: 0.4795 - acc: 0.8539 - val_loss: 0.5534 - val_acc: 0.8341

Epoch 00029: val_loss did not improve from 0.54468
Epoch 30/100
890/890 [==============================] - 3s 3ms/step - loss: 0.4909 - acc: 0.8404 - val_loss: 0.6047 - val_acc: 0.8475

Epoch 00030: val_loss did not improve from 0.54468
Epoch 31/100
890/890 [==============================] - 3s 3ms/step - loss: 0.4223 - acc: 0.8753 - val_loss: 0.5668 - val_acc: 0.8475

Epoch 00031: val_loss did not improve from 0.54468
Epoch 32/100
890/890 [==============================] - 3s 3ms/step - loss: 0.4389 - acc: 0.8472 - val_loss: 0.5404 - val_acc: 0.8610

Epoch 00032: val_loss improved from 0.54468 to 0.54042, saving model to model.h5
Epoch 33/100
890/890 [==============================] - 3s 3ms/step - loss: 0.3927 - acc: 0.8798 - val_loss: 0.5664 - val_acc: 0.8386

Epoch 00033: val_loss did not improve from 0.54042
Epoch 34/100
890/890 [==============================] - 3s 3ms/step - loss: 0.3966 - acc: 0.8685 - val_loss: 0.5363 - val_acc: 0.8475

Epoch 00034: val_loss improved from 0.54042 to 0.53626, saving model to model.h5
Epoch 35/100
890/890 [==============================] - 3s 3ms/step - loss: 0.3769 - acc: 0.8674 - val_loss: 0.5478 - val_acc: 0.8386

Epoch 00035: val_loss did not improve from 0.53626
Epoch 36/100
890/890 [==============================] - 3s 3ms/step - loss: 0.3675 - acc: 0.8854 - val_loss: 0.6317 - val_acc: 0.8430

Epoch 00036: val_loss did not improve from 0.53626
Epoch 37/100
890/890 [==============================] - 3s 3ms/step - loss: 0.3978 - acc: 0.8730 - val_loss: 0.5715 - val_acc: 0.8386

Epoch 00037: val_loss did not improve from 0.53626
Epoch 38/100
890/890 [==============================] - 3s 3ms/step - loss: 0.3596 - acc: 0.8753 - val_loss: 0.5210 - val_acc: 0.8565

Epoch 00038: val_loss improved from 0.53626 to 0.52100, saving model to model.h5
Epoch 39/100
890/890 [==============================] - 3s 3ms/step - loss: 0.3453 - acc: 0.8854 - val_loss: 0.5089 - val_acc: 0.8655

Epoch 00039: val_loss improved from 0.52100 to 0.50887, saving model to model.h5
Epoch 40/100
890/890 [==============================] - 3s 3ms/step - loss: 0.3601 - acc: 0.8820 - val_loss: 0.5250 - val_acc: 0.8655

Epoch 00040: val_loss did not improve from 0.50887
Epoch 41/100
890/890 [==============================] - 3s 3ms/step - loss: 0.3538 - acc: 0.8787 - val_loss: 0.4898 - val_acc: 0.8610

Epoch 00041: val_loss improved from 0.50887 to 0.48981, saving model to model.h5
Epoch 42/100
890/890 [==============================] - 3s 3ms/step - loss: 0.3363 - acc: 0.8843 - val_loss: 0.4492 - val_acc: 0.8610

Epoch 00042: val_loss improved from 0.48981 to 0.44920, saving model to model.h5
Epoch 43/100
890/890 [==============================] - 3s 3ms/step - loss: 0.3138 - acc: 0.8978 - val_loss: 0.5972 - val_acc: 0.8789

Epoch 00043: val_loss did not improve from 0.44920
Epoch 44/100
890/890 [==============================] - 3s 3ms/step - loss: 0.3969 - acc: 0.8607 - val_loss: 0.4873 - val_acc: 0.8700

Epoch 00044: val_loss did not improve from 0.44920
Epoch 45/100
890/890 [==============================] - 3s 3ms/step - loss: 0.3767 - acc: 0.8685 - val_loss: 0.4676 - val_acc: 0.8789

Epoch 00045: val_loss did not improve from 0.44920
Epoch 46/100
890/890 [==============================] - 3s 3ms/step - loss: 0.2885 - acc: 0.8978 - val_loss: 0.4796 - val_acc: 0.8789

Epoch 00046: val_loss did not improve from 0.44920
Epoch 47/100
890/890 [==============================] - 3s 3ms/step - loss: 0.3151 - acc: 0.8831 - val_loss: 0.4710 - val_acc: 0.8834

Epoch 00047: val_loss did not improve from 0.44920
Epoch 48/100
890/890 [==============================] - 3s 3ms/step - loss: 0.2892 - acc: 0.9034 - val_loss: 0.4452 - val_acc: 0.8789

Epoch 00048: val_loss improved from 0.44920 to 0.44524, saving model to model.h5
Epoch 49/100
890/890 [==============================] - 3s 3ms/step - loss: 0.3002 - acc: 0.8966 - val_loss: 0.4614 - val_acc: 0.8924

Epoch 00049: val_loss did not improve from 0.44524
Epoch 50/100
890/890 [==============================] - 3s 3ms/step - loss: 0.2689 - acc: 0.9124 - val_loss: 0.4783 - val_acc: 0.8744

Epoch 00050: val_loss did not improve from 0.44524
Epoch 51/100
890/890 [==============================] - 3s 4ms/step - loss: 0.2604 - acc: 0.9079 - val_loss: 0.4732 - val_acc: 0.8879

Epoch 00051: val_loss did not improve from 0.44524
Epoch 52/100
890/890 [==============================] - 3s 3ms/step - loss: 0.2685 - acc: 0.9056 - val_loss: 0.4574 - val_acc: 0.8789

Epoch 00052: val_loss did not improve from 0.44524
Epoch 53/100
890/890 [==============================] - 3s 3ms/step - loss: 0.3005 - acc: 0.8978 - val_loss: 0.5375 - val_acc: 0.8700

Epoch 00053: val_loss did not improve from 0.44524
Epoch 54/100
890/890 [==============================] - 3s 3ms/step - loss: 0.2459 - acc: 0.9135 - val_loss: 0.5310 - val_acc: 0.8789

Epoch 00054: val_loss did not improve from 0.44524
Epoch 55/100
890/890 [==============================] - 3s 3ms/step - loss: 0.2787 - acc: 0.9146 - val_loss: 0.4511 - val_acc: 0.8834

Epoch 00055: val_loss did not improve from 0.44524
Epoch 56/100
890/890 [==============================] - 3s 3ms/step - loss: 0.2216 - acc: 0.9292 - val_loss: 0.4950 - val_acc: 0.8834

Epoch 00056: val_loss did not improve from 0.44524
Epoch 57/100
890/890 [==============================] - 3s 3ms/step - loss: 0.2174 - acc: 0.9202 - val_loss: 0.4687 - val_acc: 0.8924

Epoch 00057: val_loss did not improve from 0.44524
Epoch 58/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1907 - acc: 0.9337 - val_loss: 0.4804 - val_acc: 0.8969

Epoch 00058: val_loss did not improve from 0.44524
Epoch 59/100
890/890 [==============================] - 3s 3ms/step - loss: 0.2009 - acc: 0.9270 - val_loss: 0.4387 - val_acc: 0.8879

Epoch 00059: val_loss improved from 0.44524 to 0.43874, saving model to model.h5
Epoch 60/100
890/890 [==============================] - 3s 4ms/step - loss: 0.1999 - acc: 0.9236 - val_loss: 0.4598 - val_acc: 0.8879

Epoch 00060: val_loss did not improve from 0.43874
Epoch 61/100
890/890 [==============================] - 3s 3ms/step - loss: 0.2172 - acc: 0.9124 - val_loss: 0.4530 - val_acc: 0.8879

Epoch 00061: val_loss did not improve from 0.43874
Epoch 62/100
890/890 [==============================] - 3s 3ms/step - loss: 0.2024 - acc: 0.9225 - val_loss: 0.5088 - val_acc: 0.8969

Epoch 00062: val_loss did not improve from 0.43874
Epoch 63/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1969 - acc: 0.9337 - val_loss: 0.4675 - val_acc: 0.9013

Epoch 00063: val_loss did not improve from 0.43874
Epoch 64/100
890/890 [==============================] - 3s 3ms/step - loss: 0.2205 - acc: 0.9258 - val_loss: 0.4830 - val_acc: 0.8879

Epoch 00064: val_loss did not improve from 0.43874
Epoch 65/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1751 - acc: 0.9382 - val_loss: 0.4336 - val_acc: 0.8879

Epoch 00065: val_loss improved from 0.43874 to 0.43361, saving model to model.h5
Epoch 66/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1854 - acc: 0.9247 - val_loss: 0.5198 - val_acc: 0.8834

Epoch 00066: val_loss did not improve from 0.43361
Epoch 67/100
890/890 [==============================] - 3s 3ms/step - loss: 0.2099 - acc: 0.9315 - val_loss: 0.4854 - val_acc: 0.8789

Epoch 00067: val_loss did not improve from 0.43361
Epoch 68/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1828 - acc: 0.9326 - val_loss: 0.5802 - val_acc: 0.8834

Epoch 00068: val_loss did not improve from 0.43361
Epoch 69/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1814 - acc: 0.9393 - val_loss: 0.4878 - val_acc: 0.8834

Epoch 00069: val_loss did not improve from 0.43361
Epoch 70/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1809 - acc: 0.9427 - val_loss: 0.4977 - val_acc: 0.8924

Epoch 00070: val_loss did not improve from 0.43361
Epoch 71/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1977 - acc: 0.9281 - val_loss: 0.4997 - val_acc: 0.8879

Epoch 00071: val_loss did not improve from 0.43361
Epoch 72/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1735 - acc: 0.9303 - val_loss: 0.5043 - val_acc: 0.8924

Epoch 00072: val_loss did not improve from 0.43361
Epoch 73/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1657 - acc: 0.9382 - val_loss: 0.5301 - val_acc: 0.9013

Epoch 00073: val_loss did not improve from 0.43361
Epoch 74/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1731 - acc: 0.9528 - val_loss: 0.5835 - val_acc: 0.8969

Epoch 00074: val_loss did not improve from 0.43361
Epoch 75/100
890/890 [==============================] - 3s 3ms/step - loss: 0.2019 - acc: 0.9416 - val_loss: 0.4894 - val_acc: 0.9013

Epoch 00075: val_loss did not improve from 0.43361
Epoch 76/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1723 - acc: 0.9449 - val_loss: 0.5167 - val_acc: 0.9058

Epoch 00076: val_loss did not improve from 0.43361
Epoch 77/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1777 - acc: 0.9326 - val_loss: 0.5207 - val_acc: 0.8969

Epoch 00077: val_loss did not improve from 0.43361
Epoch 78/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1653 - acc: 0.9404 - val_loss: 0.4908 - val_acc: 0.9013

Epoch 00078: val_loss did not improve from 0.43361
Epoch 79/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1683 - acc: 0.9427 - val_loss: 0.4897 - val_acc: 0.9058

Epoch 00079: val_loss did not improve from 0.43361
Epoch 80/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1928 - acc: 0.9449 - val_loss: 0.4457 - val_acc: 0.8879

Epoch 00080: val_loss did not improve from 0.43361
Epoch 81/100
890/890 [==============================] - 3s 3ms/step - loss: 0.2237 - acc: 0.9213 - val_loss: 0.5696 - val_acc: 0.8879

Epoch 00081: val_loss did not improve from 0.43361
Epoch 82/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1687 - acc: 0.9449 - val_loss: 0.4210 - val_acc: 0.8969

Epoch 00082: val_loss improved from 0.43361 to 0.42095, saving model to model.h5
Epoch 83/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1635 - acc: 0.9506 - val_loss: 0.5362 - val_acc: 0.8834

Epoch 00083: val_loss did not improve from 0.42095
Epoch 84/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1500 - acc: 0.9483 - val_loss: 0.4780 - val_acc: 0.9013

Epoch 00084: val_loss did not improve from 0.42095
Epoch 85/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1382 - acc: 0.9562 - val_loss: 0.4510 - val_acc: 0.8879

Epoch 00085: val_loss did not improve from 0.42095
Epoch 86/100
890/890 [==============================] - 3s 3ms/step - loss: 0.2028 - acc: 0.9326 - val_loss: 0.6191 - val_acc: 0.8610

Epoch 00086: val_loss did not improve from 0.42095
Epoch 87/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1616 - acc: 0.9461 - val_loss: 0.5409 - val_acc: 0.8879

Epoch 00087: val_loss did not improve from 0.42095
Epoch 88/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1436 - acc: 0.9483 - val_loss: 0.4722 - val_acc: 0.9103

Epoch 00088: val_loss did not improve from 0.42095
Epoch 89/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1570 - acc: 0.9472 - val_loss: 0.4905 - val_acc: 0.8924

Epoch 00089: val_loss did not improve from 0.42095
Epoch 90/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1277 - acc: 0.9562 - val_loss: 0.5003 - val_acc: 0.9013

Epoch 00090: val_loss did not improve from 0.42095
Epoch 91/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1332 - acc: 0.9539 - val_loss: 0.4949 - val_acc: 0.9013

Epoch 00091: val_loss did not improve from 0.42095
Epoch 92/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1137 - acc: 0.9562 - val_loss: 0.5010 - val_acc: 0.9103

Epoch 00092: val_loss did not improve from 0.42095
Epoch 93/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1087 - acc: 0.9584 - val_loss: 0.6161 - val_acc: 0.8879

Epoch 00093: val_loss did not improve from 0.42095
Epoch 94/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1255 - acc: 0.9584 - val_loss: 0.5687 - val_acc: 0.8879

Epoch 00094: val_loss did not improve from 0.42095
Epoch 95/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1228 - acc: 0.9618 - val_loss: 0.5399 - val_acc: 0.9058

Epoch 00095: val_loss did not improve from 0.42095
Epoch 96/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1220 - acc: 0.9618 - val_loss: 0.5337 - val_acc: 0.8924

Epoch 00096: val_loss did not improve from 0.42095
Epoch 97/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1164 - acc: 0.9584 - val_loss: 0.6697 - val_acc: 0.8834

Epoch 00097: val_loss did not improve from 0.42095
Epoch 98/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1171 - acc: 0.9596 - val_loss: 0.4986 - val_acc: 0.8879

Epoch 00098: val_loss did not improve from 0.42095
Epoch 99/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1236 - acc: 0.9573 - val_loss: 0.5034 - val_acc: 0.9058

Epoch 00099: val_loss did not improve from 0.42095
Epoch 100/100
890/890 [==============================] - 3s 3ms/step - loss: 0.1047 - acc: 0.9640 - val_loss: 0.4603 - val_acc: 0.9058

Epoch 00100: val_loss did not improve from 0.42095
