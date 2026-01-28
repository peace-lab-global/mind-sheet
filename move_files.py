import os
import shutil

# 定义源目录和目标目录映射
source_dir = "tables"
destination_mappings = {
    "Addiction_": "addiction",
    "Anxiety_": "anxiety",
    "Bipolar_": "bipolar",
    "Bach_Music_Therapy": "music-therapy",
    "Beethoven_Music_Therapy": "music-therapy",
    "Brahms_Music_Therapy": "music-therapy",
    "Chopin_Music_Therapy": "music-therapy",
    "Debussy_Music_Therapy": "music-therapy",
    "Faure_Music_Therapy": "music-therapy",
    "Handel_Music_Therapy": "music-therapy",
    "Mahler_Music_Therapy": "music-therapy",
    "Bio_": "bio",
    "Brain_": "brain",
    "Buddhism_": "buddhism",
    "CFS_": "cfs",
    "Chronic_Stress_": "chronic-stress",
    "Classical_Music_": "classical-music",
    "Coffee_": "coffee",
    "Dao_": "dao",
    "Death_": "death",
    "Depression_": "depression",
    "Emotion_": "emotion",
    "Family_Constellation_": "family-constellation",
    "Flow_": "flow",
    "Framework_": "framework",
    "GAD_": "gad",
    "Grief_": "grief",
    "HPA_Axis_": "hpa-axis",
    "Incense_": "incense",
    "Loneliness_": "loneliness",
    "Love_": "love",
    "Mandala_Meditation_": "mandala-meditation",
    "Marriage_": "marriage",
    "Media_": "media",
    "Meditation_": "meditation",
    "Mindfulness_": "mindfulness",
    "Morita_Therapy": "morita-therapy",
    "Mozart_Music_Therapy": "music-therapy",
    "Nutritional_": "nutritional",
    "Opera_ArtSong_Therapy": "opera-artsong-therapy",
    "Philosophy_": "philosophy",
    "Phobia_": "phobia",
    "Psychological_": "psychological",
    "Psychology_": "psychology",
    "Adolescent_Crisis_Intervention": "adolescent-crisis",
    "Anime_Manga_Therapy": "anime-manga-therapy",
    "Autism_Spectrum_Disorder": "autism",
    "Cinema_Therapy": "cinema-therapy",
    "Compassion_Focused_Therapy": "compassion-focused-therapy",
    "Containment_Techniques": "containment-techniques",
    "Cortisol_": "cortisol",
    "Crisis_Assessment_Tools": "crisis-assessment",
    "Crisis_Postvention": "crisis-postvention",
    "Daily_Advanced_Practices": "daily-practices",
    "Daily_Routine_Protocols": "daily-routines",
    "Dialectical_Behavior_Therapy": "dialectical-behavior-therapy",
    "Dzogchen_Great_Perfection": "dzogchen",
    "Folk_Music_Therapy": "folk-music-therapy",
    "Forest_Therapy_Tree_Hugging": "forest-therapy",
    "Game_Therapy": "game-therapy",
    "Grounding_Techniques": "grounding-techniques",
    "Guqin_Therapy": "guqin-therapy",
    "Herbal_Tea_Comprehensive": "herbal-tea",
    "Krishnamurti_Teachings": "krishnamurti",
    "Legalist_Management_Psychology": "legalist-management",
    "Mindful_Daily_Living": "mindful-daily-living",
    "Nan_Huaijin_Teachings": "nan-huaijin",
    "Rachmaninoff_Music_Therapy": "music-therapy",
    "Sacred_Music_Therapy": "music-therapy",
    "Satie_Music_Therapy": "music-therapy",
    "Schubert_Music_Therapy": "music-therapy",
    "Tchaikovsky_Music_Therapy": "music-therapy",
    "Vivaldi_Music_Therapy": "music-therapy",
    "Relaxation_": "relaxation",
    "Sleep_": "sleep",
    "Sensory_": "sensory",
    "Somatic_": "somatic",
    "Stretch_": "stretch",
    "Suicide_Intervention": "suicide-intervention",
    "Television_Therapy": "television-therapy",
    "Tea_": "tea",
    "Six_Yogas_Naropa": "six-yogas-naropa",
    "Satir_": "satir-model",
    "Self_Compassion_Self_Care": "self-compassion",
    "Self_Soothing_Techniques": "self-soothing",
    "Society_Community_Support": "society-community",
    "Syncretism_Three_Teachings": "syncretism",
    "TED_Talks_Healing_Resources": "ted-talks",
    "Therapy_Direct_Recognition_Healing": "therapy-direct-recognition",
    "Theravada_": "theravada",
    "Tibetan_": "tibetan-buddhism",
    "Transcendental_Meditation": "transcendental-meditation",
    "Vajrayana_": "vajrayana",
    "Vasana_": "vasana",
    "Vipassana_Meditation": "vipassana",
    "Wisdom_": "wisdom-traditions",
    "Workplace_Psychological_Crisis_Intervention": "workplace-psychological-crisis",
    "Yoga_": "yoga",
    "Zen_": "zen",
    "Mahamudra_Detailed": "mahamudra",
    "Resources_": "resources"
}

# 移动19th-century目录下的文件
nineteenth_century_path = os.path.join(source_dir, "19th-century")
if os.path.exists(nineteenth_century_path):
    for root, dirs, files in os.walk(nineteenth_century_path):
        for file in files:
            source_file = os.path.join(root, file)
            # 计算相对路径
            rel_path = os.path.relpath(source_file, source_dir)
            # 目标路径
            dest_file = os.path.join("philosophy", rel_path)
            # 确保目标目录存在
            dest_dir = os.path.dirname(dest_file)
            if dest_dir and not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            # 移动文件
            print(f"Moving {source_file} to {dest_file}")
            shutil.move(source_file, dest_file)

# 移动ancient目录下的文件
ancient_path = os.path.join(source_dir, "ancient")
if os.path.exists(ancient_path):
    for root, dirs, files in os.walk(ancient_path):
        for file in files:
            source_file = os.path.join(root, file)
            # 计算相对路径
            rel_path = os.path.relpath(source_file, source_dir)
            # 目标路径
            dest_file = os.path.join("philosophy", rel_path)
            # 确保目标目录存在
            dest_dir = os.path.dirname(dest_file)
            if dest_dir and not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            # 移动文件
            print(f"Moving {source_file} to {dest_file}")
            shutil.move(source_file, dest_file)

# 移动early-modern目录下的文件
early_modern_path = os.path.join(source_dir, "early-modern")
if os.path.exists(early_modern_path):
    for root, dirs, files in os.walk(early_modern_path):
        for file in files:
            source_file = os.path.join(root, file)
            # 计算相对路径
            rel_path = os.path.relpath(source_file, source_dir)
            # 目标路径
            dest_file = os.path.join("philosophy", rel_path)
            # 确保目标目录存在
            dest_dir = os.path.dirname(dest_file)
            if dest_dir and not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            # 移动文件
            print(f"Moving {source_file} to {dest_file}")
            shutil.move(source_file, dest_file)

# 移动enlightenment目录下的文件
enlightenment_path = os.path.join(source_dir, "enlightenment")
if os.path.exists(enlightenment_path):
    for root, dirs, files in os.walk(enlightenment_path):
        for file in files:
            source_file = os.path.join(root, file)
            # 计算相对路径
            rel_path = os.path.relpath(source_file, source_dir)
            # 目标路径
            dest_file = os.path.join("philosophy", rel_path)
            # 确保目标目录存在
            dest_dir = os.path.dirname(dest_file)
            if dest_dir and not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            # 移动文件
            print(f"Moving {source_file} to {dest_file}")
            shutil.move(source_file, dest_file)

# 移动german-idealism目录下的文件
german_idealism_path = os.path.join(source_dir, "german-idealism")
if os.path.exists(german_idealism_path):
    for root, dirs, files in os.walk(german_idealism_path):
        for file in files:
            source_file = os.path.join(root, file)
            # 计算相对路径
            rel_path = os.path.relpath(source_file, source_dir)
            # 目标路径
            dest_file = os.path.join("philosophy", rel_path)
            # 确保目标目录存在
            dest_dir = os.path.dirname(dest_file)
            if dest_dir and not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            # 移动文件
            print(f"Moving {source_file} to {dest_file}")
            shutil.move(source_file, dest_file)

# 移动其他文件
for filename in os.listdir(source_dir):
    if os.path.isfile(os.path.join(source_dir, filename)):
        # 找到对应的目标目录
        dest_dir = None
        for prefix, dir_name in destination_mappings.items():
            if filename.startswith(prefix):
                dest_dir = dir_name
                break
        
        if dest_dir:
            # 确保目标目录存在
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            # 移动文件
            source_file = os.path.join(source_dir, filename)
            dest_file = os.path.join(dest_dir, filename)
            print(f"Moving {source_file} to {dest_file}")
            shutil.move(source_file, dest_file)
        else:
            print(f"No destination found for {filename}")

# 删除空的目录
import os
for root, dirs, files in os.walk(source_dir, topdown=False):
    for dir_name in dirs:
        dir_path = os.path.join(root, dir_name)
        try:
            os.rmdir(dir_path)  # 尝试删除空目录
            print(f"Removed empty directory: {dir_path}")
        except OSError:
            pass  # 如果目录不为空，则跳过

print("File moving and cleanup completed!")
