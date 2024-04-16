# MNIST_Classification

인공신경망과 딥러닝 (Assignment #2)


사용할 신경망 모델
1. LeNet-5
2. MLP

LeNet-5와 MLP의 각각의 파라미터 수

**(LeNet-5)**

1. Conv2d 층의 파라미터 수 계산:

* 첫 번째 Conv2d 층:
입력 채널 수: 1
출력 채널 수: 6
커널 크기: 5x5

파라미터 수 = (입력 채널 수 × 출력 채널 수 × 커널 높이 × 커널 너비) + 출력 채널 수 = (1 × 6 × 5 × 5) + 6 = 156

* 두 번째 Conv2d 층:
입력 채널 수: 6
출력 채널 수: 16
커널 크기: 5x5

파라미터 수 = (입력 채널 수 × 출력 채널 수 × 커널 높이 × 커널 너비) + 출력 채널 수 = (6 × 16 × 5 × 5) + 16 = 2416

* 세 번째 Conv2d 층:
입력 채널 수: 16
출력 채널 수: 120
커널 크기: 5x5

파라미터 수 = (입력 채널 수 × 출력 채널 수 × 커널 높이 × 커널 너비) + 출력 채널 수 = (16 × 120 × 5 × 5) + 120 = 48120

2. Linear 층의 파라미터 수 계산:

* 첫 번째 Linear 층:
입력 특성 수: 120
출력 특성 수: 84

파라미터 수 = (입력 특성 수 × 출력 특성 수) + 출력 특성 수 = (120 × 84) + 84 = 10164

* 두 번째 Linear 층:
입력 특성 수: 84
출력 특성 수: 10 (클래스 수)

파라미터 수 = (입력 특성 수 × 출력 특성 수) + 출력 특성 수 = (84 × 10) + 10 = 850

총 파라미터 수 = Conv2d 층의 파라미터 수 + Linear 층의 파라미터 수 = 156 + 2416 + 48120 + 10164 + 850 = 61806

따라서 LeNet-5 모델은 총 61,806개의 파라미터를 가짐

**(MLP)**

1. 입력층에서 첫 번째 은닉층으로의 파라미터 수:

* 입력 특성 수: 784 (MNIST 이미지 크기)
* 은닉층 뉴런 수: 256
* 가중치 행렬 크기: (784, 256)
* 편향 벡터 크기: (256,)
* 파라미터 수 = (입력 특성 수 × 은닉층 뉴런 수) + 은닉층 뉴런 수 = (784 × 256) + 256 = 200960

2. 첫 번째 은닉층에서 두 번째 은닉층으로의 파라미터 수:

* 입력 특성 수: 256 (이전 은닉층의 출력 크기)
* 은닉층 뉴런 수: 128
* 가중치 행렬 크기: (256, 128)
* 편향 벡터 크기: (128,)
* 파라미터 수 = (입력 특성 수 × 은닉층 뉴런 수) + 은닉층 뉴런 수 = (256 × 128) + 128 = 32896

3. 두 번째 은닉층에서 출력층으로의 파라미터 수:

* 입력 특성 수: 128 (이전 은닉층의 출력 크기)
* 출력 클래스 수: 10
* 가중치 행렬 크기: (128, 10)
* 편향 벡터 크기: (10,)
* 파라미터 수 = (입력 특성 수 × 출력 클래스 수) + 출력 클래스 수 = (128 × 10) + 10 = 1290

총 파라미터 수 = 첫 번째 은닉층 파라미터 수 + 두 번째 은닉층 파라미터 수 + 출력층 파라미터 수 
= 200960 + 32896 + 1290 = 234146

따라서 MLP 모델은 총 234,146개의 파라미터를 가짐

Epoch에 따른 Loss와 Accuracy


**(LeNet-5)**

* Epoch: 0	Train loss: 0.2290	Valid loss: 0.1020	Train accuracy: 96.84	Valid accuracy: 96.81
* Epoch: 1	Train loss: 0.0762	Valid loss: 0.0619	Train accuracy: 98.39	Valid accuracy: 98.19
* Epoch: 2	Train loss: 0.0550	Valid loss: 0.0542	Train accuracy: 98.59	Valid accuracy: 98.45
* Epoch: 3	Train loss: 0.0438	Valid loss: 0.0486	Train accuracy: 99.07	Valid accuracy: 98.41
* Epoch: 4	Train loss: 0.0343	Valid loss: 0.0416	Train accuracy: 99.25	Valid accuracy: 98.75
* Epoch: 5	Train loss: 0.0299	Valid loss: 0.0422	Train accuracy: 99.41	Valid accuracy: 98.66
* Epoch: 6	Train loss: 0.0241	Valid loss: 0.0409	Train accuracy: 99.47	Valid accuracy: 98.70
* Epoch: 7	Train loss: 0.0228	Valid loss: 0.0418	Train accuracy: 99.57	Valid accuracy: 98.69
* Epoch: 8	Train loss: 0.0186	Valid loss: 0.0447	Train accuracy: 99.53	Valid accuracy: 98.70
* Epoch: 9	Train loss: 0.0161	Valid loss: 0.0468	Train accuracy: 99.64	Valid accuracy: 98.70
* Epoch: 10	Train loss: 0.0148	Valid loss: 0.0492	Train accuracy: 99.55	Valid accuracy: 98.54
* Epoch: 11	Train loss: 0.0146	Valid loss: 0.0486	Train accuracy: 99.65	Valid accuracy: 98.67
* Epoch: 12	Train loss: 0.0115	Valid loss: 0.0459	Train accuracy: 99.73	Valid accuracy: 98.68
* Epoch: 13	Train loss: 0.0126	Valid loss: 0.0486	Train accuracy: 99.71	Valid accuracy: 98.65
* Epoch: 14	Train loss: 0.0119	Valid loss: 0.0458	Train accuracy: 99.70	Valid accuracy: 98.89

**(MLP)**

* epoch: 0, train accuracy: 0.2834, validation accuracy: 0.2904, train loss: 7263.5355, test loss: 631.9550
* epoch: 1, train accuracy: 0.8190, validation accuracy: 0.8226, train loss: 146.9752, test loss: 17.9391
* epoch: 2, train accuracy: 0.8677, validation accuracy: 0.8707, train loss: 13.1279, test loss: 10.6673
* epoch: 3, train accuracy: 0.8815, validation accuracy: 0.883, train loss: 9.5315, test loss: 8.1971
* epoch: 4, train accuracy: 0.8840, validation accuracy: 0.8862, train loss: 7.8150, test loss: 7.0593
* epoch: 5, train accuracy: 0.9027, validation accuracy: 0.9056, train loss: 6.4080, test loss: 5.2889
* epoch: 6, train accuracy: 0.9029, validation accuracy: 0.904, train loss: 5.50391, test loss: 4.8505
* epoch: 7, train accuracy: 0.8845, validation accuracy: 0.8881, train loss: 6.2339, test loss: 5.5985
* epoch: 8, train accuracy: 0.8569, validation accuracy: 0.8595, train loss: 7.29561, test loss: 7.5304
* epoch: 9, train accuracy: 0.8810, validation accuracy: 0.8823, train loss: 6.9749, test loss: 6.1490
* epoch: 10, train accuracy: 0.9125, validation accuracy: 0.9111, train loss: 7.1213, test loss: 4.4467
* epoch: 11, train accuracy: 0.8749, validation accuracy: 0.8752, train loss: 4.8533, test loss: 6.3063
* epoch: 12, train accuracy: 0.8564, validation accuracy: 0.8516, train loss: 7.5181, test loss: 8.9381
* epoch: 13, train accuracy: 0.8783, validation accuracy: 0.8789, train loss: 7.8848, test loss: 6.8449
* epoch: 14, train accuracy: 0.8977, validation accuracy: 0.8956, train loss: 6.5561, test loss: 5.5719

**(Plot)**
![Lenet5-1](https://github.com/jimmynkim/MNIST_Classification/assets/75557016/da93b6d6-9aa6-4f89-9d7c-eb619644c394)
![Lenet5-2](https://github.com/jimmynkim/MNIST_Classification/assets/75557016/2493d193-f873-4117-8dbe-f2e3865ad067)
![MLP1](https://github.com/jimmynkim/MNIST_Classification/assets/75557016/9447731c-97e7-4559-8dbf-c6dd371dad8f)
![MLP2](https://github.com/jimmynkim/MNIST_Classification/assets/75557016/cec292ec-23d3-459d-99e4-f167e49ee12e)

* LeNet-5와 MLP의 최고 분류 성능
Lenet-5 : 90.56%
MLP: 98.89%

* 참고 

https://deep-learning-study.tistory.com/368

https://www.youtube.com/watch?v=yTgAPCY7cEc
