import sys
import argparse
import os
os.environ["CUDA_VISIBLE_DEVICES"]='1'


from ultralytics import RTDETR



def main(opt):
    yaml = opt.cfg
    model = RTDETR('runs/detect/train93/weights/last.pt')

    results = model.train(data='ultralytics/cfg/datasets/mydata.yaml',
                        epochs=300,
                        imgsz=640,
                        workers=8,
                        batch=8,
                        amp=True,
                          resume=True,
                          lr0=0.00001
                        )

def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--cfg', type=str, default= 'ultralytics/cfg/models/rt-detr/rtdetr-l-mutil-cmfusion.yaml', help='initial weights path')

    opt = parser.parse_known_args()[0] if known else parser.parse_args()
    return opt

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)