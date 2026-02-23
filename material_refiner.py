import bpy

# ==========================================
# БАЗЫ ДАННЫХ (Списки материалов)
# Сюда ты просто дописываешь названия из Mineways
# ==========================================

# Материалы со слабым излучением
LIST_EMISSION_WEAK = {
    # Редстоун
    "deepslate_redstone_ore",
    "redstone_ore",
    # Растения
    "sea_pickle",
    "torchflower_crop_stage1",
    "jack_o_lantern",
    "pitcher_crop_bottom_stage4",
    "firefly_bush",
    "glow_lichen",
    # Свечи
    "black_candle_lit",
    "blue_candle_lit",
    "brown_candle_lit",
    "candle_lit",
    "cyan_candle_lit",
    "gray_candle_lit",
    "green_candle_lit",
    "light_blue_candle_lit",
    "light_gray_candle_lit",
    "lime_candle_lit",
    "magenta_candle_lit",
    "orange_candle_lit",
    "pink_candle_lit",
    "purple_candle_lit",
    "red_candle_lit",
    "white_candle_lit",
    "yellow_candle_lit",
    # «Админские» блоки
    "jigsaw_lock",
    "jigsaw_side",
    "jigsaw_top",
    "structure_block_corner",
    "structure_block_data",
    "structure_block_load",
    "structure_block_save",
    "test_block_accept",
    "test_block_fail",
    "test_block_log",
    "test_block_start",
    "test_instance_block",
    "chain_command_block_back",
    "chain_command_block_conditional",
    "chain_command_block_front",
    "chain_command_block_side",
    "command_block_back",
    "command_block_conditional",
    "command_block_front",
    "command_block_side",
    "repeating_command_block_back",
    "repeating_command_block_conditional",
    "repeating_command_block_front",
    "repeating_command_block_side",
    # Дворцы испытаний
    "trial_spawner_side_active",
    "trial_spawner_side_active_ominous",
    "trial_spawner_top_active",
    "trial_spawner_top_active_ominous",
    "trial_spawner_top_ejecting_reward",
    "trial_spawner_top_ejecting_reward_ominous",
    "vault_bottom",
    "vault_bottom_ominous",
    "vault_front_ejecting",
    "vault_front_ejecting_ominous",
    "vault_front_off",
    "vault_front_off_ominous",
    "vault_front_on",
    "vault_front_on_ominous",
    "vault_side_off",
    "vault_side_off_ominous",
    "vault_side_on",
    "vault_side_on_ominous",
    "vault_top",
    "vault_top_ejecting",
    "vault_top_ejecting_ominous",
    "vault_top_ominous",
    # Остальное
    "amethyst_cluster",
    "large_amethyst_bud",
    "medium_amethyst_bud",
    "small_amethyst_bud",
    "crying_obsidian",
    "respawn_anchor_bottom",
    "respawn_anchor_side0",
    "respawn_anchor_side1",
    "respawn_anchor_side2",
    "respawn_anchor_side3",
    "respawn_anchor_side4",
    "respawn_anchor_top",
    "respawn_anchor_top_off",
    "campfire_log_lit",
    "soul_campfire_log_lit",
    "creaking_heart_awake",
    "creaking_heart_top_awake",
    "brewing_stand",
    "conduit",
    "magma",
    "dragon_egg",
    "spawner",
    "MWO_ender_chest_front",
    "MWO_ender_chest_latch",
    "MWO_ender_chest_side",
    "MWO_ender_chest_top",
    "sculk", 
    "sculk_vein",
    "calibrated_sculk_sensor_amethyst",
    "calibrated_sculk_sensor_input_side",
    "calibrated_sculk_sensor_top",
    "sculk_catalyst_bottom",
    "sculk_catalust_side",
    "sculk_catalyst_top",
    "sculk_sensor_bottom",
    "sculk_sensor_side",
    "sculk_sensor_tendril_active",
    "sculk_sensor_tendril_inactive",
    "sculk_sensor_top",
    "sculk_shrieker_bottom",
    "sculk_shrieker_can_summon_inner_top",
    "sculk_shrieker_inner_top",
}

# Материалы с мощным излучением
LIST_EMISSION_STRONG = {
    # Блоки
    "shroomlight",
    "redstone_lamp_on",
    "glowstone",
    "sea_lantern",
    "beacon",
    "ochre_froglight_side",
    "ochre_froglight_top",
    "pearlescent_froglight_side",
    "pearlescent_froglight_top",
    "verdant_froglight_side",
    "verdant_froglight_top",
    # Факелы
    "redstone_torch",
    "torch",
    "soul_torch",
    "copper_torch",
    # Порталы
    "MW_end_portal",
    "nether_portal",
    # Фонари
    "lantern",
    "soul_lantern",
    "copper_lantern",
    "exposed_copper_lantern",
    "weathered_copper_lantern",
    "oxidized_copper_lantern",
    "waxed_copper_lantern",
    "waxed_exposed_copper_latnern",
    "waxed_weathered_copper_lantern",
    "waxed_oxidized_copper_lantern",
    # Остальное
    "fire_0",
    "soul_fire_0",
    "campfire_fire",
    "soul_campfire_fire",
    "smoker_front_on",
    "blast_furnace_front_on",
    "furnace_front_on",
    "lava_still",
    "lava_flow",
    "end_rod",
    "lightning_rod",
    "comparator_on",
    "repeater_on",
    "activator_rail_on",
    "detector_rail_on",
    "powered_rail_on",
}

# Тонкие материалы, которым нужно просвечивание
LIST_TRANSLUCENCY = {
    # Растения
        # Листва
        "bamboo_large_leaves",
        "bamboo_small_leaves",
        "oak_leaves",
        "pale_oak_leaves",
        "spruce_leaves",
        "birch_leaves",
        "acacia_leaves",
        "azalea_leaves",
        "flowering_azalea_leaves",
        "cherry_leaves",
        "dark_oak_leaves",
        "jungle_leaves",
        "mangrove_leaves",
        # Растущее
        "pitcher_crop_bottom_stage1",
        "pitcher_crop_bottom_stage2",
        "pitcher_crop_bottom_stage3",
        "pitcher_crop_bottom_stage4",
        "pitcher_crop_top_stage3",
        "wheat_stage0",
        "wheat_stage1",
        "wheat_stage2",
        "wheat_stage3",
        "wheat_stage4",
        "wheat_stage5",
        "wheat_stage6",
        "wheat_stage7",
        "carrots_stage0",
        "carrots_stage1",
        "carrots_stage2",
        "carrots_stage3",
        "potatoes_stage0",
        "potatoes_stage1",
        "potatoes_stage2",
        "potatoes_stage3",
        "beetroots_stage0",
        "beetroots_stage1",
        "beetroots_stage2",
        "beetroots_stage3",
        # Кусты
        "bush",
        "firefly_bush",
        "potted_azalea_bush_side",
        "potted_azalea_bush_top",
        "potted_flowering_azalea_bush_side",
        "potted_flowering_azalea_bush_top",
        "sweet_berry_bush_stage0",
        "sweet_berry_bush_stage1",
        "sweet_berry_bush_stage2",
        "sweet_berry_bush_stage3",
        # Листья
        "leaf_litter",
        "bamboo_singleleaf",
        "big_dripleaf_side",
        "big_dripleaf_stem",
        "big_dripleaf_tip",
        "big_dripleaf_top",
        "small_dripleaf_side",
        "small_dripleaf_stem_bottom",
        "small_dripleaf_stem_top",
        "small_dripleaf_side",
        "small_dripleaf_top",
        # Трава
            # Обычная
            "short_grass",
            "short_dry_grass",
            "tall_dry_grass",
            "tall_grass_bottom",
            "tall_grass_top",
            "fern",
            "large_fern_bottom",
            "large_fern_top",
            # Подводная
            "seagrass",
            "tall_seagrass_bottom",
            "tall_seagrass_top",
            "kelp",
            "kelp_plant",
        # Цветы
        "poppy",
        "dandelion",
        "blue_orchid",
        "allium",
        "azure_bluet",
        "open_eyeblossom",
        "closed_eyeblossom",
        "oxeye_daisy",
        "cornflower",
        "lily_of_the_valley",
        "wither_rose",
        "spore_blossom",
        "spore_blossom_base",
        "pink_petals",
        "pink_petals_stem",
        "wildflowers",
        "wildflowers_stem",
        "rose_bush_bottom",
        "rose_bush_top",
        "peony_bottom",
        "peony_top",
        "sunflower_back",
        "sunflower_bottom",
        "sunflower_front",
        "sunflower_top",
        "lilac_bottom",
        "lilac_top",
        "cactus_flower",
        "torchflower_crop_stage0",
        "torchflower_crop_stage1",
            # тюльпаны
            "red_tulip",
            "orange_tulip",
            "white_tulip",
            "pink_tulip",
        # Остальные растения
        "vine",
        "lily_pad",
    # Остальное
    "cobweb",
}

# Вода
LIST_WATER = {
	"water_still",
  	"water_flow",
}

# Цветное стекло (лицевая сторона)
LIST_STAINED_GLASS = {
    "blue_stained_glass",
    "brown_stained_glass",
    "cyan_stained_glass",
    "green_stained_glass",
    "light_blue_stained_glass",
    "lime_stained_glass",
    "magenta_stained_glass",
    "orange_stained_glass",
    "pink_stained_glass",
    "purple_stained_glass",
    "red_stained_glass",
    "yellow_stained_glass",
}

# Цветное стекло (верхушка панели)
LIST_STAINED_GLASS_PANE_TOP = {
    "blue_stained_glass_pane_top",
    "brown_stained_glass_pane_top",
    "cyan_stained_glass_pane_top",
    "green_stained_glass_pane_top",
    "light_blue_stained_glass_pane_top",
    "lime_stained_glass_pane_top",
    "magenta_stained_glass_pane_top",
    "orange_stained_glass_pane_top",
    "pink_stained_glass_pane_top",
    "purple_stained_glass_pane_top",
    "red_stained_glass_pane_top",
    "yellow_stained_glass_pane_top",
}

#Чёрно-белое стекло (лицевая сторона)
LIST_ACHROMATIC_GLASS = {
    "tinted_glass",
    "black_stained_glass",
    "gray_stained_glass",
    "light_gray_stained_glass",
    "white_stained_glass",
}

#Чёрно-белое стекло (верхушка панели)
LIST_ACHROMATIC_GLASS_PANE_TOP = {
    "black_stained_glass_pane_top",
    "gray_stained_glass_pane_top",
    "light_gray_stained_glass_pane_top",
    "white_stained_glass_pane_top",
}

# Обычное стекло (лицевая сторона)
LIST_GLASS = {
    "glass",
}

# Обычное стекло (верхушка панели)
LIST_GLASS_PANE_TOP = {
    "glass_pane_top",
}

# Лёд (обычный прозрачный)
LIST_ICE = {
    "ice",
}

# Подповерхностное рассеивание в плотных блоках (слабое SSS)
LIST_SSS_DENSE = {
    # Грибы
    "brown_mushroom_block",
    "mushroom_block_inside",
    "red_mushroom_block",
    # "mushroom_stem", # нормальная карта «круглая», поэтому SSS не нужен
    # Мох
    "moss_block",
    "pale_moss_block",
    "moss_carpet",
    "pale_moss_carpet",
    # Шерсть
    "black_wool",
    "blue_wool",
    "brown_wool",
    "cyan_wool",
    "gray_wool",
    "green_wool",
    "light_blue_wool",
    "light_gray_wool",
    "lime_wool",
    "magenta_wool",
    "orange_wool",
    "pink_wool",
    "purple_wool",
    "red_wool",
    "white_wool",
    "yellow_wool",
    # Остальное
    "honeycomb_block",
    "wet_sponge",
    "snow",
    "powder_snow",
    "cake_side",
    "cake_top",
}

# Подповерхностное рассеивание в легкопроницаемых блоках (сильное SSS)
LIST_SSS_SPARSE = {
    "sponge",
    "hay_block_side",
    "hay_block_top",
    "packed_ice",
    "blue_ice",
    "frosted_ice_0",
    "frosted_ice_1",
    "frosted_ice_2",
    "frosted_ice_3",
}

# LIST_GOLD = {
#     "gold_block",
# }

# ==========================================
# ОПРЕДЕЛЕНИЕ ФУНКЦИЙ
# ==========================================

# --- СБРОС АВТОМАТИЗАЦИИ

# Функция сброса узлов
def reset_material_to_vanilla(mat):
    """
    Удаляет все узлы внутри фреймов 'Auto_*' и восстанавливает связь
    Principled BSDF -> Output.
    """
    if not mat.use_nodes:
        return False

    tree = mat.node_tree
    nodes = tree.nodes
    links = tree.links

    # 1. Находим все фреймы, созданные нашими скриптами
    # (Имя начинается с "Auto_")
    auto_frames = [n for n in nodes if n.type == 'FRAME' and n.name.startswith("Auto_")]

    if not auto_frames:
        return False  # В этом материале нет нашей автоматизации

    # 2. Находим все ноды, которые лежат внутри этих фреймов
    nodes_to_delete = []
    for node in nodes:
        # Проверяем, является ли родитель ноды одним из наших фреймов
        if node.parent in auto_frames:
            nodes_to_delete.append(node)

    # 3. Удаляем ноды
    # Сначала удаляем содержимое
    for node in nodes_to_delete:
        nodes.remove(node)
    
    # Потом удаляем сами фреймы
    for frame in auto_frames:
        nodes.remove(frame)

    # 4. Восстанавливаем прямую связь (Principled -> Output)
    principled = next((n for n in nodes if n.type == 'BSDF_PRINCIPLED'), None)
    output_node = next((n for n in nodes if n.type == 'OUTPUT_MATERIAL'), None)

    if principled and output_node:
        # Блендер достаточно умен: если мы создаем новую связь в тот же вход,
        # старая связь (даже если она сломана) заменяется новой.
        # Обычно 'BSDF' - это первый выход, 'Surface' - первый вход.
        links.new(principled.outputs[0], output_node.inputs[0])

    # 5. Ищем текстуру цвета (Albedo), чтобы вернуть альфу
    # Ищем, что подключено во вход 'Base Color' у Principled BSDF
    base_color_socket = principled.inputs['Base Color']
    image_node = None
    
    if base_color_socket.is_linked:
        # Берём узел, от которого идёт связь
        image_node = base_color_socket.links[0].from_node
        # Проверяем, точно ли это картинка
        if image_node.type != 'TEX_IMAGE':
            print(f"В {mat.name} к цвету подключена не картинка, а {image_node.type}")
            # Можно прервать или продолжить, но лучше прервать пока
            # return 
    else:
        print(f"В {mat.name} нет текстуры, подключенной к Base Color")
        return

    # 6. Возвращаем альфу
    if image_node.image:
        # Меняем режим альфы на "None" (игнорировать прозрачность)
        image_node.image.alpha_mode = 'STRAIGHT'

    return True
  
# Запуск сброса автоматизации  
def undo_nodes_automation():
    print("--- ЗАПУСК ПОЛНОГО СБРОСА (UNDO) ---")
    reset_count = 0
    
    for mat in bpy.data.materials:
        if reset_material_to_vanilla(mat):
            print(f"Сброшен: {mat.name}")
            reset_count += 1
            
    print(f"--- Готово. Сброшено материалов: {reset_count} ---")

# Интерполяция «ближайшие соседи»
def set_closest_interpolation():
    # Проходимся по всем материалам в проекте
    for material in bpy.data.materials:
        # Проверяем, использует ли материал ноды
        if material.use_nodes:
            # Проходимся по всем узлам (nodes) внутри материала
            for node in material.node_tree.nodes:
                # Проверяем тип узла: является ли он "Image Texture"
                if node.type == 'TEX_IMAGE':
                    # Меняем интерполяцию
                    node.interpolation = 'Closest'
                    print(f"Material: {material.name} | Node: {node.name} -> Closest")

# --- ФУНКЦИИ ДОНАСТРОЙКИ МАТЕРИАЛОВ ---
    
# Сильное свечение
def setup_emission_strong(mat):
    # Получаем доступ к нодам
    nodes = mat.node_tree.nodes
    
    # Ищем Principled BSDF
    principled = next((n for n in nodes if n.type == 'BSDF_PRINCIPLED'), None)
    
    if principled:
        try:
            # Устанавливаем силу свечения
            principled.inputs[28].default_value = 20.0
            print(f"[Свет] {mat.name}: Яркость установлена на 20")
        except KeyError:
            print(f"[Ошибка] У материала {mat.name} нет слота 'Emission Strength'")
    
# Просвечивание
def setup_translucency(mat):
  
    tree = mat.node_tree
    nodes = tree.nodes
    links = tree.links
    
    # 1. Проверка: не настроен ли он уже?
    # Если в нодах уже есть фрейм с названием "Auto_Translucency", выходим
    if "Auto_Translucency" in nodes:
        print(f"Материал {mat.name} уже настроен.")
        return

    # 2. Ищем ключевые узлы (Якоря)
    # Нам нужно найти Principled BSDF и Output
    principled = next((n for n in nodes if n.type == 'BSDF_PRINCIPLED'), None)
    output_node = next((n for n in nodes if n.type == 'OUTPUT_MATERIAL'), None)
    
    if not principled or not output_node:
        print(f"В материале {mat.name} нет Principled BSDF или Output!")
        return

    # 3. Ищем текстуру цвета (Albedo)
    # Ищем, что подключено во вход 'Base Color' у Principled BSDF
    base_color_socket = principled.inputs['Base Color']
    image_node = None
    
    if base_color_socket.is_linked:
        # Берём узел, от которого идёт связь
        image_node = base_color_socket.links[0].from_node
        # Проверяем, точно ли это картинка
        if image_node.type != 'TEX_IMAGE':
            print(f"В {mat.name} к цвету подключена не картинка, а {image_node.type}")
            # Можно прервать или продолжить, но лучше прервать пока
            # return 
    else:
        print(f"В {mat.name} нет текстуры, подключенной к Base Color")
        return

    # ==========================================
    # 4. СОЗДАНИЕ НОВЫХ НОД (как на скриншоте)
    # ==========================================
    
    # Создаем Фрейм
    frame = nodes.new('NodeFrame')
    frame.name = "Auto_Translucency"
    frame.label = "Auto Translucency"
    
    # Invert Color (для инверсии Альфы)
    invert_node = nodes.new('ShaderNodeInvert')
    invert_node.parent = frame
    invert_node.location = (principled.location.x, principled.location.y - 400)
    
    # Hue/Saturation (для насыщенности транслюценции)
    hsv_node = nodes.new('ShaderNodeHueSaturation')
    hsv_node.inputs['Saturation'].default_value = 2.0  # Как ты просил
    hsv_node.inputs['Value'].default_value = 1.0
    hsv_node.parent = frame
    hsv_node.location = (principled.location.x, principled.location.y - 800)
    
    # Translucent BSDF
    translucent_node = nodes.new('ShaderNodeBsdfTranslucent')
    translucent_node.parent = frame
    translucent_node.location = (principled.location.x + 200, principled.location.y - 800)
    
    # Transparent BSDF (Прозрачность)
    transparent_node = nodes.new('ShaderNodeBsdfTransparent')
    transparent_node.parent = frame
    transparent_node.location = (principled.location.x + 200, principled.location.y - 400)
    
    # Add Shader (Смешиваем Principled + Translucent)
    add_node = nodes.new('ShaderNodeAddShader')
    add_node.parent = frame
    add_node.location = (principled.location.x + 400, principled.location.y - 800)
    
    # Mix Shader Adjustment (Регулировка силы просвечивания)
    mix_adjustment_node = nodes.new('ShaderNodeMixShader')
    mix_adjustment_node.inputs['Factor'].default_value = 0.8 # Чем больше число, чем больше просвечивания
    mix_adjustment_node.parent = frame
    mix_adjustment_node.location = (principled.location.x + 600, principled.location.y - 700)
    
    # Mix Shader Final (Финальное смешивание по маске)
    mix_final_node = nodes.new('ShaderNodeMixShader')
    mix_final_node.parent = frame
    mix_final_node.location = (principled.location.x + 800, principled.location.y - 600)

    # ==========================================
    # 5. СОЕДИНЕНИЕ НОД (Линковка)
    # ==========================================
    
    # Сначала очистим связь Principled -> Output, так как мы врежемся между ними
    if output_node.inputs['Surface'].is_linked:
        tree.links.remove(output_node.inputs['Surface'].links[0])

    # Ветка 1: Translucency (Свет на просвет)
    # Image Color -> HSV -> Translucent -> Add Shader (нижний слот)
    links.new(image_node.outputs['Color'], hsv_node.inputs['Color'])
    links.new(hsv_node.outputs['Color'], translucent_node.inputs['Color'])
    links.new(translucent_node.outputs['BSDF'], add_node.inputs[1]) # [1] - второй слот
    
    # Principled -> Add Shader (верхний слот)
    links.new(principled.outputs['BSDF'], add_node.inputs[0])
    
    # Ветка 2: Transparency (Прозрачность блоков)
    links.new(image_node.outputs['Alpha'], invert_node.inputs['Color'])
    links.new(invert_node.outputs['Color'], transparent_node.inputs['Color'])
    
    # Ветка 3: Сборка в Mix Shader Adjustment
    links.new(principled.outputs['BSDF'], mix_adjustment_node.inputs[1]) 
    links.new(add_node.outputs['Shader'], mix_adjustment_node.inputs[2]) 
    
    # Ветка 3: Сборка в Mix Shader Final
    links.new(image_node.outputs['Alpha'], mix_final_node.inputs['Factor'])
    links.new(transparent_node.outputs['BSDF'], mix_final_node.inputs[1])
    links.new(mix_adjustment_node.outputs['Shader'], mix_final_node.inputs[2]) 
    
    # Mix -> Output
    links.new(mix_final_node.outputs['Shader'], output_node.inputs['Surface'])

    print(f"Материал {mat.name} успешно обновлён!")
    
# Вода
def setup_water(mat):
  
    tree = mat.node_tree
    nodes = tree.nodes
    links = tree.links
    
    # 1. Проверка: не настроен ли он уже?
    # Если в нодах уже есть фрейм с названием "Auto_Translucency", выходим
    if "Auto_Water" in nodes:
        print(f"Материал {mat.name} уже настроен.")
        return

    # 2. Ищем ключевые узлы (Якоря)
    # Нам нужно найти Principled BSDF и Output
    principled = next((n for n in nodes if n.type == 'BSDF_PRINCIPLED'), None)
    output_node = next((n for n in nodes if n.type == 'OUTPUT_MATERIAL'), None)
    normal_node = next((n for n in nodes if n.type == 'NORMAL_MAP'), None)
    
    if not principled or not output_node:
        print(f"В материале {mat.name} нет Principled BSDF или Output!")
        return

    # ==========================================
    # 3. СОЗДАНИЕ НОВЫХ НОД
    # ==========================================
    
    # Создаем Фрейм
    frame = nodes.new('NodeFrame')
    frame.name = "Auto_Water"
    frame.label = "Auto Water"
    
    # Glass BSDF (для реалистичных отражений)
    glass_node = nodes.new('ShaderNodeBsdfGlass')
    glass_node.inputs['Roughness'].default_value = 0.05
    glass_node.inputs['IOR'].default_value = 1.33
    glass_node.parent = frame
    glass_node.location = (principled.location.x, principled.location.y - 400)
    
    # Volume Scatter (для объёма)
    volume_node = nodes.new('ShaderNodeVolumeScatter')
    volume_node.phase = 'FOURNIER_FORAND'
    volume_node.inputs['Density'].default_value = 0.8
    volume_node.inputs['IOR'].default_value = 1.33
    volume_node.inputs['Backscatter'].default_value = 0.08
    volume_node.parent = frame
    volume_node.location = (principled.location.x, principled.location.y - 600)

    # ==========================================
    # 4. СОЕДИНЕНИЕ НОД (Линковка)
    # ==========================================
    
    # Сначала очистим связь Principled -> Output, так как мы врежемся между ними
    if output_node.inputs['Surface'].is_linked:
        tree.links.remove(output_node.inputs['Surface'].links[0])

	# Normal map -> Glass BSDF
    links.new(normal_node.outputs['Normal'], glass_node.inputs['Normal'])        
        
    # Glass BSDF -> Surface
    links.new(glass_node.outputs['BSDF'], output_node.inputs['Surface'])
    
    # Volume Scatter -> Surface
    links.new(volume_node.outputs['Volume'], output_node.inputs['Volume'])
        
    print(f"Материал {mat.name} успешно обновлён!")
    
# Цветное стекло
def setup_stained_glass(mat):
  
    tree = mat.node_tree
    nodes = tree.nodes
    links = tree.links
    
    # 1. Проверка: не настроен ли он уже?
    # Если в нодах уже есть фрейм с названием "Auto_Stained_Glass", выходим
    if "Auto_Stained_Glass" in nodes:
        print(f"Материал {mat.name} уже настроен.")
        return

    # 2. Ищем ключевые узлы (Якоря)
    # Нам нужно найти Principled BSDF и Output
    principled = next((n for n in nodes if n.type == 'BSDF_PRINCIPLED'), None)
    output_node = next((n for n in nodes if n.type == 'OUTPUT_MATERIAL'), None)
    separate_node = next((n for n in nodes if n.type == 'SEPARATE_COLOR'), None)
    normal_node = next((n for n in nodes if n.type == 'NORMAL_MAP'), None)
    
    if not principled or not output_node:
        print(f"В материале {mat.name} нет Principled BSDF или Output!")
        return

    # 3. Ищем текстуру цвета (Albedo)
    # Ищем, что подключено во вход 'Base Color' у Principled BSDF
    base_color_socket = principled.inputs['Base Color']
    image_node = None
    
    if base_color_socket.is_linked:
        # Берём узел, от которого идёт связь
        image_node = base_color_socket.links[0].from_node
        # Проверяем, точно ли это картинка
        if image_node.type != 'TEX_IMAGE':
            print(f"В {mat.name} к цвету подключена не картинка, а {image_node.type}")
            # Можно прервать или продолжить, но лучше прервать пока
            # return 
    else:
        print(f"В {mat.name} нет текстуры, подключенной к Base Color")
        return
    
    # 4. Отключим альфу, чтобы текстура не затемнялась, а прозрачность пропала
    if image_node.image:
        # Меняем режим альфы на "None" (игнорировать прозрачность)
        image_node.image.alpha_mode = 'NONE'

    # ==========================================
    # 5. СОЗДАНИЕ НОВЫХ НОД
    # ==========================================
    
    # Создаем Фрейм
    frame = nodes.new('NodeFrame')
    frame.name = "Auto_Stained_Glass"
    frame.label = "Auto Stained Glass"

    # Separate Color (чтобы насыщенность и яркость максимизировать)
    separate_hsv_node = nodes.new('ShaderNodeSeparateColor')
    separate_hsv_node.mode = 'HSV'
    separate_hsv_node.parent = frame
    separate_hsv_node.location = (principled.location.x, principled.location.y - 400)

    # Combine Color (чтобы насыщенность и яркость максимизировать)
    combine_node = nodes.new('ShaderNodeCombineColor')
    combine_node.mode = 'HSV'
    combine_node.inputs[1].default_value = 0.4 # Насыщенность стекла
    combine_node.inputs[2].default_value = 1.0 # Светлота стекла
    combine_node.parent = frame
    combine_node.location = (principled.location.x + 200, principled.location.y - 400)

    # Fresnel (чтобы отражения были только под определённым углом. Это нужно для реалистичности)   
    fresnel_node = nodes.new('ShaderNodeFresnel')
    fresnel_node.inputs['IOR'].default_value = 1.45 # Показатель преломления
    fresnel_node.parent = frame
    fresnel_node.location = (principled.location.x + 400, principled.location.y - 400)

    # Refraction BSDF (для преломления света)
    refraction_node = nodes.new('ShaderNodeBsdfRefraction')
    refraction_node.inputs['IOR'].default_value = 1.45 # Показатель преломления
    refraction_node.parent = frame
    refraction_node.location = (principled.location.x + 400, principled.location.y - 600)

    # Glossy BSDF (для отражений и бликов)
    glossy_node = nodes.new('ShaderNodeBsdfAnisotropic')
    glossy_node.inputs['Color'].default_value = (1.0, 1.0, 1.0, 1.0)
    glossy_node.parent = frame
    glossy_node.location = (principled.location.x + 400, principled.location.y - 800)

    # Mix Shader (Угол Френеля + преломление + отражения = реалистичное стекло)
    mix_node = nodes.new('ShaderNodeMixShader')
    mix_node.parent = frame
    mix_node.location = (principled.location.x + 600, principled.location.y - 400)

    # ==========================================
    # 6. СОЕДИНЕНИЕ НОД (Линковка)
    # ==========================================
    
    # Сначала очистим связь Principled -> Output, так как мы врежемся между ними
    if output_node.inputs['Surface'].is_linked:
        tree.links.remove(output_node.inputs['Surface'].links[0])

    # Обработка базового цвета
    links.new(image_node.outputs['Color'], separate_hsv_node.inputs['Color'])
    links.new(separate_hsv_node.outputs[0], combine_node.inputs[0])

    # Подключаем все нормальные карты
    links.new(normal_node.outputs['Normal'], fresnel_node.inputs['Normal'])
    links.new(normal_node.outputs['Normal'], refraction_node.inputs['Normal'])
    links.new(normal_node.outputs['Normal'], glossy_node.inputs['Normal'])

    # Подключаем все карты шероховатостей
    links.new(separate_node.outputs['Red'], refraction_node.inputs['Roughness'])
    links.new(separate_node.outputs['Red'], glossy_node.inputs['Roughness'])

    # Устанавливаем обработанный цвет для преломления
    links.new(combine_node.outputs['Color'], refraction_node.inputs['Color'])

    # Соединяем все шейдеры в миксере для реалистичного стекла
    links.new(fresnel_node.outputs['Factor'], mix_node.inputs[0]) # Первый вход
    links.new(refraction_node.outputs['BSDF'], mix_node.inputs[1]) # Второй вход
    links.new(glossy_node.outputs['BSDF'], mix_node.inputs[2]) # Третий вход
    
    # Mix -> Output
    links.new(mix_node.outputs['Shader'], output_node.inputs['Surface'])

    print(f"Материал {mat.name} успешно обновлён!")

# Цветное стекло (верхушка панели)
def setup_stained_glass_pane_top(mat):
  
    tree = mat.node_tree
    nodes = tree.nodes
    links = tree.links
    
    # 1. Проверка: не настроен ли он уже?
    # Если в нодах уже есть фрейм с названием "Auto_Stained_Glass_Pane_Top", выходим
    if "Auto_Stained_Glass_Pane_Top" in nodes:
        print(f"Материал {mat.name} уже настроен.")
        return

    # 2. Ищем ключевые узлы (Якоря)
    # Нам нужно найти Principled BSDF и Output
    principled = next((n for n in nodes if n.type == 'BSDF_PRINCIPLED'), None)
    output_node = next((n for n in nodes if n.type == 'OUTPUT_MATERIAL'), None)
    
    if not principled or not output_node:
        print(f"В материале {mat.name} нет Principled BSDF или Output!")
        return

    # 3. Ищем текстуру цвета (Albedo)
    # Ищем, что подключено во вход 'Base Color' у Principled BSDF
    base_color_socket = principled.inputs['Base Color']
    image_node = None
    
    if base_color_socket.is_linked:
        # Берём узел, от которого идёт связь
        image_node = base_color_socket.links[0].from_node
        # Проверяем, точно ли это картинка
        if image_node.type != 'TEX_IMAGE':
            print(f"В {mat.name} к цвету подключена не картинка, а {image_node.type}")
            # Можно прервать или продолжить, но лучше прервать пока
            # return 
    else:
        print(f"В {mat.name} нет текстуры, подключенной к Base Color")
        return
    
    # 4. Отключим альфу, чтобы текстура не затемнялась, а прозрачность пропала
    if image_node.image:
        # Меняем режим альфы на "None" (игнорировать прозрачность)
        image_node.image.alpha_mode = 'NONE'

    # ==========================================
    # 5. СОЗДАНИЕ НОВЫХ НОД
    # ==========================================
    
    # Создаем Фрейм
    frame = nodes.new('NodeFrame')
    frame.name = "Auto_Stained_Glass_Pane_Top"
    frame.label = "Auto Stained Glass Pane Top"

    # Separate Color (чтобы насыщенность и яркость максимизировать)
    separate_hsv_node = nodes.new('ShaderNodeSeparateColor')
    separate_hsv_node.mode = 'HSV'
    separate_hsv_node.parent = frame
    separate_hsv_node.location = (principled.location.x, principled.location.y - 400)

    # Combine Color (чтобы насыщенность и яркость максимизировать)
    combine_node = nodes.new('ShaderNodeCombineColor')
    combine_node.mode = 'HSV'
    combine_node.inputs[1].default_value = 0.4 # Насыщенность стекла
    combine_node.inputs[2].default_value = 1.0 # Светлота стекла
    combine_node.parent = frame
    combine_node.location = (principled.location.x + 200, principled.location.y - 400)

    # Fresnel (чтобы отражения были только под определённым углом. Это нужно для реалистичности)   
    fresnel_node = nodes.new('ShaderNodeFresnel')
    fresnel_node.inputs['IOR'].default_value = 1.45 # Показатель преломления
    fresnel_node.parent = frame
    fresnel_node.location = (principled.location.x + 400, principled.location.y - 400)

    # Refraction BSDF (для преломления света)
    refraction_node = nodes.new('ShaderNodeBsdfRefraction')
    refraction_node.inputs['IOR'].default_value = 1.45 # Показатель преломления
    refraction_node.inputs['Roughness'].default_value = 0.047 # Чтобы «срез» не был слишком гладким
    refraction_node.parent = frame
    refraction_node.location = (principled.location.x + 400, principled.location.y - 600)

    # Glossy BSDF (для отражений и бликов)
    glossy_node = nodes.new('ShaderNodeBsdfAnisotropic')
    glossy_node.inputs['Color'].default_value = (1.0, 1.0, 1.0, 1.0)
    glossy_node.parent = frame
    glossy_node.location = (principled.location.x + 400, principled.location.y - 800)

    # Mix Shader (Угол Френеля + преломление + отражения = реалистичное стекло)
    mix_node = nodes.new('ShaderNodeMixShader')
    mix_node.parent = frame
    mix_node.location = (principled.location.x + 600, principled.location.y - 400)

    # ==========================================
    # 6. СОЕДИНЕНИЕ НОД (Линковка)
    # ==========================================
    
    # Сначала очистим связь Principled -> Output, так как мы врежемся между ними
    if output_node.inputs['Surface'].is_linked:
        tree.links.remove(output_node.inputs['Surface'].links[0])

    # Обработка базового цвета
    links.new(image_node.outputs['Color'], separate_hsv_node.inputs['Color'])
    links.new(separate_hsv_node.outputs[0], combine_node.inputs[0])

    # Устанавливаем обработанный цвет для преломления
    links.new(combine_node.outputs['Color'], refraction_node.inputs['Color'])

    # Соединяем все шейдеры в миксере для реалистичного стекла
    links.new(fresnel_node.outputs['Factor'], mix_node.inputs[0]) # Первый вход
    links.new(refraction_node.outputs['BSDF'], mix_node.inputs[1]) # Второй вход
    links.new(glossy_node.outputs['BSDF'], mix_node.inputs[2]) # Третий вход
    
    # Mix -> Output
    links.new(mix_node.outputs['Shader'], output_node.inputs['Surface'])

    print(f"Материал {mat.name} успешно обновлён!")

# Чёрно-белое стекло (лицевая сторона)
def setup_achromatic_glass(mat):
  
    tree = mat.node_tree
    nodes = tree.nodes
    links = tree.links
    
    # 1. Проверка: не настроен ли он уже?
    # Если в нодах уже есть фрейм с названием "Auto_Achromatic_Glass", выходим
    if "Auto_Achromatic_Glass" in nodes:
        print(f"Материал {mat.name} уже настроен.")
        return

    # 2. Ищем ключевые узлы (Якоря)
    # Нам нужно найти Principled BSDF и Output
    principled = next((n for n in nodes if n.type == 'BSDF_PRINCIPLED'), None)
    output_node = next((n for n in nodes if n.type == 'OUTPUT_MATERIAL'), None)
    separate_node = next((n for n in nodes if n.type == 'SEPARATE_COLOR'), None)
    normal_node = next((n for n in nodes if n.type == 'NORMAL_MAP'), None)
    
    if not principled or not output_node:
        print(f"В материале {mat.name} нет Principled BSDF или Output!")
        return

    # 3. Ищем текстуру цвета (Albedo)
    # Ищем, что подключено во вход 'Base Color' у Principled BSDF
    base_color_socket = principled.inputs['Base Color']
    image_node = None
    
    if base_color_socket.is_linked:
        # Берём узел, от которого идёт связь
        image_node = base_color_socket.links[0].from_node
        # Проверяем, точно ли это картинка
        if image_node.type != 'TEX_IMAGE':
            print(f"В {mat.name} к цвету подключена не картинка, а {image_node.type}")
            # Можно прервать или продолжить, но лучше прервать пока
            # return 
    else:
        print(f"В {mat.name} нет текстуры, подключенной к Base Color")
        return
    
    # 4. Отключим альфу, чтобы текстура не затемнялась, а прозрачность пропала
    if image_node.image:
        # Меняем режим альфы на "None" (игнорировать прозрачность)
        image_node.image.alpha_mode = 'NONE'

    # 5. Отключим прохождение света для Principled BSDF: пусть это будет чисто слой краски
    principled.inputs[18].default_value = 0.0

    # ==========================================
    # 6. СОЗДАНИЕ НОВЫХ НОД
    # ==========================================
    
    # Создаем Фрейм
    frame = nodes.new('NodeFrame')
    frame.name = "Auto_Achromatic_Glass"
    frame.label = "Auto Achromatic Glass"

    # Fresnel (чтобы отражения были только под определённым углом. Это нужно для реалистичности)   
    fresnel_node = nodes.new('ShaderNodeFresnel')
    fresnel_node.inputs['IOR'].default_value = 1.45 # Показатель преломления
    fresnel_node.parent = frame
    fresnel_node.location = (principled.location.x, principled.location.y - 400)

    # Refraction BSDF (для преломления света)
    refraction_node = nodes.new('ShaderNodeBsdfRefraction')
    refraction_node.inputs['IOR'].default_value = 1.45 # Показатель преломления
    refraction_node.inputs['Color'].default_value = (1.0, 1.0, 1.0, 1.0)
    refraction_node.parent = frame
    refraction_node.location = (principled.location.x, principled.location.y - 600)

    # Glossy BSDF (для отражений и бликов)
    glossy_node = nodes.new('ShaderNodeBsdfAnisotropic')
    glossy_node.inputs['Color'].default_value = (1.0, 1.0, 1.0, 1.0)
    glossy_node.parent = frame
    glossy_node.location = (principled.location.x, principled.location.y - 800)

    # Mix Shader (Угол Френеля + преломление + отражения = реалистичное стекло)
    mix_node = nodes.new('ShaderNodeMixShader')
    mix_node.parent = frame
    mix_node.location = (principled.location.x + 200, principled.location.y - 400)

    # Final Mix Shader (Principled BSDF + реалистичное стекло = белое стекло)
    final_mix_node = nodes.new('ShaderNodeMixShader')
    final_mix_node.inputs['Factor'].default_value = 0.1
    final_mix_node.parent = frame
    final_mix_node.location = (principled.location.x + 400, principled.location.y - 400)

    # ==========================================
    # 7. СОЕДИНЕНИЕ НОД (Линковка)
    # ==========================================
    
    # Сначала очистим связь Principled -> Output, так как мы врежемся между ними
    if output_node.inputs['Surface'].is_linked:
        tree.links.remove(output_node.inputs['Surface'].links[0])

    # Подключаем все нормальные карты
    links.new(normal_node.outputs['Normal'], fresnel_node.inputs['Normal'])
    links.new(normal_node.outputs['Normal'], refraction_node.inputs['Normal'])
    links.new(normal_node.outputs['Normal'], glossy_node.inputs['Normal'])

    # Подключаем все карты шероховатостей
    links.new(separate_node.outputs['Red'], refraction_node.inputs['Roughness'])
    links.new(separate_node.outputs['Red'], glossy_node.inputs['Roughness'])

    # Соединяем все шейдеры в миксере для реалистичного стекла
    links.new(fresnel_node.outputs['Factor'], mix_node.inputs[0]) # Первый вход
    links.new(refraction_node.outputs['BSDF'], mix_node.inputs[1]) # Второй вход
    links.new(glossy_node.outputs['BSDF'], mix_node.inputs[2]) # Третий вход

    # Mix -> Final Mix (добавляем на поверхность стекла краску)
    links.new(mix_node.outputs['Shader'], final_mix_node.inputs[1])
    links.new(principled.outputs['BSDF'], final_mix_node.inputs[2])

    # Final Mix -> Output
    links.new(final_mix_node.outputs['Shader'], output_node.inputs['Surface'])

    print(f"Материал {mat.name} успешно обновлён!")

# Чёрно-белое стекло (верхушка панели)
def setup_achromatic_glass_pane_top(mat):
  
    tree = mat.node_tree
    nodes = tree.nodes
    links = tree.links
    
    # 1. Проверка: не настроен ли он уже?
    # Если в нодах уже есть фрейм с названием "Auto_Achromatic_Glass_Pane_Top", выходим
    if "Auto_Achromatic_Glass_Pane_Top" in nodes:
        print(f"Материал {mat.name} уже настроен.")
        return

    # 2. Ищем ключевые узлы (Якоря)
    # Нам нужно найти Principled BSDF и Output
    principled = next((n for n in nodes if n.type == 'BSDF_PRINCIPLED'), None)
    output_node = next((n for n in nodes if n.type == 'OUTPUT_MATERIAL'), None)
    
    if not principled or not output_node:
        print(f"В материале {mat.name} нет Principled BSDF или Output!")
        return

    # 3. Ищем текстуру цвета (Albedo)
    # Ищем, что подключено во вход 'Base Color' у Principled BSDF
    base_color_socket = principled.inputs['Base Color']
    image_node = None
    
    if base_color_socket.is_linked:
        # Берём узел, от которого идёт связь
        image_node = base_color_socket.links[0].from_node
        # Проверяем, точно ли это картинка
        if image_node.type != 'TEX_IMAGE':
            print(f"В {mat.name} к цвету подключена не картинка, а {image_node.type}")
            # Можно прервать или продолжить, но лучше прервать пока
            # return 
    else:
        print(f"В {mat.name} нет текстуры, подключенной к Base Color")
        return
    
    # 4. Отключим альфу, чтобы текстура не затемнялась, а прозрачность пропала
    if image_node.image:
        # Меняем режим альфы на "None" (игнорировать прозрачность)
        image_node.image.alpha_mode = 'NONE'

    # 5. Отключим прохождение света для Principled BSDF: пусть это будет чисто слой краски
    principled.inputs[18].default_value = 0.0

    # ==========================================
    # 6. СОЗДАНИЕ НОВЫХ НОД
    # ==========================================
    
    # Создаем Фрейм
    frame = nodes.new('NodeFrame')
    frame.name = "Auto_Achromatic_Glass_Pane_Top"
    frame.label = "Auto Achromatic Glass Pane Top"

    # Fresnel (чтобы отражения были только под определённым углом. Это нужно для реалистичности)   
    fresnel_node = nodes.new('ShaderNodeFresnel')
    fresnel_node.inputs['IOR'].default_value = 1.45 # Показатель преломления
    fresnel_node.parent = frame
    fresnel_node.location = (principled.location.x, principled.location.y - 400)

    # Refraction BSDF (для преломления света)
    refraction_node = nodes.new('ShaderNodeBsdfRefraction')
    refraction_node.inputs['IOR'].default_value = 1.45 # Показатель преломления
    refraction_node.inputs['Color'].default_value = (1.0, 1.0, 1.0, 1.0)
    refraction_node.inputs['Roughness'].default_value = 0.047 # Чтобы «срез» не был слишком гладким
    refraction_node.parent = frame
    refraction_node.location = (principled.location.x, principled.location.y - 600)

    # Glossy BSDF (для отражений и бликов)
    glossy_node = nodes.new('ShaderNodeBsdfAnisotropic')
    glossy_node.inputs['Color'].default_value = (1.0, 1.0, 1.0, 1.0)
    glossy_node.parent = frame
    glossy_node.location = (principled.location.x, principled.location.y - 800)

    # Mix Shader (Угол Френеля + преломление + отражения = реалистичное стекло)
    mix_node = nodes.new('ShaderNodeMixShader')
    mix_node.parent = frame
    mix_node.location = (principled.location.x + 200, principled.location.y - 400)

    # Final Mix Shader (Principled BSDF + реалистичное стекло = белое стекло)
    final_mix_node = nodes.new('ShaderNodeMixShader')
    final_mix_node.inputs['Factor'].default_value = 0.1
    final_mix_node.parent = frame
    final_mix_node.location = (principled.location.x + 400, principled.location.y - 400)

    # ==========================================
    # 7. СОЕДИНЕНИЕ НОД (Линковка)
    # ==========================================
    
    # Сначала очистим связь Principled -> Output, так как мы врежемся между ними
    if output_node.inputs['Surface'].is_linked:
        tree.links.remove(output_node.inputs['Surface'].links[0])

    # Соединяем все шейдеры в миксере для реалистичного стекла
    links.new(fresnel_node.outputs['Factor'], mix_node.inputs[0]) # Первый вход
    links.new(refraction_node.outputs['BSDF'], mix_node.inputs[1]) # Второй вход
    links.new(glossy_node.outputs['BSDF'], mix_node.inputs[2]) # Третий вход

    # Mix -> Final Mix (добавляем на поверхность стекла краску)
    links.new(mix_node.outputs['Shader'], final_mix_node.inputs[1])
    links.new(principled.outputs['BSDF'], final_mix_node.inputs[2])

    # Final Mix -> Output
    links.new(final_mix_node.outputs['Shader'], output_node.inputs['Surface'])

    print(f"Материал {mat.name} успешно обновлён!")

# Обычное стекло
def setup_glass(mat):
  
    tree = mat.node_tree
    nodes = tree.nodes
    links = tree.links
    
    # 1. Проверка: не настроен ли он уже?
    # Если в нодах уже есть фрейм с названием "Auto_Glass", выходим
    if "Auto_Glass" in nodes:
        print(f"Материал {mat.name} уже настроен.")
        return

    # 2. Ищем ключевые узлы (Якоря)
    # Нам нужно найти Principled BSDF и Output
    principled = next((n for n in nodes if n.type == 'BSDF_PRINCIPLED'), None)
    output_node = next((n for n in nodes if n.type == 'OUTPUT_MATERIAL'), None)
    separate_node = next((n for n in nodes if n.type == 'SEPARATE_COLOR'), None)
    normal_node = next((n for n in nodes if n.type == 'NORMAL_MAP'), None)
    
    if not principled or not output_node:
        print(f"В материале {mat.name} нет Principled BSDF или Output!")
        return

    # 3. Ищем текстуру цвета (Albedo)
    # Ищем, что подключено во вход 'Base Color' у Principled BSDF
    base_color_socket = principled.inputs['Base Color']
    image_node = None
    
    if base_color_socket.is_linked:
        # Берём узел, от которого идёт связь
        image_node = base_color_socket.links[0].from_node
        # Проверяем, точно ли это картинка
        if image_node.type != 'TEX_IMAGE':
            print(f"В {mat.name} к цвету подключена не картинка, а {image_node.type}")
            # Можно прервать или продолжить, но лучше прервать пока
            # return 
    else:
        print(f"В {mat.name} нет текстуры, подключенной к Base Color")
        return

    # ==========================================
    # 4. СОЗДАНИЕ НОВЫХ НОД
    # ==========================================
    
    # Создаем Фрейм
    frame = nodes.new('NodeFrame')
    frame.name = "Auto_Glass"
    frame.label = "Auto Glass"
    
    # Glass BSDF (реалистичное стекло)
    glass_node = nodes.new('ShaderNodeBsdfGlass')
    glass_node.inputs['IOR'].default_value = 1.45 # Показатель преломления
    glass_node.parent = frame
    glass_node.location = (principled.location.x, principled.location.y - 400)

    # ==========================================
    # 5. СОЕДИНЕНИЕ НОД (Линковка)
    # ==========================================
    
    # Сначала очистим связь Principled -> Output, так как мы врежемся между ними
    if output_node.inputs['Surface'].is_linked:
        tree.links.remove(output_node.inputs['Surface'].links[0])

    # Подключаем необходимое к Glass BSDF
    links.new(separate_node.outputs['Red'], glass_node.inputs['Roughness'])
    links.new(normal_node.outputs['Normal'], glass_node.inputs['Normal'])
    
    # Glass BSDF -> Output
    links.new(glass_node.outputs['BSDF'], output_node.inputs['Surface'])

    print(f"Материал {mat.name} успешно обновлён!")

# Обычное стекло (верхушка панели)
def setup_glass_pane_top(mat):
  
    tree = mat.node_tree
    nodes = tree.nodes
    links = tree.links
    
    # 1. Проверка: не настроен ли он уже?
    # Если в нодах уже есть фрейм с названием "Auto_Stained_Glass_Pane_Top", выходим
    if "Auto_Glass_Pane_Top" in nodes:
        print(f"Материал {mat.name} уже настроен.")
        return

    # 2. Ищем ключевые узлы (Якоря)
    # Нам нужно найти Principled BSDF и Output
    principled = next((n for n in nodes if n.type == 'BSDF_PRINCIPLED'), None)
    output_node = next((n for n in nodes if n.type == 'OUTPUT_MATERIAL'), None)
    
    if not principled or not output_node:
        print(f"В материале {mat.name} нет Principled BSDF или Output!")
        return

    # 3. Ищем текстуру цвета (Albedo)
    # Ищем, что подключено во вход 'Base Color' у Principled BSDF
    base_color_socket = principled.inputs['Base Color']
    image_node = None
    
    if base_color_socket.is_linked:
        # Берём узел, от которого идёт связь
        image_node = base_color_socket.links[0].from_node
        # Проверяем, точно ли это картинка
        if image_node.type != 'TEX_IMAGE':
            print(f"В {mat.name} к цвету подключена не картинка, а {image_node.type}")
            # Можно прервать или продолжить, но лучше прервать пока
            # return 
    else:
        print(f"В {mat.name} нет текстуры, подключенной к Base Color")
        return
    
    # ==========================================
    # 4. СОЗДАНИЕ НОВЫХ НОД
    # ==========================================
    
    # Создаем Фрейм
    frame = nodes.new('NodeFrame')
    frame.name = "Auto_Glass_Pane_Top"
    frame.label = "Auto Glass Pane Top"

    # Glass BSDF (реалистичное стекло)
    glass_node = nodes.new('ShaderNodeBsdfGlass')
    glass_node.inputs['IOR'].default_value = 1.45 # Показатель преломления
    glass_node.inputs['Roughness'].default_value = 0.047 # Чтобы «срез» не был слишком гладким
    glass_node.parent = frame
    glass_node.location = (principled.location.x, principled.location.y - 400)

    # ==========================================
    # 5. СОЕДИНЕНИЕ НОД (Линковка)
    # ==========================================
    
    # Сначала очистим связь Principled -> Output, так как мы врежемся между ними
    if output_node.inputs['Surface'].is_linked:
        tree.links.remove(output_node.inputs['Surface'].links[0])
    
    # Glass BSDF -> Output
    links.new(glass_node.outputs['BSDF'], output_node.inputs['Surface'])

    print(f"Материал {mat.name} успешно обновлён!")

# Лёд (обычный, прозрачный)
def setup_ice(mat):
  
    tree = mat.node_tree
    nodes = tree.nodes
    links = tree.links
    
    # 1. Проверка: не настроен ли он уже?
    # Если в нодах уже есть фрейм с названием "Auto_Ice", выходим
    if "Auto_Ice" in nodes:
        print(f"Материал {mat.name} уже настроен.")
        return

    # 2. Ищем ключевые узлы (Якоря)
    # Нам нужно найти Principled BSDF и Output
    principled = next((n for n in nodes if n.type == 'BSDF_PRINCIPLED'), None)
    output_node = next((n for n in nodes if n.type == 'OUTPUT_MATERIAL'), None)
    separate_node = next((n for n in nodes if n.type == 'SEPARATE_COLOR'), None)
    normal_node = next((n for n in nodes if n.type == 'NORMAL_MAP'), None)
    
    if not principled or not output_node:
        print(f"В материале {mat.name} нет Principled BSDF или Output!")
        return

    # 3. Ищем текстуру цвета (Albedo)
    # Ищем, что подключено во вход 'Base Color' у Principled BSDF
    base_color_socket = principled.inputs['Base Color']
    image_node = None
    
    if base_color_socket.is_linked:
        # Берём узел, от которого идёт связь
        image_node = base_color_socket.links[0].from_node
        # Проверяем, точно ли это картинка
        if image_node.type != 'TEX_IMAGE':
            print(f"В {mat.name} к цвету подключена не картинка, а {image_node.type}")
            # Можно прервать или продолжить, но лучше прервать пока
            # return 
    else:
        print(f"В {mat.name} нет текстуры, подключенной к Base Color")
        return
    
    # 4. Отключим альфу, чтобы текстура не затемнялась, а прозрачность пропала
    if image_node.image:
        # Меняем режим альфы на "None" (игнорировать прозрачность)
        image_node.image.alpha_mode = 'NONE'

    # ==========================================
    # 5. СОЗДАНИЕ НОВЫХ НОД
    # ==========================================
    
    # Создаем Фрейм
    frame = nodes.new('NodeFrame')
    frame.name = "Auto_Ice"
    frame.label = "Auto Ice"

    # Separate Color (чтобы насыщенность и яркость максимизировать)
    separate_hsv_node = nodes.new('ShaderNodeSeparateColor')
    separate_hsv_node.mode = 'HSV'
    separate_hsv_node.parent = frame
    separate_hsv_node.location = (principled.location.x, principled.location.y - 400)

    # Combine Color (чтобы насыщенность и яркость максимизировать)
    combine_node = nodes.new('ShaderNodeCombineColor')
    combine_node.mode = 'HSV'
    combine_node.inputs[1].default_value = 0.35 # Насыщенность льда
    combine_node.inputs[2].default_value = 1.0 # Светлота льда
    combine_node.parent = frame
    combine_node.location = (principled.location.x + 200, principled.location.y - 400)

    # Fresnel (чтобы отражения были только под определённым углом. Это нужно для реалистичности)   
    fresnel_node = nodes.new('ShaderNodeFresnel')
    fresnel_node.inputs['IOR'].default_value = 1.31 # Показатель преломления льда
    fresnel_node.parent = frame
    fresnel_node.location = (principled.location.x + 400, principled.location.y - 400)

    # Refraction BSDF (для преломления света)
    refraction_node = nodes.new('ShaderNodeBsdfRefraction')
    refraction_node.inputs['IOR'].default_value = 1.31 # Показатель преломления льда
    refraction_node.parent = frame
    refraction_node.location = (principled.location.x + 400, principled.location.y - 600)

    # Glossy BSDF (для отражений и бликов)
    glossy_node = nodes.new('ShaderNodeBsdfAnisotropic')
    glossy_node.inputs['Color'].default_value = (1.0, 1.0, 1.0, 1.0)
    glossy_node.parent = frame
    glossy_node.location = (principled.location.x + 400, principled.location.y - 800)

    # Mix Shader (Угол Френеля + преломление + отражения = реалистичный лёд)
    mix_node = nodes.new('ShaderNodeMixShader')
    mix_node.parent = frame
    mix_node.location = (principled.location.x + 600, principled.location.y - 400)

    # ==========================================
    # 6. СОЕДИНЕНИЕ НОД (Линковка)
    # ==========================================
    
    # Сначала очистим связь Principled -> Output, так как мы врежемся между ними
    if output_node.inputs['Surface'].is_linked:
        tree.links.remove(output_node.inputs['Surface'].links[0])

    # Обработка базового цвета
    links.new(image_node.outputs['Color'], separate_hsv_node.inputs['Color'])
    links.new(separate_hsv_node.outputs[0], combine_node.inputs[0])

    # Подключаем все нормальные карты
    links.new(normal_node.outputs['Normal'], fresnel_node.inputs['Normal'])
    links.new(normal_node.outputs['Normal'], refraction_node.inputs['Normal'])
    links.new(normal_node.outputs['Normal'], glossy_node.inputs['Normal'])

    # Подключаем все карты шероховатостей
    links.new(separate_node.outputs['Red'], refraction_node.inputs['Roughness'])
    links.new(separate_node.outputs['Red'], glossy_node.inputs['Roughness'])

    # Устанавливаем обработанный цвет для преломления
    links.new(combine_node.outputs['Color'], refraction_node.inputs['Color'])

    # Соединяем все шейдеры в миксере для реалистичного льда
    links.new(fresnel_node.outputs['Factor'], mix_node.inputs[0]) # Первый вход
    links.new(refraction_node.outputs['BSDF'], mix_node.inputs[1]) # Второй вход
    links.new(glossy_node.outputs['BSDF'], mix_node.inputs[2]) # Третий вход
    
    # Mix -> Output
    links.new(mix_node.outputs['Shader'], output_node.inputs['Surface'])

    print(f"Материал {mat.name} успешно обновлён!")

# Подповерхностное рассеивание в плотных блоках (слабое SSS)
def setup_sss_dense(mat):
  
    tree = mat.node_tree
    nodes = tree.nodes
    links = tree.links
    
    # 1. Проверка: не настроен ли он уже?
    # Если в нодах уже есть фрейм с названием "Auto_SSS_Dense", выходим
    if "Auto_SSS_Dense" in nodes:
        print(f"Материал {mat.name} уже настроен.")
        return

    # 2. Ищем ключевые узлы (Якоря)
    # Нам нужно найти Principled BSDF и Output
    principled = next((n for n in nodes if n.type == 'BSDF_PRINCIPLED'), None)
    output_node = next((n for n in nodes if n.type == 'OUTPUT_MATERIAL'), None)
    
    if not principled or not output_node:
        print(f"В материале {mat.name} нет Principled BSDF или Output!")
        return

    # 3. Ищем текстуру цвета (Albedo)
    # Ищем, что подключено во вход 'Base Color' у Principled BSDF
    base_color_socket = principled.inputs['Base Color']
    image_node = None
    
    if base_color_socket.is_linked:
        # Берём узел, от которого идёт связь
        image_node = base_color_socket.links[0].from_node
        # Проверяем, точно ли это картинка
        if image_node.type != 'TEX_IMAGE':
            print(f"В {mat.name} к цвету подключена не картинка, а {image_node.type}")
            # Можно прервать или продолжить, но лучше прервать пока
            # return 
    else:
        print(f"В {mat.name} нет текстуры, подключенной к Base Color")
        return

    # 4. Донастраиваем PrincipledBSDF
    principled.subsurface_method = 'BURLEY'
    principled.inputs[8].default_value = 1.0
    principled.inputs[10].default_value = 1.0

    # ==========================================
    # 5. СОЗДАНИЕ НОВЫХ НОД (как на скриншоте)
    # ==========================================
    
    # Создаем Фрейм
    frame = nodes.new('NodeFrame')
    frame.name = "Auto_SSS_Dense"
    frame.label = "Auto SSS Dense"
    
    # Gamma (чтобы линейную картинку получить)
    gamma_node = nodes.new('ShaderNodeGamma')
    gamma_node.inputs['Gamma'].default_value = 0.4545
    gamma_node.parent = frame
    gamma_node.location = (principled.location.x, principled.location.y - 500)
    
    # Hue/Saturation (для насыщенности SSS)
    hsv_node = nodes.new('ShaderNodeHueSaturation')
    hsv_node.inputs['Saturation'].default_value = 3.0
    hsv_node.inputs['Value'].default_value = 0.8
    hsv_node.parent = frame
    hsv_node.location = (principled.location.x + 200, principled.location.y - 500)

    # ==========================================
    # 6. СОЕДИНЕНИЕ НОД (Линковка)
    # ==========================================

    # Текстура -> Gamma
    links.new(image_node.outputs['Color'], gamma_node.inputs['Color'])

    # Gamma -> HSV
    links.new(gamma_node.outputs['Color'], hsv_node.inputs['Color'])

    # HSV -> Subsurface Radius
    links.new(hsv_node.outputs['Color'], principled.inputs[9])

    print(f"Материал {mat.name} успешно обновлён!")

# Подповерхностное рассеивание в легкопроницаемых блоках (сильное SSS)
def setup_sss_sparse(mat):
  
    tree = mat.node_tree
    nodes = tree.nodes
    links = tree.links
    
    # 1. Проверка: не настроен ли он уже?
    # Если в нодах уже есть фрейм с названием "Auto_SSS_Sparse", выходим
    if "Auto_SSS_Sparse" in nodes:
        print(f"Материал {mat.name} уже настроен.")
        return

    # 2. Ищем ключевые узлы (Якоря)
    # Нам нужно найти Principled BSDF и Output
    principled = next((n for n in nodes if n.type == 'BSDF_PRINCIPLED'), None)
    output_node = next((n for n in nodes if n.type == 'OUTPUT_MATERIAL'), None)
    
    if not principled or not output_node:
        print(f"В материале {mat.name} нет Principled BSDF или Output!")
        return

    # 3. Ищем текстуру цвета (Albedo)
    # Ищем, что подключено во вход 'Base Color' у Principled BSDF
    base_color_socket = principled.inputs['Base Color']
    image_node = None
    
    if base_color_socket.is_linked:
        # Берём узел, от которого идёт связь
        image_node = base_color_socket.links[0].from_node
        # Проверяем, точно ли это картинка
        if image_node.type != 'TEX_IMAGE':
            print(f"В {mat.name} к цвету подключена не картинка, а {image_node.type}")
            # Можно прервать или продолжить, но лучше прервать пока
            # return 
    else:
        print(f"В {mat.name} нет текстуры, подключенной к Base Color")
        return

    # 4. Донастраиваем PrincipledBSDF
    principled.subsurface_method = 'BURLEY'
    principled.inputs[8].default_value = 1.0
    principled.inputs[10].default_value = 1.0

    # ==========================================
    # 5. СОЗДАНИЕ НОВЫХ НОД (как на скриншоте)
    # ==========================================
    
    # Создаем Фрейм
    frame = nodes.new('NodeFrame')
    frame.name = "Auto_SSS_Sparse"
    frame.label = "Auto SSS Sparse"
    
    # Gamma (чтобы линейную картинку получить)
    gamma_node = nodes.new('ShaderNodeGamma')
    gamma_node.inputs['Gamma'].default_value = 0.4545
    gamma_node.parent = frame
    gamma_node.location = (principled.location.x, principled.location.y - 500)
    
    # Hue/Saturation (для насыщенности SSS)
    hsv_node = nodes.new('ShaderNodeHueSaturation')
    hsv_node.inputs['Saturation'].default_value = 3.0
    hsv_node.inputs['Value'].default_value = 2.0
    hsv_node.parent = frame
    hsv_node.location = (principled.location.x + 200, principled.location.y - 500)

    # ==========================================
    # 6. СОЕДИНЕНИЕ НОД (Линковка)
    # ==========================================

    # Текстура -> Gamma
    links.new(image_node.outputs['Color'], gamma_node.inputs['Color'])

    # Gamma -> HSV
    links.new(gamma_node.outputs['Color'], hsv_node.inputs['Color'])

    # HSV -> Subsurface Radius
    links.new(hsv_node.outputs['Color'], principled.inputs[9])

    print(f"Материал {mat.name} успешно обновлён!")

# Золото
# def setup_gold(mat):
#    # Получаем доступ к нодам
#     nodes = mat.node_tree.nodes
#     
#     # Ищем Principled BSDF
#     principled = next((n for n in nodes if n.type == 'BSDF_PRINCIPLED'), None)
#     
#     if principled:
#         try:
#             # Устанавливаем шероховатость поменьше
#             principled.inputs['Roughness'].default_value = 0.1
#             print(f"[Шероховатость] {mat.name}: Шероховатость установлена на 0.1")
#         except KeyError:
#             print(f"[Ошибка] У материала {mat.name} нет слота 'Roughness'")

# Запуск донастройки материалов
def auto_configure_materials():
    print("--- Запуск конфигуратора материалов ---")
    
    for mat in bpy.data.materials:
        if not mat.use_nodes:
            continue
            
        # ТРЮК: Очистка имени от мусора Blender
        # Blender любит делать имена типа "oak_leaves.001", "torch.002"
        # Мы отрезаем всё, что после точки, чтобы сравнивать чистое имя.
        clean_name = mat.name.split('.')[0]
        
        # Точное сравнение с базами данных                     
        if clean_name in LIST_EMISSION_STRONG:
            setup_emission_strong(mat)
            
        if clean_name in LIST_TRANSLUCENCY:
            setup_translucency(mat)
            
        if clean_name in LIST_WATER:
            setup_water(mat)
            
        if clean_name in LIST_STAINED_GLASS:
            setup_stained_glass(mat)

        if clean_name in LIST_STAINED_GLASS_PANE_TOP:
            setup_stained_glass_pane_top(mat)

        if clean_name in LIST_ACHROMATIC_GLASS:
            setup_achromatic_glass(mat)

        if clean_name in LIST_ACHROMATIC_GLASS_PANE_TOP:
            setup_achromatic_glass_pane_top(mat)

        if clean_name in LIST_GLASS:
            setup_glass(mat)

        if clean_name in LIST_GLASS_PANE_TOP:
            setup_glass_pane_top(mat)

        if clean_name in LIST_ICE:
            setup_ice(mat)

        if clean_name in LIST_SSS_DENSE:
            setup_sss_dense(mat)

        if clean_name in LIST_SSS_SPARSE:
            setup_sss_sparse(mat)

        # if clean_name in LIST_GOLD:
        #     setup_gold(mat)

# Изменение шейдинга на «плоский»
def set_flat_shading_for_all():
    print("Применяю Flat Shading ко всей геометрии...")
    
    # 1. Снимаем выделение со всего
    bpy.ops.object.select_all(action='DESELECT')
    
    found_mesh = False
    
    # 2. Проходимся по всем объектам в текущей сцене
    for obj in bpy.context.scene.objects:
        if obj.type == 'MESH':
            # Выделяем объект
            obj.select_set(True)
            # Делаем его активным (нужно для работы bpy.ops)
            bpy.context.view_layer.objects.active = obj
            found_mesh = True
            
    # 3. Если нашли хоть один меш, применяем Shade Flat сразу ко всем выделенным
    if found_mesh:
        bpy.ops.object.shade_flat()
        print("Готово: Все блоки стали плоскими.")
    else:
        print("В сцене нет мешей!")

    # 4. (Опционально) Снимаем выделение, чтобы сцена была чистой
    bpy.ops.object.select_all(action='DESELECT')

# Всякая каустика

# Включение приёма каустики для всех материалов
def enable_receive_caustics_for_all():
    print("--- Включаю получение каустики (Receive) для всей геометрии ---")
    count = 0
    
    # Проходим по всем объектам в текущей сцене
    for obj in bpy.context.scene.objects:
        # Нас интересуют только меши (у ламп и камер нет этого свойства)
        if obj.type == 'MESH':
            obj.cycles.is_caustics_receiver = True
            count += 1
            
    print(f"Готово: Получение каустики включено для {count} объектов.")

# Отбрасывание каустики для преломляющих объектов
def enable_caustics_caster_for_refractive():
    print("--- Включаю отбрасывание каустики (Cast) для преломляющих объектов ---")
    
    # 1. Объединяем все нужные списки в одно общее множество
    # Оператор | работает как "объединение" для множеств (sets)
    # Если твои списки это list [], то используй set(LIST_WATER) | set(LIST_GLASS)...
    # Но так как мы договаривались использовать {}, то | сработает сразу.
    refractive_names = (
        LIST_WATER |
        LIST_STAINED_GLASS |
        LIST_STAINED_GLASS_PANE_TOP |
        LIST_ACHROMATIC_GLASS |
        LIST_ACHROMATIC_GLASS_PANE_TOP |
        LIST_GLASS |
        LIST_GLASS_PANE_TOP |
        LIST_ICE
    )

    count = 0

    # 2. Проходим по всем объектам сцены
    for obj in bpy.context.scene.objects:
        # Нас интересуют только меши
        if obj.type != 'MESH':
            continue
            
        # Очищаем имя от суффиксов Blender (.001, .002)
        clean_name = obj.name.split('.')[0]
        
        # 3. Проверка: есть ли имя в нашем объединенном списке?
        if clean_name in refractive_names:
            # Включаем галочку "Cast Shadow Caustics"
            obj.cycles.is_caustics_caster = True
            # ВЫКЛЮЧАЕМ галочку "Receive Shadow Caustics" (иначе чернота появляется)
            obj.cycles.is_caustics_receiver = False
            count += 1

    print(f"Готово: Отбрасывание каустики включено для {count} объектов.")

# ==========================================
# ЗАПУСК ВСЕГО
# ==========================================

# 0. Откатываем всю автоматизацию
undo_nodes_automation()

# 1. Настраиваем интерполяцию
set_closest_interpolation()

# 2. Донастраиваем материалы
auto_configure_materials()

# 3. Делаем всё плоским
set_flat_shading_for_all()

# 4. Включаем для всех объектов приём каустики
enable_receive_caustics_for_all()

# 5. Включаем для преломляющих объектов отбрасывание каустики
enable_caustics_caster_for_refractive()

print("Автоматизация завершена! Можно рендерить.")