import numpy as np

CO3_contained_nnlist_abs_path_list_loaded = np.load('/mnt/ssd_elecom_black_c2c/scripts_get_CO3-contained_nnlist_abs_path_list/CO3_contained_nnlist_abs_path_list.npy')

CO3_contained_poscar_folder_abs_path_list = [nnlist_path[:-14] for nnlist_path in CO3_contained_nnlist_abs_path_list_loaded]

np.save('CO3_contained_poscar_folder_abs_path_list.npy', CO3_contained_poscar_folder_abs_path_list)
    