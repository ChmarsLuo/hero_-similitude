import os
import glob
import pinyin
import shutil

path = r'C:\Users\yeluo\Desktop\new\0519\111'
save_path = r'C:\Users\yeluo\Desktop\new\0519\111_new'
if not os.path.exists(save_path):
    os.makedirs(save_path)
heros = os.listdir(path)
for he in heros:
    # hero name
    he_str = pinyin.get(he,format='strip').replace(' ','')
    hero = os.path.join(path,he)
    hero_str = os.path.join(save_path,he_str)
    if not os.path.exists(hero_str):
        os.makedirs(hero_str)
    skins = os.listdir(hero)
    for sk in skins:
        # skin name
        sk_str = pinyin.get_initial(sk).replace(' ','')
        skin_str = os.path.join(hero_str,sk_str)
        skin = os.path.join(hero,sk)
        skin_1 = os.path.join(skin,'1')
        for sk1 in os.listdir(skin_1):
            if 'Idleshow' in str(sk1):
                pass
            else:
                come = os.path.join(skin_1,sk1)
                for co in os.listdir(come):
                    if co == 'left.png':
                        place = os.path.join(come,co)
                        sk1 = sk1.replace(' ','')
                        temp = skin_str + '_' + sk1 + '_' + 'lift'
                        if not os.path.exists(temp):
                            os.makedirs(temp)
                        name = os.path.join(temp,  str(111) + '_'  + co)
                        shutil.copyfile(place,name)
                    elif co == 'right.png':
                        place = os.path.join(come,co)
                        sk1 = sk1.replace(' ','')
                        temp = skin_str + '_' + sk1 + '_' + 'right'
                        if not os.path.exists(temp):
                            os.makedirs(temp)
                        name = os.path.join(temp,  str(111) + '_'  + co)
                        shutil.copyfile(place,name)
                    elif co == 'backward.png':
                        place = os.path.join(come,co)
                        sk1 = sk1.replace(' ','')
                        temp = skin_str + '_' + sk1 + '_' + 'backward'
                        if not os.path.exists(temp):
                            os.makedirs(temp)
                        name = os.path.join(temp,  str(111) + '_'  + co)
                        shutil.copyfile(place,name)
                    elif co == 'forward.png':
                        place = os.path.join(come,co)
                        sk1 = sk1.replace(' ','')
                        temp = skin_str + '_' + sk1 + '_' + 'forward'
                        if not os.path.exists(temp):
                            os.makedirs(temp)
                        name = os.path.join(temp,  str(111) + '_'  + co)
                        shutil.copyfile(place,name)
