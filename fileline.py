import os
import glob
import pinyin
import shutil

path = r'C:\Users\yeluo\Desktop\new\uploadSkin3'
save_path = r'C:\Users\yeluo\Desktop\new\uploadSkin3_new'
if not os.path.exists(save_path):
	os.makedirs(save_path)

# path = 'C:/Users/Administrator/Desktop/SGameServer2/'
# save_path = 'C:/Users/Administrator/Desktop/hero/testing/'

files = os.listdir(path) # 104 hero
all_count = 0
count_class = 0
for f in files:
	count_hero = 1
	heros_path = os.path.join(path, f)
	heros = os.listdir(heros_path)
	for hero in heros:
		count_class = count_class + all_count
		hero_str = pinyin.get_initial(hero).replace(' ','')
		# if len(str(count_hero)) == 1:
		# 	new_name = '0'+str(count_hero)+'_'+hero_str
		# else:
		# 	new_name = str(count_hero)+'_'+hero_str
		# hero_new_path = os.path.join(save_path,new_name)
		hero_new_path = os.path.join(save_path, str(hero_str))
		if os.path.exists(hero_new_path):
			pass
		else:
			os.mkdir(hero_new_path)
		hero_use = os.path.join(heros_path, hero)
		# print(hero_use)
		skin = os.listdir(hero_use)
		for i in skin:
			print(i)
			count_skin = 1
			skin_str = pinyin.get_initial(i).replace(' ', '')
			if len(str(count_skin)) == 1:
				new_name = skin_str + '0'+str(count_skin)
			else:
				new_name = skin_str + str(count_skin)
			skin_new_path = os.path.join(hero_new_path, str(new_name))
			# print(skin_new_path)
			skin_use = os.path.join(hero_use,i)
			path_temp = glob.glob(skin_use+'*/1/*/*')
			# print(path_temp)

			for j in path_temp:
				fina_path = os.path.join(skin_new_path,str(count_class)+'.png')
				if not os.path.exists(skin_new_path):
					os.makedirs(skin_new_path)
				# print(fina_path)
				shutil.copyfile(j, fina_path)

				count_class += 1
			# count_skin += 1


		# 	hero_new_save_path = os.path.join(hero_new_path, str(count_class)+'.png')
	# 		shutil.copyfile(i, hero_new_save_path)
	# 		count_class += 1
	#
		count_hero += 1
	all_count = len(path_temp)