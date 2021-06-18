import os
import glob
import pinyin
import shutil

# path = r'C:\Users\yeluo\Desktop\new\uploadSkin3'
# save_path = r'C:\Users\yeluo\Desktop\new\uploadSkin3_new'
path = r'C:\Users\yeluo\Desktop\new\uploadSkin6'
save_path = r'C:\Users\yeluo\Desktop\new\uploadSkin6_double1'
if not os.path.exists(save_path):
    os.makedirs(save_path)
heros = os.listdir(path)
for he in heros:
    he_str = pinyin.get(he,format='strip').replace(' ','')
    hero = os.path.join(path,he)
    hero_str = os.path.join(save_path,he_str)
    # print(hero_str)
    if not os.path.exists(hero_str):
        os.makedirs(hero_str)
    skins = os.listdir(hero)
    for sk in skins:
        sk_str = pinyin.get_initial(sk).replace(' ','')
        skin = os.path.join(hero,sk)
        count = 0
        a = ['left','right','backward','forward']
        for e in a:
            temp_path = glob.glob(skin+'/1/*/'+e+'.png')
            print(temp_path)
            for im in temp_path:
                print(im)
                final_path = os.path.join(hero_str, he_str + '_' + sk_str + '_' + e)
                if not os.path.exists(final_path):
                    os.makedirs(final_path)
                count += 1
                name = os.path.join(final_path,e+'_'+str(count)+'.png')
                shutil.copyfile(im, name)
