import torch
from collections import OrderedDict

def fix_mismatch(in_state_dict):
    print('fixing name mismatch problem...')
    renamed_list = ['_conv_stem','_depthwise_conv','_se_reduce','_se_expand','_project_conv','_expand_conv','_conv_head']
    new_state_dict = OrderedDict()
    for key, values in in_state_dict.items():
       # print(key)
        names = key.split('.')
        if len(names)==2:
            names[0] = names[0]+'.conv' if names[0] in renamed_list else names[0]
        elif len(names)==4:
            names[2] = names[2]+'.conv' if names[2] in renamed_list else names[2]
        names = '.'.join(names)
        new_state_dict[names] = values
    return new_state_dict


if __name__ == '__main__':
    ori_pth_f = 'weights/efficientnet-b0-355c32eb.pth'
    out_pth_f = 'weights/effNet-b0.pth'
    print('loading stat_dict')
    old_weight = torch.load(ori_pth_f)
    
    new_state = fix_weight_name_mismatch(old_weight)
    #torch.save(new_state,out_pth_f)
