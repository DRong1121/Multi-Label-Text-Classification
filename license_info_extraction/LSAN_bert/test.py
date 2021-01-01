import torch
import numpy as np
from sklearn import metrics

from utils import *

true_mat_1 = torch.tensor([[0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                     [0., 1., 1., 1., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
                     [0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
                     [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
                     [0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                     [0., 1., 0., 1., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
                     [0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                     [0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                     [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
                     [0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
                     [1., 1., 1., 1., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
                     [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
                     [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
                     [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
                     [1., 1., 1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
                     [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0.]])

pred_mat_1 = torch.tensor([[0.4337, 0.3988, 0.3631, 0.5756, 0.2371, 0.3322, 0.5705, 0.7902, 0.5423, 0.5958, 0.4889, 0.4430, 0.5679],
        [0.3723, 0.5596, 0.4712, 0.6130, 0.4789, 0.3579, 0.5378, 0.5906, 0.5152, 0.5599, 0.4290, 0.6708, 0.4975],
        [0.5771, 0.4400, 0.5223, 0.6037, 0.4995, 0.4757, 0.4966, 0.6429, 0.4728, 0.5795, 0.5326, 0.5164, 0.5028],
        [0.3850, 0.5178, 0.4867, 0.5713, 0.4951, 0.4131, 0.5858, 0.6906, 0.4397, 0.4746, 0.4736, 0.5769, 0.4500],
        [0.4199, 0.5117, 0.4825, 0.5101, 0.4148, 0.4770, 0.6273, 0.4875, 0.4050, 0.5345, 0.5132, 0.4941, 0.4654],
        [0.3609, 0.3587, 0.3928, 0.6026, 0.3959, 0.3456, 0.6947, 0.5913, 0.6560, 0.3365, 0.5647, 0.4588, 0.3446],
        [0.3599, 0.4366, 0.5345, 0.6934, 0.5066, 0.3061, 0.6135, 0.6795, 0.6128, 0.3743, 0.6997, 0.4956, 0.4439],
        [0.4475, 0.5435, 0.5293, 0.5809, 0.4392, 0.4397, 0.5616, 0.5388, 0.5313, 0.5043, 0.5430, 0.5486, 0.5717],
        [0.4852, 0.4960, 0.4368, 0.6440, 0.5454, 0.3363, 0.5821, 0.6044, 0.5887, 0.4401, 0.5364, 0.4717, 0.4735],
        [0.4299, 0.6008, 0.5172, 0.5532, 0.4583, 0.4198, 0.5692, 0.6323, 0.6092, 0.3913, 0.5816, 0.3721, 0.5770],
        [0.3564, 0.4658, 0.3735, 0.5489, 0.3529, 0.3695, 0.5602, 0.5983, 0.5608, 0.6569, 0.3906, 0.5784, 0.4995],
        [0.4094, 0.4162, 0.5172, 0.6308, 0.5361, 0.4275, 0.6384, 0.6831, 0.5418, 0.5979, 0.5407, 0.4650, 0.5227],
        [0.4089, 0.5853, 0.4605, 0.6882, 0.5047, 0.5000, 0.6107, 0.5828, 0.5323, 0.4198, 0.4786, 0.4642, 0.5388],
        [0.4378, 0.5370, 0.4789, 0.6116, 0.4546, 0.4896, 0.5982, 0.5189, 0.5925, 0.4810, 0.6398, 0.5235, 0.5820],
        [0.3605, 0.5506, 0.4016, 0.6759, 0.4612, 0.4891, 0.5953, 0.4772, 0.5094, 0.5936, 0.5437, 0.6379, 0.5004],
        [0.3505, 0.5857, 0.5021, 0.6141, 0.5397, 0.3803, 0.6248, 0.7473, 0.4852, 0.5320, 0.4147, 0.5090, 0.4894]])

true_mat_2 = torch.tensor([[0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
        [0., 0., 0., 0., 0., 0., 0., 0., 1., 1., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
        [0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [1., 1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
        [0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
        [0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.]])

pred_mat_2 = torch.tensor([[0.4221, 0.5553, 0.3858, 0.6325, 0.3889, 0.4680, 0.5761, 0.5989, 0.5501, 0.4882, 0.4936, 0.4840, 0.5761],
        [0.3453, 0.6388, 0.4213, 0.6855, 0.5939, 0.4160, 0.4610, 0.5221, 0.5733, 0.5339, 0.4808, 0.5809, 0.4432],
        [0.4408, 0.4930, 0.4485, 0.6217, 0.4718, 0.4064, 0.5759, 0.5770, 0.4749, 0.5129, 0.5106, 0.5325, 0.5087],
        [0.4594, 0.4818, 0.4975, 0.5718, 0.4995, 0.3493, 0.4341, 0.6127, 0.4746, 0.4618, 0.4753, 0.5717, 0.5546],
        [0.3860, 0.5319, 0.4572, 0.5851, 0.4870, 0.4209, 0.5771, 0.6024, 0.5276, 0.5424, 0.5414, 0.4858, 0.5643],
        [0.4561, 0.4552, 0.3215, 0.6306, 0.4396, 0.5134, 0.5254, 0.4999, 0.5324, 0.5483, 0.5445, 0.5579, 0.5798],
        [0.2875, 0.4406, 0.5219, 0.6128, 0.4277, 0.2989, 0.6081, 0.6404, 0.5090, 0.5280, 0.4526, 0.5125, 0.5895],
        [0.4058, 0.5398, 0.4183, 0.6670, 0.5398, 0.4122, 0.5857, 0.4886, 0.5307, 0.5115, 0.5633, 0.4674, 0.5593],
        [0.3635, 0.4994, 0.4895, 0.5651, 0.4426, 0.4628, 0.7129, 0.4604, 0.5124, 0.4965, 0.5396, 0.5920, 0.5110],
        [0.4445, 0.5175, 0.4640, 0.5782, 0.4881, 0.4626, 0.5461, 0.5695, 0.5116, 0.4635, 0.5427, 0.5084, 0.4797],
        [0.3265, 0.4864, 0.4548, 0.6326, 0.6484, 0.2587, 0.5784, 0.4821, 0.5853, 0.6408, 0.4378, 0.5470, 0.6822],
        [0.4545, 0.5026, 0.5473, 0.6203, 0.4320, 0.4369, 0.5152, 0.5692, 0.3997, 0.3289, 0.5396, 0.5554, 0.4939],
        [0.4309, 0.4898, 0.4274, 0.6436, 0.4439, 0.3919, 0.6026, 0.5920, 0.4831, 0.5350, 0.4903, 0.5576, 0.5166],
        [0.4584, 0.4953, 0.4664, 0.6354, 0.4835, 0.4262, 0.5080, 0.6252, 0.4707, 0.4831, 0.4983, 0.4842, 0.5637],
        [0.4272, 0.5085, 0.4667, 0.5490, 0.4886, 0.3843, 0.6150, 0.6090, 0.6137, 0.5572, 0.5457, 0.5810, 0.4287],
        [0.5189, 0.5385, 0.4278, 0.6088, 0.5820, 0.3085, 0.4728, 0.5908, 0.5164, 0.5409, 0.5232, 0.4860, 0.5928]])

threshold = 0.5


if __name__ == '__main__':
    true_label_dict = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: [],
        11: [],
        12: [],
        13: []
    }
    pred_label_dict = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: [],
        11: [],
        12: [],
        13: []
    }
    accuracy_score_list = []
    precision_score_list = []
    recall_score_list = []
    f1_score_list = []

    true_label_1, pred_label_1 = make_label_all_class(true_mat_1, pred_mat_1, threshold)
    print(true_label_1)
    print(pred_label_1)

    for i in range(0, 13):
        make_label_each_class(true_arr=true_label_1, pred_arr=pred_label_1, index=i,
                              true_label_list=true_label_dict[i+1], pred_label_list=pred_label_dict[i+1])

    true_label_2, pred_label_2 = make_label_all_class(true_mat_2, pred_mat_2, threshold)
    print(true_label_2)
    print(pred_label_2)

    for i in range(0, 13):
        make_label_each_class(true_arr=true_label_2, pred_arr=pred_label_2, index=i,
                              true_label_list=true_label_dict[i+1], pred_label_list=pred_label_dict[i+1])

    for i in range(0, 13):
        accuracy_score, precision_score, recall_score, f1_score = get_metrics_each_class(true_label_dict[i+1], pred_label_dict[i+1])
        accuracy_score_list.append(accuracy_score)
        precision_score_list.append(precision_score)
        recall_score_list.append(recall_score)
        f1_score_list.append(f1_score)

    avg_accuracy_score = np.mean(accuracy_score_list)
    print(avg_accuracy_score)
    macro_precision_score = np.mean(precision_score_list)
    print(macro_precision_score)
    macro_recall_score = np.mean(recall_score_list)
    print(macro_recall_score)
    macro_f1_score = np.mean(f1_score_list)
    print(macro_f1_score)


