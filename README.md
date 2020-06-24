# Fix-name-mismatch-in-loading-EfficientNet-weight-Yet-Another-EfficientDet-Pytorch-
## Guide
step 1: Download fix_name_mismatch.py to 'Yet-Another-EfficientDet-Pytorch/efficientnet/'

step 2: open Yet-Another-EfficientDet-Pytorch/efficientnet/utils.py and add 'from .fix_name_mismatch import fix_mismatch'

step 3: open Yet-Another-EfficientDet-Pytorch/efficientnet/utils.py and add 'state_dict = fix_mismatch(state_dict)'
