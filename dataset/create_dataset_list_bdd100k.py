# -*- coding: utf-8 -*-
import os
import glob
root_path=os.path.expanduser('./bdd100k')
image_path='images/100k/'
annotation_path='drivable_maps/labels/'
splits=['train','val','test']

#train glob images 2975
#train glob annotations 2975
#val glob images 500
#val glob annotations 500
#test glob images 1525
#test glob annotations 1525

for split in splits:
    glob_images=glob.glob(os.path.join(root_path,image_path,split,'*.jpg').replace("\\","/"))
    glob_annotations=glob.glob(os.path.join(root_path,annotation_path,split,'*_drivable_id.png').replace("\\","/"))
    print('%s glob images'%split,len(glob_images))
    print('%s glob annotations'%split,len(glob_annotations))
    
    write_file=open('./bdd100k/bdd100k_'+split+'_list.txt','w')
    for g_img in glob_images:
        #img_p: eg leftImg8bit/val/frankfurt/frankfurt_000001_083852_leftImg8bit.png
        #ann_p: eg gtFine/val/frankfurt/frankfurt_000001_083852_gtFine_labelTrainIds.png
        img_p=g_img.replace(root_path+'/','').replace("\\","/")
        #replace will not change img_p
        ann_p=img_p.replace('images/100k','drivable_maps/labels').replace('.jpg','_drivable_id.png').replace("\\","/")
        #assert os.path.join(root_path,img_p) in glob_images,'%s not exist'%img_p
        #assert os.path.join(root_path,ann_p) in glob_annotations,'%s not exist'%ann_p
        write_file.write(img_p+' '+ann_p+'\n')
    write_file.close()
