_base_ = [
    '../_base_/models/mask_rcnn_r50_fpn.py',
    '../_base_/datasets/coco_instance.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]
log_config = dict(
    interval=2
    )
data = dict(
    samples_per_gpu=1,
    workers_per_gpu=0,
    )