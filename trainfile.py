import os
import glob
import pinyin
import shutil

# path = r'C:\Users\yeluo\Desktop\new\uploadSkin3'
# save_path = r'C:\Users\yeluo\Desktop\new\uploadSkin3_new'
path = r'C:\Users\yeluo\Desktop\new\uploadSkin6'
save_path = r'C:\Users\yeluo\Desktop\new\uploadSkin6_double'
if not os.path.exists(save_path):
    os.makedirs(save_path)

heros = os.listdir(path)
for he in heros:
    he_str = pinyin.get(he,format='strip').replace(' ','')
    hero = os.path.join(path,he)
    hero_str = os.path.join(save_path,he_str)
    print(hero_str)
    if not os.path.exists(hero_str):
        os.makedirs(hero_str)
    skins = os.listdir(hero)
    for sk in skins:
        sk_str = pinyin.get_initial(sk).replace(' ','')
        skin = os.path.join(hero,sk)
        skin_str = os.path.join(hero_str,sk_str)
        if not os.path.exists(skin_str):
            os.makedirs(skin_str)
        # print(skin_str)
        count = 1
        path_temp = glob.glob(skin + "*/1/*/*")
        for im in path_temp:

            final_path = os.path.join(skin_str,he_str+'_'+sk_str+'_'+str(count)+'.png')
            # print(final_path)
            count += 1
            shutil.copyfile(im,final_path)