# Author:LiPu
import argparse
from models import *
from torchinfo import summary

parser = argparse.ArgumentParser()
parser.add_argument('--cfg', type=str, default='cfg/yolov3/yolov3.cfg', help='*.cfg path')
parser.add_argument('--img_size', type=int, default=416, help='img_size')
parser.add_argument('--device', default='cpu', help='device id (i.e. 0 or 0,1) or cpu')
opt = parser.parse_args()

device = torch_utils.select_device(opt.device)
model = Darknet(opt.cfg)
# model.fuse()
model.to(device)
summary(model, input_size=(1, 3, opt.img_size, opt.img_size), col_names=["kernel_size", "output_size", "num_params", "mult_adds"],)
