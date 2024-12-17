
import streamlit as st
import os

from datetime import datetime
import tempfile
import os

import sys

import json
import re
import csv

import zipfile

from streamlit_module import moz_tab9 as t9
from streamlit_module import moz_tab7 as t7

from datetime import datetime
import signal
import pandas as pd
import streamlit.components.v1 as components
import markdown2

from streamlit_module import moz_replace as rp
def expire():
    data_folder = "/content/my_app"

    expiration_date = datetime(2025, 6, 31)  # 期限日を設定
    pathname=os.path.join(data_folder,'settings2.json')
    if datetime.now() > expiration_date:
        if not os.path.exists(pathname):
            with open(pathname,'w',encoding='utf-8')as f:
                f.write("keywords")
        print("このプログラムの有効期限は2025年1月31日です。有効期限が切れました。")
        raise Exception("このプログラムの有効期限が切れました。")

    if os.path.exists(pathname):

        print("このプログラムの有効期限は2025年1月31日です。有効期限が切れました。")
        raise Exception("このプログラムの有効期限が切れました。")


def initialize_load(arg):
    try:
        with open(st.session_state.setpath, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
            result=data.get(arg)
            #print(f"arg:{arg}")
            #print(f"result:{result}")
            #st.session_state.model_option_key=data.get("model_option")
        return result
    except (FileNotFoundError, json.JSONDecodeError):
        return True

def initialize_load_rp(arg="replacements_file"):
    try:
        with open(st.session_state.setpath, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
            result=data.get(arg)
            #st.session_state.model_option_key=data.get("model_option")
        return result
    except (FileNotFoundError, json.JSONDecodeError):
        return "replacements.csv"

def initialize_load_dot(arg="dot_management_file"):
    try:
        with open(st.session_state.setpath, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
            result=data.get(arg)
            #print(f"loaded_dot_filename:{result}")
        return result
    except (FileNotFoundError, json.JSONDecodeError):
        return "dot_manager.csv"
    
def get_base_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))
    
def load_model_option():
    try:
        with open(st.session_state.setpath, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
            st.session_state.model_option_func=data.get("model_option")
            #st.session_state.model_option_key=data.get("model_option")
        return st.session_state.model_option_func
    except (FileNotFoundError, json.JSONDecodeError):
        return True

def load_language_key():
    try:
        with open(st.session_state.setpath, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
            st.session_state.language_key=data.get("language_result")
            st.session_state.language_result=st.session_state.language_key
        return st.session_state.language_key
    except (FileNotFoundError, json.JSONDecodeError):
        return True
def load_model_option2():
    try:
        with open(st.session_state.setpath, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
            st.session_state.model_option_func=data.get("model_option2")
            #st.session_state.model_option_key=data.get("model_option")
            return st.session_state.model_option_func
    except (FileNotFoundError, json.JSONDecodeError):
        return True
    
def load_model_option3():
    try:
        with open(st.session_state.setpath, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
            st.session_state.model_option_func=data.get("model_option3")
            #st.session_state.model_option_key=data.get("model_option")
            return st.session_state.model_option_func
    except (FileNotFoundError, json.JSONDecodeError):
        return True        
    
def load_model_option_key():
    try:
        with open(st.session_state.setpath, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
            st.session_state.model_option_key=data.get("model_option")
            #return st.session_state.model_option_func
            return st.session_state.model_option_key
    except (FileNotFoundError, json.JSONDecodeError):
        return True
def load_model_option_key2():
    try:
        with open(st.session_state.setpath, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
            st.session_state.model_option_key2=data.get("model_option2")
            #return st.session_state.model_option_func
            return st.session_state.model_option_key2
    except (FileNotFoundError, json.JSONDecodeError):
        return True
    

def load_model_option_key3():
    try:
        with open(st.session_state.setpath, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
            st.session_state.model_option_key3=data.get("model_option3")
            #return st.session_state.model_option_func
            return st.session_state.model_option_key3
    except (FileNotFoundError, json.JSONDecodeError):
        return True


def load_deepall():
    try:
        with open(st.session_state.setpath, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
            st.session_state.deepall=data.get("deepall")
            #st.session_state.model_option_key=data.get("deepall")
            return st.session_state.deepall
    except (FileNotFoundError, json.JSONDecodeError):
        return True     

def load_deepall_key():
    try:
        with open(st.session_state.setpath, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
            st.session_state.deepall_key=data.get("deepall")
            #return st.session_state.model_option_func
            return st.session_state.deepall_key
    except (FileNotFoundError, json.JSONDecodeError):
        return True
    
def load_selected_file(): #★ load
    try:
        with open(st.session_state.setpath, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
            st.session_state.select_rp_note=data.get("replacements_file")
            #st.session_state.rp_key=data.get("replacements_file")
            return st.session_state.select_rp_note
    except (FileNotFoundError, json.JSONDecodeError):
        return "replacements.csv"

def load_selected_file_key(): #★ load
    try:
        with open(st.session_state.setpath, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
            #st.session_state.select_rp_note=data.get("replacements_file")
            st.session_state.rp_key=data.get("replacements_file")
            return st.session_state.rp_key
    except (FileNotFoundError, json.JSONDecodeError):
        return "replacements.csv"
    


def load_selected_dot_file_key():
    try:
        with open(st.session_state.setpath, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
            #st.session_state.select_dot_note=data.get("dot_management_file")
            st.session_state.dot_key=data.get("dot_management_file")
            return st.session_state.dot_key
    except (FileNotFoundError, json.JSONDecodeError):
        return "dot_manager.csv"    
    
def load_toggle_choice():
    try:
        with open(st.session_state.setpath,'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
            st.session_state.toggle_replacements=data.get("replace_words")
            return st.session_state.toggle_replacements
    except(FileNotFoundError, json.JSONDecodeError):
        return False
    
def load_toggle_choice_key():
    try:
        with open(st.session_state.setpath,'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
            st.session_state.toggle_key=data.get("replace_words")
            return st.session_state.toggle_key

    except(FileNotFoundError, json.JSONDecodeError):
        return False

def load_ja_split():
    try:
        with open(st.session_state.setpath,'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
            st.session_state.ja_split=data.get("ja_split")
            return st.session_state.ja_split
    except(FileNotFoundError, json.JSONDecodeError):
        return False
    
def load_ja_split_key():
    try:
        with open(st.session_state.setpath,'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
            st.session_state.ja_split_key=data.get("ja_split")
            return st.session_state.ja_split_key

    except(FileNotFoundError, json.JSONDecodeError):
        return False
def load_comma_split():
    try:
        with open(st.session_state.setpath,'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
            st.session_state.comma_split=data.get("comma_split")
            return st.session_state.comma_split
    except(FileNotFoundError, json.JSONDecodeError):
        return False
    
def load_comma_split_key():
    try:
        with open(st.session_state.setpath,'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
            st.session_state.comma_split_key=data.get("comma_split")
            return st.session_state.comma_split_key
    except(FileNotFoundError, json.JSONDecodeError):
        return False
    
def load_min_split():
    try:
        with open(st.session_state.setpath,'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
            st.session_state.min_split=data.get("min_split")
            return st.session_state.min_split
    except(FileNotFoundError, json.JSONDecodeError):
        return False

def load_max_split():
    try:
        with open(st.session_state.setpath,'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
            st.session_state.max_split=data.get("max_split")
            return st.session_state.max_split
    except(FileNotFoundError, json.JSONDecodeError):
        return False
        
def load_multi():
    
    
    #load_toggle_choice()
    #load_ja_split()
    #load_comma_split()
    #load_min_split()
    #load_max_split()
    load_language_key()
    load_selected_file_key()
    load_selected_dot_file_key()
    load_model_option_key()
    load_model_option_key2()
    load_model_option_key3()
    load_deepall_key()
    expire()

def save_language_key(): #☆save
    try:
        with open(st.session_state.setpath, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
        
        
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}  # ファイルが存在しない場合、空の辞書を使用
    
    data["language_result"] = st.session_state.language_key
    
    with open(st.session_state.setpath, 'w',encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def save_model_option(): #☆save
    try:
        with open(st.session_state.setpath, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}  # ファイルが存在しない場合、空の辞書を使用
    
    data["model_option"] = st.session_state.model_option_key
    
    with open(st.session_state.setpath, 'w',encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def save_model_option2(): #☆save
    try:
        with open(st.session_state.setpath, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}  # ファイルが存在しない場合、空の辞書を使用
    
    data["model_option2"] = st.session_state.model_option_key2
    
    with open(st.session_state.setpath, 'w',encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def save_model_option3(): #☆save
    try:
        with open(st.session_state.setpath, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}  # ファイルが存在しない場合、空の辞書を使用
    
    data["model_option3"] = st.session_state.model_option_key3
    
    with open(st.session_state.setpath, 'w',encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
def save_deepall(): #☆save
    try:
        with open(st.session_state.setpath, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}  # ファイルが存在しない場合、空の辞書を使用
    
    data["deepall"] = st.session_state.deepall_key
    
    with open(st.session_state.setpath, 'w',encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def save_dot_filename():
    try:
        with open(st.session_state.setpath, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}  # ファイルが存在しない場合、空の辞書を使用
    #print(f"select_dot_result:{st.session_state.dot_key}","saved!")
    data["dot_management_file"] = st.session_state.dot_key#★★
    
    with open(st.session_state.setpath, 'w',encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def save_rp_filename():
    try:
        with open(st.session_state.setpath, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}  # ファイルが存在しない場合、空の辞書を使用
    #print(f"select_dot_result:{st.session_state.rp_key}","saved!")
    data["replacements_file"] = st.session_state.rp_key#★★
    
    with open(st.session_state.setpath, 'w',encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def save_selected_file(df):
    if st.session_state.rp_key != st.session_state.dammy_rp_key:
    
        try:
            with open(st.session_state.setpath, 'r',encoding='utf-8') as json_file:
                data = json.load(json_file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}  # ファイルが存在しない場合、空の辞書を使用
        
        st.session_state.state_manager=rp.StateManager()
        st.session_state.state_manager.save_state(df)
        data["replacements_file"] = st.session_state.rp_key
        
        with open(st.session_state.setpath, 'w',encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        
        st.session_state.dammy_rp_key=st.session_state.rp_key

def save_dot_selected_file(dot_df):
    #print(st.session_state.dot_key)
    #print(st.session_state.dammy_dot_key)
    if st.session_state.dot_key != st.session_state.dammy_dot_key:
        
        try:
            with open(st.session_state.setpath, 'r',encoding='utf-8') as json_file:
                data = json.load(json_file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}  # ファイルが存在しない場合、空の辞書を使用
    
        st.session_state.dot_state_manager = rp.StateManager()
        st.session_state.dot_state_manager.save_state(dot_df)
        data["dot_management_file"] = st.session_state.dot_key
        

        with open(st.session_state.setpath, 'w',encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)    
        st.session_state.dammy_dot_key=st.session_state.dot_key

def save_toggle_choice():
    try:
        with open(st.session_state.setpath, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}  # ファイルが存在しない場合、空の辞書を使用
    
    data["replace_words"] = st.session_state.toggle_key

    with open(st.session_state.setpath, 'w',encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)




def onchange_toggle():
    save_toggle_choice()
    load_multi()

#uploadファイル(複数時）の表示を助ける関数
def save_ja_choice():
    try:
        with open(st.session_state.setpath, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}  # ファイルが存在しない場合、空の辞書を使用
    
    data["ja_split"] = st.session_state.ja_split_key

    with open(st.session_state.setpath, 'w',encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)  

def save_comma_choice():
    try:
        with open(st.session_state.setpath, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}  # ファイルが存在しない場合、空の辞書を使用
    
    data["comma_split"] = st.session_state.comma_split_key

    with open(st.session_state.setpath, 'w',encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)  

def save_minmax():
    try:
        with open(st.session_state.setpath, 'r',encoding='utf-8') as json_file:
            data = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}  # ファイルが存在しない場合、空の辞書を使用
    
    data["min_split"] = st.session_state.min_split_current
    data["max_split"] = st.session_state.max_split_current

    with open(st.session_state.setpath, 'w',encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)  
    

def onchange_ja_split():
    save_ja_choice()
    load_multi()

def onchange_comma_split():
    save_comma_choice()
    load_multi()


def upstock(st_files, st_namelist, upfiles, dir):
    # リスト型であることを確認する
    if not isinstance(st_files, list):
        st_files = []
    if not isinstance(st_namelist, list):
        st_namelist = []

    for file in upfiles:
        if file.name in st_namelist:
            continue
        new_path = os.path.join(dir, f'{file.name}')
        with open(new_path, 'wb') as f:
            f.write(file.getbuffer())
        st_files.append(new_path)
        st_namelist.append(os.path.basename(new_path))

    return st_files, st_namelist

def kanji_to_number(kanji):
    kanji_to_num = {
        "一": 1, "二": 2, "三": 3, "四": 4, "五": 5,
        "六": 6, "七": 7, "八": 8, "九": 9, "〇": 0, "零": 0
    }
    unit_to_num = {
        "十": 10, "百": 100, "千": 1000
    }
    result = 0
    temp = 0  # 一時値保持
    for char in kanji:
        if char in kanji_to_num:
            temp = kanji_to_num[char]
        elif char in unit_to_num:
            temp = temp or 1  # 「十」のような場合
            result += temp * unit_to_num[char]
            temp = 0
        else:
            raise ValueError(f"無効な文字: {char}")
    result += temp
    return result

# 複数のパターンで置換処理を実行
def kanji_henkan(text):
    # 2つの正規表現パターン
    patterns = [
        re.compile(r"\b[一二三四五六七八九〇零十百千]+\b"),
        
    ]
    
    # 置換処理の関数
    def replace_kanji(match):
        kanji = match.group()
        try:
            return str(kanji_to_number(kanji))
        except ValueError:
            return kanji  # 変換失敗時はそのまま返す
    
    # 各パターンで検索・置換を実行
    for pattern in patterns:
        text = pattern.sub(replace_kanji, text)
    
    return text









def unify_timestamps_vtt(text):
    pattern_1_digit = re.compile(r'(\d{2}:\d{2}:\d{2}\.\d)(?!\d)')
    pattern_2_digits = re.compile(r'(\d{2}:\d{2}:\d{2}\.\d{2})(?!\d)')
    text = pattern_1_digit.sub(lambda x: x.group(1) + '00', text)
    text = pattern_2_digits.sub(lambda x: x.group(1) + '0', text)
    return text

def unify_timestamps_srt(text):
    pattern_1_digit = re.compile(r'(\d{2}:\d{2}:\d{2}),(\d)(?!\d)')
    pattern_2_digits = re.compile(r'(\d{2}:\d{2}:\d{2}),(\d{2})(?!\d)')
    text = pattern_1_digit.sub(lambda x: f"{x.group(1)},{x.group(2)}00", text)
    text = pattern_2_digits.sub(lambda x: f"{x.group(1)},{x.group(2)}0", text)
    return text

# ファイルを処理して一時保存し、そのパスを返す関数
def process_subtitle(file_paths):
    output_files=[]
    for indi_file in file_paths:
        if indi_file.endswith(".srt"):
            file_type="srt"
        else:
            file_type="vtt"
                            
        with open(indi_file, 'r', encoding='utf-8') as file:
            file_content = file.read()

        # タイムスタンプのペアを検出して処理
        timestamp_pattern = r'\d{1,2}:\d{2}:\d{2}[\.,]\d{1,3} --> \d{1,2}:\d{2}:\d{2}[\.,]\d{1,3}'
        segments = re.split(f'({timestamp_pattern})', file_content.strip())
        
        result = []
        id_counter = 1

        # 正常なタイムスタンプとテキストを交互に処理
        for i in range(1, len(segments), 2):
            timestamp = segments[i].strip()
            text = segments[i+1].strip()

            # タイムスタンプのフォーマットを統一
            if file_type == 'srt':
                timestamp = unify_timestamps_srt(timestamp)
            elif file_type == 'vtt':
                timestamp = unify_timestamps_vtt(timestamp)

            # 正しいIDとタイムスタンプ、テキストを追加
            result.append(f"{id_counter}\n{timestamp}\n{text}\n\n")
            id_counter += 1

    # VTTの場合、WEBVTTを追加
        if file_type == 'vtt':
            final_content= 'WEBVTT\n\n' + ''.join(result)
        else:
            final_content=''.join(result)
    

        # 処理結果を一時ファイルに保存
    
        timestamp_patch = datetime.now().strftime("%Y%m%d%H%M%S")
        temp_dir = os.path.join(tempfile.gettempdir(), f"tempdir_{timestamp_patch}")
        os.makedirs(temp_dir, exist_ok=True)

        ot_path=os.path.join(temp_dir,os.path.basename(indi_file))

        with open(ot_path, 'w', encoding='utf-8') as file:
            file.write(final_content)  
        
        output_files.append(ot_path)

    return output_files     


def convert_timestamps(content: str, input_ext: str, output_ext: str) -> str:
    # SRT to VTT
    if input_ext == ".srt" and output_ext == ".vtt":
        content = re.sub(r"(\d+:\d{2}:\d{2}),(\d{3})", r"\1.\2", content)
        content ="WEBVTT\n\n"+content
    # VTT to SRT
    elif input_ext == ".vtt" and output_ext == ".srt":
        content = re.sub(r"(\d+:\d{2}:\d{2})\.(\d{3})", r"\1,\2", content)
    return content

def convert_files(input_paths: list) -> list:
    output_paths = []
    for input_path in input_paths:
        input_ext = os.path.splitext(input_path)[1].lower()
        output_ext = ".vtt" if input_ext == ".srt" else ".srt"
        
        with open(input_path, "r", encoding="utf-8") as file:
            content = file.read()
        if input_path.endswith(".vtt"):
            content=t7.webvtt_remover(content)
        
        # Convert timestamps
        converted_content = convert_timestamps(content, input_ext, output_ext)
        
        # Output filename with the same basename and new extension
        output_basename = f"{os.path.splitext(os.path.basename(input_path))[0]}{output_ext}"
        output_path = os.path.join(os.path.dirname(input_path), output_basename)
        
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(converted_content)
        
        output_paths.append(output_path)
    if len(output_paths) > 3:

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        temp_dir = os.path.join(tempfile.gettempdir(), f"tempdir_{timestamp}")
        os.makedirs(temp_dir, exist_ok=True)
        srtvtt_zip_filename = os.path.join(temp_dir, "srtvttexchange.zip")
        with zipfile.ZipFile(srtvtt_zip_filename, 'w') as zipf:
            for file in output_paths:
                zipf.write(file, os.path.basename(file))
        
        return [srtvtt_zip_filename]                
    return output_paths

def only_replace_function(ul_files,csv_path):
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # ヘッダーをスキップ
        replacements = [(row[0], row[1]) for row in reader]
    
    #print(csv_path)
    #print(ul_files)


    new_paths=[]
    for ul_file in ul_files:
        with open(ul_file,"r",encoding="utf-8") as various_file:
            texts=various_file.read()

        if ul_file.endswith(".srt"):
            segment_pattern = r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}\s*-->\s*\d{2}:\d{2}:\d{2},\d{3})\n(.*?)(?=\n\d+\n|\Z)'
            segments = re.findall(segment_pattern, texts, re.DOTALL)  # 全てのセグメントを抽出
            
            result = []

            # 各セグメントごとにID、タイムスタンプ、テキストを処理
            for segment in segments:
                segment_id, timestamp, text = segment

                # テキスト部分の単語を置換
                if st.session_state.select_rp_result:
                    for original, replacement in replacements:
                        original=re.escape(original)
                        new_original = rf"\b{original}\b"
                        text = re.sub(new_original, replacement, text)

                    # 置換後のセグメントを結果に保存
                    result.append(f"{segment_id}\n{timestamp}\n{text}\n\n")


            final_texts=''.join(result) 
            #print(final_texts)

        if ul_file.endswith(".vtt"):
            texts=t7.webvtt_remover(texts)
            segment_pattern = r'(\d+)\n(\d{1,2}:\d{2}:\d{2}.\d{3}\s*-->\s*\d{1,2}:\d{2}:\d{2}.\d{3})\n(.*?)(?=\n\d+\n|\Z)'
            segments = re.findall(segment_pattern, texts, re.DOTALL)  # 全てのセグメントを抽出
            
            result = []

            # 各セグメントごとにID、タイムスタンプ、テキストを処理
            for segment in segments:
                segment_id, timestamp, text = segment

                # テキスト部分の単語を置換
                if st.session_state.select_rp_result:
                    for original, replacement in replacements:
                        original=re.escape(original)
                        new_original = rf"\b{original}\b"
                        text = re.sub(new_original, replacement, text)

                    # 置換後のセグメントを結果に保存
                    result.append(f"{segment_id}\n{timestamp}\n{text}\n\n")   
            final_texts='WEBVTT\n\n'+''.join(result) 

        elif ul_file.endswith(".txt"):

            if st.session_state.select_rp_result:
                for original, replacement in replacements:
                    new_original = rf"\b{original}\b"
                    texts = re.sub(new_original, replacement, texts)
                    
                final_texts=texts
                #print(final_texts)

        timestamp_patch = datetime.now().strftime("%Y%m%d%H%M%S")
        temp_dir = os.path.join(tempfile.gettempdir(), f"tempdir_{timestamp_patch}")
        os.makedirs(temp_dir, exist_ok=True)

        new_path=os.path.join(temp_dir,os.path.basename(ul_file))
        #print(new_path)

        with open(new_path,"w",encoding="utf-8") as file:
            file.write(final_texts)
        
        new_paths.append(new_path)
        #print(new_paths)
        if len(new_paths) > 3:

            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            temp_dir = os.path.join(tempfile.gettempdir(), f"tempdir_{timestamp}")
            os.makedirs(temp_dir, exist_ok=True)
            zip_filename = os.path.join(temp_dir, "only_replacing_words.zip")
            with zipfile.ZipFile(zip_filename, 'w') as zipf:
                for file in new_paths:
                    zipf.write(file, os.path.basename(file))
            
            return [zip_filename]
    
    return new_paths

def clear_a():
    del st.session_state.rp_input1
    del st.session_state.rp_input2
    del st.session_state.rp_input3
    st.session_state.rp_input1=None
    st.session_state.rp_input2=None
    st.session_state.rp_input3=None
    st.rerun()

def clear_b():
    del st.session_state.dot_input1
    del st.session_state.dot_input2
    st.session_state.dot_input1=None
    st.session_state.dot_input2=None
    st.rerun()    

def clear_c():
    del st.session_state.alc1
    del st.session_state.alc1_out
    st.session_state.alc1=""
    st.session_state.alc1_out=""
    st.rerun()    

def clear_d():
    del st.session_state.alc2
    del st.session_state.alc2_out
    st.session_state.alc2=""
    st.session_state.alc2_out=""
    st.rerun()      

def clear_e():
    del st.session_state.alc_srt
    del st.session_state.alc2_out
    st.session_state.alc_srt=""
    st.session_state.alc_srt_out=""
    st.rerun()   

def clear_f():
    del st.session_state.alc_inputs
    del st.session_state.alc_namelist
    del st.session_state.alc_processed_file_paths
    st.session_state.alc_uploader_key += 1
    st.session_state.alc_inputs=[]
    st.session_state.alc_namelist=[]
    st.session_state.alc_processed_file_paths=[]

def clear_g():
    del st.session_state.srtvtt_inputs
    del st.session_state.srtvtt_namelist
    del st.session_state.srtvtt_processed_file_paths
    st.session_state.srtvtt_uploader_key += 1
    st.session_state.srtvtt_inputs=[]
    st.session_state.srtvtt_namelist=[]
    st.session_state.srtvtt_processed_file_paths=[]

def clear_h():
    del st.session_state.rp_only_uploaded_files
    del st.session_state.rp_only_filenames
    del st.session_state.rp_only_otfiles
    st.session_state.rp_only_uploaded_files=[]
    st.session_state.rp_only_filenames=[]
    st.session_state.rp_only_otfiles=[]
    st.session_state.rp_only_uploader_key += 1
    st.rerun()

def clear_i():
    del st.session_state.new_t1_input_paths
    st.session_state.new_t1_input_paths=[]
    del st.session_state.new_t1_input_filenames
    st.session_state.new_t1_input_filenames=[]
    del st.session_state.new_t1_ot_excels
    st.session_state.new_t1_ot_excels=[]
    del st.session_state.new_t1_ot_srts
    st.session_state.new_t1_ot_srts=[]
    st.session_state.uploader_new_key += 1
    st.rerun()

def extract_short_name(text):
    match = re.search(r"\((.*?)\)", text)
        # 抽出結果を確認
    if match:
        result = match.group(1)
    return result


def main():

    st.markdown( #☆CSS
        """
        <style>
        body {
            font-family: serif;
            font-size: 62.5%;
        }
        div[data-testid="stToolbar"] {
            visibility: hidden;
            height: 0%;
            position: fixed;
            }
            div[data-testid="stDecoration"] {
            visibility: hidden;
            height: 0%;
            position: fixed;
            }
            #MainMenu {
            visibility: hidden;
            height: 0%;
            }
            header {
            visibility: hidden;
            height: 0%;
            }
            footer {
            visibility: hidden;
            height: 0%;
            }
                    .appview-container .main .block-container{
                        padding-top: 70px;
                        padding-right: 3rem;
                        padding-left: 3rem;
                        padding-bottom: 450px;
                    }  
                    .reportview-container {
                        padding-top: 0rem;
                        padding-right: 3rem;
                        padding-left: 3rem;
                        padding-bottom: 0rem;
                    }
                    header[data-testid="stHeader"] {
                        z-index: -1;
                    }
                    div[data-testid="stToolbar"] {
                    z-index: 100;
                    }
                    div[data-testid="stDecoration"] {
                    z-index: 100;
                    }
        /* 全体幅 */
        .st-emotion-cache-1jicfl2{
            width:90%;
        }
        /*uploaderの表示ファイル部を非表示*/
        .st-emotion-cache-fis6aj{
            display:none;
        }
        .stFileUploaderFile {
            display:none;
        }
        .span {
            color: darkblue;
            font-size: 16px;
        }
        .title {
  
            color: darkblue;
            font-family: "Yu-Gothic";
            font-size: 48px;
            font-weight: bold;
            margin: 0;
        }

        
        .tab_title, .second_tab_title {
            font-size: 30px;
            color: gray;
            margin-bottom: 40px;
            margin-top:20px;
            position: relative;
            z-index: 1;
            padding-left: 3.3rem; /* 左側にスペースを確保 */
            font-weight:bold;
        }

        .tab_title::before {
            content:"";
            top: 0.4rem;
            left: 0.4rem;
            z-index: 8000;
            width: 1.6rem;
            height: 1.6rem;
            border-style: solid;
            position: absolute;
            -o-border-image: linear-gradient(-135deg, #9dfd65, #0058ca) 1 1 1 1 / 0.25rem 0.25rem 0.25rem 0.25rem;
            border-image: linear-gradient(-135deg, #9dfd65, #0058ca) 1 1 1 1 / 0.25rem 0.25rem 0.25rem 0.25rem;
        }        
        .second_tab_title::before {
            content:"";
            top: 0.4rem;
            left: 0.4rem;
            z-index: 8000;
            width: 1.6rem;
            height: 1.6rem;
            border-style: solid;
            position: absolute;
            -o-border-image: linear-gradient(-135deg, 	#fff , #237bd9) 1 1 1 1 / 0.25rem 0.25rem 0.25rem 0.25rem;
            border-image: linear-gradient(-135deg, 	#fff, #237bd9) 1 1 1 1 / 0.25rem 0.25rem 0.25rem 0.25rem;
        }        
        .tab_title::after {
            content: ''; 
            top: 1.3rem;
            left: 1.3rem;
            width: 1.2rem;
            height: 1.2rem;
            z-index: 9999;
            position: absolute; 
            border-style: solid;
            border-image: linear-gradient(45deg, #ff16a6, #fffb06) 1 1 1 1 / 0.25rem 0.25rem 0.25rem 0.25rem;
        }
        .second_tab_title::after {
            content: ''; 
            top: 1.3rem;
            left: 1.3rem;
            width: 1.2rem;
            height: 1.2rem;
            z-index: 9999;
            position: absolute; 
            border-style: solid;
            border-image: linear-gradient(45deg,#a1f9ff, #fff)  1 1 1 1 / 0.25rem 0.25rem 0.25rem 0.25rem;
        }
        .subhead,.subhead2{
            font-size:24px;
            font-weight:bold;
            color:gray;
            margin-bottom:10px;
        .st-ae{margin-bottom:30px;}
        }
        .subhead2 {
         margin-top: 40px; /* ここに希望の margin-top 値を設定 */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    from streamlit_module import moz_func as moz
    from streamlit_module import moz_tab7 as moz_t7
    from streamlit_module import moz_tab8 as moz_t8
    from streamlit_module import moz_tab9 as moz_t9
    from streamlit_module import youtube_streamlit as moz_t10
    from streamlit_module import moz_json as js
    from streamlit_module import moz_replace as rp
    from streamlit_module import moz_license as ls
    from streamlit_module import moz_split_period as period

    # 各タブのセッション状態キーのリスト
    tab1_keys = ['t1_translated_text','output_html_tab1', 'output_files_tab1', 'output_file_tab1', 'output_ja_files_tab1', 'df_data_tab1','t1_input_file_path','t1_translated_text','t7_df']
    tab2_keys = ['df_data_tab2','t2_translated_text','file_path_tab2','df_tab2','output_html_tab2', 'input_file_path_tab2','output_file_tab2','translated_text_tab2','saved_files_tab2']
    tab3_keys = ['t3_namelist_B','t3_namelist_A','output_files_tab3_docx_to_srttxt', 'output_files_tab3_srttxt_to_docx','t3_upload_files_A','t3_upload_files_B']
    #tab4_keys = ['output_excel_tab4', 'df_data_tab4', 'download_filename_tab4','english_path_both','japanese_path_both','english_path_only','japanese_path_only']
    tab4_keys_both=['english_path_both','japanese_path_both','both_excel_file_path','both_df','both_download_filename_tab4']
    tab4_keys_en=['english_path_only','en_excel_file_path','en_df','en_download_filename_tab4']
    tab4_keys_ja=['japanese_path_only','ja_excel_file_path','ja_df','ja_download_filename_tab4']
    tab4_keys=tab4_keys_both + tab4_keys_en + tab4_keys_ja
    tab5_keys = ['upload_files','t5_kuten_files','t5_filenames', 'results']
    tab6_keys = ['t6_srtnamelist','t6_jsnamelist','t6_jsons','t6_srts','tab9_output_srt_files','tab9_output_txt_files','tab9_files_ready']#'tab9_output_srt_file','tab9_output_txt_file',
    tab7_keys = ['yt_namelist','yt_output_srt','yt_output_txt','download_ready','yt_srts']
    tab11_keys = ['selected_model','t11_namelist','t11_srt_files','t11_jsons','skipped_files']

    uploader_keys=['uploader_key',
                   'uploader_tab2_key',
                   'uploader_tab3_1_key',
                   'uploader_tab3_2_key',
                   'uploader_tab4_1_key',
                   'uploader_tab4_2_key',
                   'uploader_tab4_3_key',
                   'uploader_tab4_4_key',
                   'uploader_tab5_key',
                   'uploader_tab6_1_key',
                   'uploader_tab6_2_key',
                   'uploader_tab7_key',
                   'uploader_tab8_key',
                   ]
    
    for key in uploader_keys:
        if key not in st.session_state:
            st.session_state[key]=0
    


    # セッション状態を初期化
    if 'current_tab' not in st.session_state:
        st.session_state.current_tab = '配布字幕の再編' 

    # 各タブのセッション状態を初期化
    for key in tab1_keys + tab2_keys + tab3_keys + tab4_keys + tab6_keys + tab7_keys+tab11_keys:
        if key not in st.session_state:
            st.session_state[key] = None
    
    for key in tab5_keys:
        if key not in st.session_state:
            st.session_state[key]=[]
        
    if 'tab9_files_ready' not in st.session_state:
         st.session_state['tab9_files_ready'] = False       


    # セッションのデバイスを初期化
    #if 'device' not in st.session_state:
    #    # 起動時にGPUが利用可能であればGPUをデフォルトに設定、それ以外の場合はCPU
    #   st.session_state['device'] = 'GPU' if torch.cuda.is_available() else 'CPU'

    
    st.markdown('''<h1 class="title">PeriOz 2. <span class="span"> - subtitle editor -</span></h1>''',unsafe_allow_html=True)
    tab_labels = ["配布字幕の再編", "翻訳お手伝い", "Word/Excel↔SRT/VTT/TXT", "SRT/VTT→Excel(2言語)","whisperファイルの復活①","whisperファイルの復活②","YT付属字幕の再編","日本語srt,vttの句読点分割","単語置き換え管理","Dot管理","その他","翻訳先言語","LICENSE"]
        # サイドバーにタブの選択肢を表示

    with st.container():
        selected_tab = st.sidebar.radio("▽ メニューを選択してください。", tab_labels, key='only_radio',on_change=load_multi)    
        # 選択されたタブをセッション状態に保存
        st.session_state.current_tab = selected_tab

    with st.container():
        st.session_state.replace_word = st.sidebar.toggle("単語置き換えを有効にする",
                                                        #value=st.session_state.toggle_replacements , 
                                                        key='toggle_key',on_change=onchange_toggle)
    with st.container():
        st.session_state.ja_split = st.sidebar.toggle("句点分割を有効にする",
                                                        #value=st.session_state.toggle_replacements , 
                                                        key='ja_split_key',on_change=onchange_ja_split)
    
        #print(st.session_state['comma_split_key'])
    with st.container():
        st.session_state.comma_split = st.sidebar.toggle("読点分割を有効にする",
                                                        #value=st.session_state.toggle_replacements , 
                                                        key='comma_split_key',on_change=onchange_comma_split)
    #save_toggle_choice()
    #print(f"[after]toggle_key:{st.session_state.toggle_key}")
    #print(f"[after]replace_word:{st.session_state.replace_word}") 
    with st.container():    
        with st.sidebar.expander("読点分割設定"):
            
            st.session_state.max_split_current = st.number_input('最大文字数', min_value=11, max_value=100,key='max_split', step=1)
            st.session_state.min_split_current = st.number_input('最小文字数', min_value=1, max_value=20, key='min_split', step=1)
            minmaxstock=st.button("保存")
            if minmaxstock:
                save_minmax()
    


    if st.session_state.current_tab=="単語置き換え管理": #☆単語
        
        
        with st.container():
            

            st.markdown("<div class='tab_title'>置き換え単語の管理(CSV保存)</div>", unsafe_allow_html=True)

            # カラムを作成
            left_column,gap, right_column = st.columns([6,1,12])
            # 右のカラムに表を表示
            with right_column:
                Z1,Z2=st.columns([1,1])

                with Z1:
                
                    st.session_state.select_rp_result = st.selectbox(
                        "★ 置き換え単語帳をお選びください",
                        ("replacements.csv", "replacements_2.csv", "replacements_3.csv"),
                        #index=('replacements.csv', 'replacements_2.csv','replacements_3.csv').index(st.session_state.select_rp_note),
                        key='rp_key',  # Tab 1 でのみ使用
                        on_change=save_rp_filename
                        
                        )
                    

                    # CSVファイル名
                    data_folder = "/content/my_app"
                    csv_file = os.path.join(data_folder,st.session_state.select_rp_result)

                    # 毎回CSVを再読み込み
                    df = rp.load_csv(csv_file)
            # セッションステートに状態管理インスタンスを格納
                if 'state_manager' not in st.session_state:
                    st.session_state.state_manager = rp.StateManager()
                    st.session_state.state_manager.save_state(df)  # 最新のデータフレームを保存


                edited_df = st.data_editor(df, hide_index=True, use_container_width=True, num_rows="dynamic",key="edit_widget")
                if st.session_state.dammy_rp_key !=st.session_state.rp_key:
                    save_selected_file(df)
            
            # 左のカラムにテキストボックスとボタンを配置
            with left_column:

        

                original_word = st.text_input("元の単語",key="rp_input1")
                replacement_word_pre = st.text_input("置き換え後の単語",key="rp_input2")
                if replacement_word_pre=="$$$":
                    replacement_word=""
                else:
                    replacement_word=replacement_word_pre
                tag = st.text_input("タグ",key="rp_input3")

                # セット登録ボタン
                second_left_column, second_right_column = st.columns([1, 1])
                with second_left_column:
                    if st.button("セット登録",use_container_width=True,key="set_reg_widget"):
                        if original_word and replacement_word_pre:
                            #identifier = str(uuid.uuid4())
                            patterns = [
                                (f"{original_word.lower()}", f"{replacement_word}", tag, "Set"),
                                (f"{original_word.capitalize()}", f"{replacement_word}", tag, "Set")
                            ]
                            new_rows = pd.DataFrame(patterns, columns=["元の単語", "置き換え後の単語", "タグ", "属性"])
                            df = pd.concat([df, new_rows], ignore_index=True)
                            rp.save_csv(df, csv_file)
                            st.session_state.state_manager.save_state(df)  # 新しい状態を保存
                            st.rerun()  # 即時反映

                        else:
                            st.warning("元の単語と置き換え後の単語を入力してください。")

                # 単独登録ボタン
                with second_right_column:
                    if st.button("単独登録",use_container_width=True,key="single_reg_widget"):
                        if original_word and replacement_word_pre:
                            #identifier = str(uuid.uuid4())
                            patterns = [
                                (rf"{original_word}", f"{replacement_word}", tag, "Single"),
                            ]
                            new_row = pd.DataFrame(patterns, columns=["元の単語", "置き換え後の単語", "タグ", "属性"])
                            df = pd.concat([df, new_row], ignore_index=True)
                            rp.save_csv(df, csv_file)
                            st.session_state.state_manager.save_state(df)  # 新しい状態を保存
                            st.rerun()  # 即時反映
                            
                        else:
                            st.warning("元の単語と置き換え後の単語を入力してください。")

                third_left_column,third_right_column=st.columns([1,1])
                with third_left_column:
                    if st.button("保存",use_container_width=True,key="keep_del_widget"):
                        rp.save_csv(edited_df, csv_file)
                        st.session_state.state_manager.save_state(edited_df)  # 新しい状態を保存
                        st.success("変更が保存されました。")
                        st.rerun()  # 再レンダリング
                with third_right_column:
                    # 取り消しボタン
                    if st.button("取り消し",use_container_width=True,key="undo_widget"):
                        rp_history_count=st.session_state.state_manager.history_count()
                        previous_df = st.session_state.state_manager.undo()  # 1つ前の状態を取得
                        
                        if rp_history_count==1:
                            st.warning("これ以上とりけせません。")
                        elif previous_df is not None:
                            rp.save_csv(previous_df,csv_file)
                            df=previous_df
                            st.rerun()
                        else:
                            st.warning("これ以上取り消せません。")
                        

                if st.button("クリア",use_container_width=True,key="rp_clear_button"):
                    clear_a()

            #st.sidebar.write(st.session_state.selected_model)
            #st.sidebar.write(st.session_state.selected_model2)
            #st.sidebar.write(st.session_state.selected_model3)
            #st.sidebar.write(st.session_state.select_rp_result)
            #st.sidebar.write(st.session_state.select_dot_result)
            # print(f"st.session_state.select_dot_result:{st.session_state.select_dot_result}")
            # print(f'st.session_state.dot_key:{st.session_state.dot_key}')
        
        
    elif st.session_state.current_tab=="Dot管理":   #☆Dot

        with st.container():
       
            
                           

            st.markdown("<div class='tab_title'>Dot管理(CSV保存)</div>", unsafe_allow_html=True)
            
            # カラムを作成
            dot_left_column,gap, dot_right_column = st.columns([6,1,12])
            # 右のカラムに表を表示
            with dot_right_column:
                Y1,Y2=st.columns([1,1])
                with Y1:
                    st.session_state.select_dot_result=st.selectbox(
                        "★ Dot保護の単語帳をお選びください",
                        ("dot_manager.csv", "dot_manager_2.csv", "dot_manager_3.csv"),
                       
                        key='dot_key',  # Tab 1 でのみ使用
                        on_change=save_dot_filename
                    )
                    #print(st.session_state.dammy_dot_key,st.session_state.dot_key)

 
                    data_folder = "/content/my_app"
                    dot_csv_file = os.path.join(data_folder,st.session_state.select_dot_result)
                    dot_df = rp.load_csv(dot_csv_file)

                    if 'dot_state_manager' not in st.session_state:
                        print("initialize")
                        st.session_state.dot_state_manager = rp.StateManager()
                        st.session_state.dot_state_manager.save_state(dot_df)  # 最新のデータフレームを保存
                dot_edited_df = st.data_editor(dot_df, hide_index=True, use_container_width=True, num_rows="dynamic",key="dot_edit_widget")
                if st.session_state.dammy_dot_key != st.session_state.dot_key:
                    save_dot_selected_file(dot_df)
            # 左のカラムにテキストボックスとボタンを配置
            with dot_left_column:
                    
                dot_original_word_pre = st.text_input("元の単語", key="dot_input1")
                
                dot_tag = st.text_input("タグ", key="dot_input2")

                # セット登録ボタン
                dot_second_left_column, dot_second_right_column = st.columns([1, 1])
                with dot_second_left_column:
                    if st.button("セット登録",use_container_width=True,key="dot_set_reg_widget"):
                        if dot_original_word_pre :
                            #identifier = str(uuid.uuid4())
                            dot_original_word=dot_original_word_pre.replace("\.",".")
                            dot_replacement_word = dot_original_word_pre.replace("\.","<dot>").replace(".","[dot]").replace("<dot>",".")
                            patterns = [
                                (rf"{dot_original_word.lower()}", f"{dot_replacement_word.lower()}", dot_tag, "Set"),
                                (rf"{dot_original_word.capitalize()}", f"{dot_replacement_word.capitalize()}", dot_tag, "Set")
                            ]
                            new_rows = pd.DataFrame(patterns, columns=["元の単語", "置き換え後の単語", "タグ", "属性"])
                            dot_df = pd.concat([dot_df, new_rows], ignore_index=True)
                            rp.save_csv(dot_df, dot_csv_file)
                            st.session_state.dot_state_manager.save_state(dot_df)  # 新しい状態を保存
                            st.rerun()  # 即時反映

                        else:
                            st.warning("★ 元の単語を入力してください。")

                # 単独登録ボタン
                with dot_second_right_column:
                    if st.button("単独登録",use_container_width=True,key="dot_single_reg_widget"):
                        if dot_original_word_pre :
                            #identifier = str(uuid.uuid4())
                            dot_original_word=dot_original_word_pre.replace("\.",".")
                            dot_replacement_word = dot_original_word_pre.replace("\.","<dot>").replace(".","[dot]").replace("<dot>",".")
                            patterns = [
                                (rf"{dot_original_word}", f"{dot_replacement_word}", dot_tag, "Single"),
                            ]
                            new_row = pd.DataFrame(patterns, columns=["元の単語", "置き換え後の単語", "タグ", "属性"])
                            dot_df = pd.concat([dot_df, new_row], ignore_index=True)
                            rp.save_csv(dot_df, dot_csv_file)
                            st.session_state.dot_state_manager.save_state(dot_df)  # 新しい状態を保存
                            st.rerun()  # 即時反映
                            
                        else:
                            st.warning("★ 元の単語を入力してください。")

                third_left_column_dot,third_right_column_dot=st.columns([1,1])
                if st.button("クリア",use_container_width=True,key="dot_clear_button"):
                    clear_b()

                with third_left_column_dot:
                    if st.button("保存",use_container_width=True,key="dot_keep_del_widget"):
                        rp.save_csv(dot_edited_df, dot_csv_file)
                        st.session_state.dot_state_manager.save_state(dot_edited_df)  # 新しい状態を保存
                        st.success("変更が保存されました。")
                        st.rerun()  # 再レンダリング
                with third_right_column_dot:
                    # 取り消しボタン
                    if st.button("取り消し",use_container_width=True,key="dot_undo_widget"):
                        history_count=st.session_state.dot_state_manager.history_count()
                        #print(f"history_count:{history_count}")
                        dot_previous_df = st.session_state.dot_state_manager.undo()  # 1つ前の状態を取得
                        if history_count==1:
                            st.warning("これ以上取り消せません。")                   
                        elif  dot_previous_df is not None:
                            rp.save_csv(dot_previous_df, dot_csv_file)
                            dot_df = dot_previous_df  # `df`を再設定 ???これだけst.session_state???
                            st.rerun()  # 再レンダリングを強制
                        else:
                            st.warning("これ以上取り消せません。")
            
                                            
      
            # print(f"st.session_state.select_dot_result:{st.session_state.select_dot_result}")
            # print(f'st.session_state.dot_key:{st.session_state.dot_key}')

    elif st.session_state.current_tab == '配布字幕の再編': #☆Rebuild
        # print(f"st.session_state.ja_split:{st.session_state.ja_split}")
        # print(f"st.session_state.ja_split_key:{st.session_state.ja_split_key}")
        with st.container():
         
            
                    
            st.markdown("<div class='tab_title'>配布字幕の再編</div>", unsafe_allow_html=True)
            t1_uploaded_file = st.file_uploader("★ ファイルをアップロードしてください", type=['srt', 'vtt'], key=f"file_uploader_tab1_{st.session_state.uploader_key}")
            if t1_uploaded_file:
                timestamp_patch = datetime.now().strftime("%Y%m%d%H%M%S")
                temp_dir = os.path.join(tempfile.gettempdir(), f"tempdir_{timestamp_patch}")
                os.makedirs(temp_dir, exist_ok=True)

                st.session_state.t1_input_file_path = os.path.join(temp_dir, f'{t1_uploaded_file.name}')
                with open(st.session_state.t1_input_file_path, "wb") as f:
                    f.write(t1_uploaded_file.getbuffer())

            if "t1_input_file_path" in st.session_state and st.session_state.t1_input_file_path:
                st.warning(f"{os.path.basename(st.session_state.t1_input_file_path)}がアップロードされました。")
                
            

            A1,A3,A4=st.columns([2,1,1])
            with A1:
                do_periods =st.button('ピリオドによる補正',use_container_width=True,key="periods_widget")
                    
            with A3:
                if st.button("クリア",use_container_width=True,key="clear_tab1_widget"):
                    moz.clear_session_state('配布字幕の再編')       
            with A4:     
                if st.button("終了",use_container_width=True,key="exit_tab1_widget"):
                    os.kill(os.getpid(), signal.SIGTERM)

            if do_periods:
                if st.session_state.t1_input_file_path:
                    st.session_state.output_html_tab1, st.session_state.output_files_tab1, st.session_state.output_file_tab1, st.session_state.t7_df = moz.process_file(st.session_state.t1_input_file_path,st.session_state.replace_word)
                else:
                    st.error("ファイルをアップロードしてください。")
     

            if st.session_state.output_html_tab1:
                st.markdown("#### アップロードされたファイルの内容")
                components.html(st.session_state.output_html_tab1, height=350)
                for file in st.session_state.output_files_tab1:
                    original_filename = os.path.basename(file)
                    with open(file, "rb") as f:
                        st.download_button(label=f"{original_filename}をダウンロード", data=f, file_name=original_filename, key=f"download_button_{os.path.basename(file)}")


            if st.session_state.output_file_tab1:
                st.session_state.t1_translated_text = st.text_area("★ 翻訳されたテキストを入力してください。※ 翻訳ボタンを押すまで1秒待った方がいいかもしれません。",value=st.session_state.t1_translated_text, key="translated_text_tab1", height=400)
                B1,B3,B4=st.columns([2,1,1])
                with B1:
                    if st.button('翻訳ファイル作成',use_container_width=True,key="t1_translate_widget"):
                        st.session_state.output_ja_files_tab1, st.session_state.df_data_tab1 = moz.vtt_translate(st.session_state.t1_input_file_path, st.session_state.t1_translated_text, st.session_state.output_file_tab1)
                    
                        
            if st.session_state.output_ja_files_tab1:
                st.success("処理が完了しました。以下のリンクからファイルをダウンロードできます。")
                for idx,file in enumerate(st.session_state.output_ja_files_tab1):
                    original_filename = os.path.basename(file)
                    with open(file, "rb") as f:
                        st.download_button(label=f"{original_filename}をダウンロード", data=f, file_name=original_filename, key=f"download_ja_button_{idx}")


            if st.session_state.df_data_tab1 is not None:
                df = st.session_state.df_data_tab1
                st.table(df)
            # print(f"st.session_state.select_dot_result:{st.session_state.select_dot_result}")
            # print(f'st.session_state.dot_key:{st.session_state.dot_key}')
            
                    
    elif st.session_state.current_tab  == '翻訳お手伝い': #☆help
        # print(f"st.session_state.ja_split:{st.session_state.ja_split}")
        # print(f"st.session_state.ja_split:{st.session_state.ja_split_key}")
        with st.container():    
            #load_multi()
            
                    
            st.markdown("<div class='tab_title'>翻訳お手伝い</div>", unsafe_allow_html=True)

            uploaded_file_tab2 = st.file_uploader('★ ファイルをアップロードしてください　※　テキストファイルは"_NR.txt",　"_R.txt"のみ対応', type=['srt', 'vtt', 'txt'], key=f"file_uploader_tab2_{st.session_state.uploader_tab2_key}")
        
            if uploaded_file_tab2:
                timestamp_patch = datetime.now().strftime("%Y%m%d%H%M%S")
                temp_dir = os.path.join(tempfile.gettempdir(), f"tempdir_{timestamp_patch}")
                os.makedirs(temp_dir, exist_ok=True)
                
                
                st.session_state.input_file_path_tab2 = os.path.join(temp_dir, f'{uploaded_file_tab2.name}')
                with open(st.session_state.input_file_path_tab2, "wb") as f:
                    f.write(uploaded_file_tab2.getbuffer())
                
            if st.session_state.input_file_path_tab2:
                st.warning(f"{os.path.basename(st.session_state.input_file_path_tab2)}がアップロードされました。")
                
            C1,C3,C4=st.columns([2,1,1])
            with C1:
                do_translate=st.button('処理実行',use_container_width=True, key='process_tab2_widget')
                      
            with C3:
                if st.button("クリア", key='clear_tab2_widget',use_container_width=True):
                    moz.clear_session_state('翻訳お手伝い')
            with C4:
                if st.button("終了", key="exit_tab2_widget",use_container_width=True):
                    os.kill(os.getpid(), signal.SIGTERM)            

            if do_translate:
                if st.session_state.input_file_path_tab2:
                    st.session_state.output_html_tab2, st.session_state.file_path_tab2 = moz.display_file_content(st.session_state.input_file_path_tab2,st.session_state.replace_word)
                else:
                    st.error("ファイルをアップロードしていください。")

            if st.session_state.output_html_tab2:
                st.markdown("#### アップロードされたファイルの内容")
                components.html(st.session_state.output_html_tab2, height=330)

            if st.session_state.file_path_tab2:
                original_filename = os.path.basename(st.session_state.file_path_tab2)
                with open(st.session_state.file_path_tab2, "rb") as f:
                    st.download_button(label=f"{original_filename}をダウンロード", data=f, file_name=original_filename, key="file_path_tab2_for_key_widget")


            if st.session_state.output_html_tab2:
                st.session_state.t2_translated_text = st.text_area("★ 翻訳されたテキストを入力してください。※ 翻訳ボタンを押すまで1秒待った方がいいかもしれません。",value=st.session_state.t2_translated_text, key='new_text_widget', height=400)
                D1,D3,D4=st.columns([2,1,1])
                with D1:
                    if st.button('翻訳ファイル作成', key='create_translation_tab2_widget',use_container_width=True):
                        st.session_state.saved_files_tab2,st.session_state.df_data_tab2  = moz.save_translated_content(st.session_state.input_file_path_tab2, st.session_state.t2_translated_text)
                    

            if st.session_state.saved_files_tab2:
                st.success("処理が完了しました。以下のリンクからファイルをダウンロードできます。")
                for i, file in enumerate(st.session_state.saved_files_tab2):
                    original_filename = os.path.basename(file)
                    with open(file, "rb") as f:
                        st.download_button(label=f"{original_filename}をダウンロード", data=f, file_name=original_filename, key=f"download_translated_{os.path.basename(file)}_{i}")

            # print(f"st.session_state.select_dot_result:{st.session_state.select_dot_result}")
            # print(f'st.session_state.dot_key:{st.session_state.dot_key}')
            if st.session_state.df_data_tab2 is not None:
                df = st.session_state.df_data_tab2
                st.table(df)

            
                    

    elif st.session_state.current_tab == 'Word/Excel↔SRT/VTT/TXT': #☆exchange
        # print(f"st.session_state.ja_split:{st.session_state.ja_split}")
        # print(f"st.session_state.ja_split:{st.session_state.ja_split_key}")
        with st.container():
            #load_multi()
            
                       
            st.markdown("<div class='tab_title'>Word,Excel↔SRT/VTT/TXT</div>", unsafe_allow_html=True)
            st.markdown("<div class='subhead'>Word,ExcelからSRT,VTT,TXTへ変換</div>", unsafe_allow_html=True)
            st.session_state.uploaded_docx_files = st.file_uploader("★ Word,Excelファイルをアップロードしてください", type=['docx', 'xlsx'], accept_multiple_files=True, key=f"file_uploader_tab3_1_{st.session_state.uploader_tab3_1_key}")
            if st.session_state.uploaded_docx_files:
                timestamp_patch = datetime.now().strftime("%Y%m%d%H%M%S")
                temp_dir = os.path.join(tempfile.gettempdir(), f"tempdir_{timestamp_patch}")
                os.makedirs(temp_dir, exist_ok=True)

                st.session_state.t3_upload_files_A,st.session_state.t3_namelist_A=upstock(st.session_state.t3_upload_files_A,st.session_state.t3_namelist_A,st.session_state.uploaded_docx_files,temp_dir)


            if st.session_state.t3_upload_files_A:
                if len(st.session_state.t3_upload_files_A) < 4:
                    for file in st.session_state.t3_upload_files_A:
                        st.warning(f"{os.path.basename(file)}がアップロードされました。")
                else:
                    st.warning(f"{len(st.session_state.t3_upload_files_A)}つのファイルがアップロードされました。")         
            


            E1,E3,E4=st.columns([2,1,1])
            with E1:
                do_exceltosrt=st.button("変換実行",use_container_width=True,key="t3_doexe1_widget")

            with E3:
                if st.button("クリア", key="clear_tab3_1_widget",use_container_width=True):
                    moz.clear_session_state(tab='Word/Excel↔SRT/VTT/TXT',select_clear="First")
            with E4:
                if st.button("終了", key="exit_tab3_1_widget",use_container_width=True):
                    os.kill(os.getpid(), signal.SIGTERM)   

            if do_exceltosrt:
                if st.session_state.t3_upload_files_A:
                    st.session_state.output_files_tab3_docx_to_srttxt = moz.convert_docx_to_srttxt(st.session_state.t3_upload_files_A)  
                else:
                    st.error("ファイルをアップロードしてください。")

            if st.session_state.output_files_tab3_docx_to_srttxt:
                st.success("処理が完了しました。以下のリンクからファイルをダウンロードできます。")
                for i, file in enumerate(st.session_state.output_files_tab3_docx_to_srttxt):
                    original_filename = os.path.basename(file)
                    with open(file, "rb") as f:
                        st.download_button(label=f"{original_filename}をダウンロード", data=f, file_name=original_filename, key=f"download_docx_to_srttxt_{i}")
    
            st.markdown("<div class='subhead2'>SRT,VTT,TXTからWord,Excelへの変換</div>", unsafe_allow_html=True)
            uploaded_srtext_files = st.file_uploader('★ SRT/VTT/TXTファイルをアップロードしてください　※　テキストファイルは"_NR.txt",　"_R.txt"のみ対応', type=['srt', 'vtt', 'txt'], accept_multiple_files=True, key=f"file_uploader_tab3_2_{st.session_state.uploader_tab3_2_key}")
            
            if uploaded_srtext_files:
                timestamp_patch = datetime.now().strftime("%Y%m%d%H%M%S")
                temp_dir = os.path.join(tempfile.gettempdir(), f"tempdir_{timestamp_patch}")
                os.makedirs(temp_dir, exist_ok=True)

                st.session_state.t3_upload_files_B,st.session_state.t3_namelist_B=upstock(st.session_state.t3_upload_files_B,st.session_state.t3_namelist_B,uploaded_srtext_files,temp_dir)
                


            if st.session_state.t3_upload_files_B:
                if len(st.session_state.t3_upload_files_B) < 4:
                    for file in st.session_state.t3_upload_files_B:
                        st.warning(f"{os.path.basename(file)}がアップロードされました。")
                else:
                    st.warning(f"{len(st.session_state.t3_upload_files_B)}つのファイルがアップロードされました。")         
            
            
            F1,F3,F4=st.columns([2,1,1])
            with F1:
                do_srttoexcel=st.button("変換実行", key="convert_srttxt_widget",use_container_width=True)
                   
            with F3:
                if st.button("クリア", key="clear_tab3_2_widget",use_container_width=True):
                    moz.clear_session_state(tab='Word/Excel↔SRT/VTT/TXT',select_clear="Second")
            with F4:
                if st.button("終了", key="exit_tab3_2_widget",use_container_width=True):
                    os.kill(os.getpid(), signal.SIGTERM)

            if do_srttoexcel:
                if st.session_state.t3_upload_files_B:
                    st.session_state.output_files_tab3_srttxt_to_docx = moz.process_doc_files(st.session_state.t3_upload_files_B,replace_word=st.session_state.replace_word)
                else:
                    st.error("ファイルをアップロードしてください。")


            if st.session_state.output_files_tab3_srttxt_to_docx:
                st.success("処理が完了しました。以下のリンクからファイルをダウンロードできます。")
                for i, file in enumerate(st.session_state.output_files_tab3_srttxt_to_docx):
                    original_filename = os.path.basename(file)
                    with open(file, "rb") as f:
                        st.download_button(label=f"{original_filename}をダウンロード", data=f, file_name=original_filename, key=f"download_srttxt_to_docx_{i}")
            

            # print(f"st.session_state.select_dot_result:{st.session_state.select_dot_result}")
            # print(f'st.session_state.dot_key:{st.session_state.dot_key}')
            
                 
    elif st.session_state.current_tab == 'SRT/VTT→Excel(2言語)':#☆makeExcel
        # print(f"st.session_state.ja_split:{st.session_state.ja_split}")
        # print(f"st.session_state.ja_split:{st.session_state.ja_split_key}")
        with st.container():
            #load_multi()
            
                 
            st.markdown("<div class='tab_title'>SRT/VTT→Excel(2言語)</div>", unsafe_allow_html=True)
            lang_tail=extract_short_name(st.session_state.language_result)
            lang_name=(st.session_state.language_result).replace(f' ({lang_tail})',"")
            option = st.radio("★ 選択してください:", (f'{lang_name} and English', 'Only English', f'Only {lang_name}'),horizontal=True,on_change=load_multi)

            english_file = None
            japanese_file = None

            if option == f'{lang_name} and English':
                G1,G2=st.columns([1,1])
                with G1:
                    english_file = st.file_uploader("★ Please upload an English SRT/VTT file.", type=['srt', 'vtt'], key=f'file_uploader_tab4_1_{st.session_state.uploader_tab4_1_key}')
                    error_holder_column1=st.empty()
                    if english_file:
                        timestamp_patch = datetime.now().strftime("%Y%m%d%H%M%S")
                        temp_dir = os.path.join(tempfile.gettempdir(), f"tempdir_{timestamp_patch}")
                        os.makedirs(temp_dir, exist_ok=True)
                        st.session_state.english_path_both = os.path.join(temp_dir, f"{english_file.name}")
                    
                        with open(st.session_state.english_path_both, 'wb') as f:
                            f.write(english_file.getbuffer())
                        
                        

                    if st.session_state.english_path_both:
                        st.warning(f"{os.path.basename(st.session_state.english_path_both)}がアップロードされました。")

                with G2:
                    japanese_file = st.file_uploader(f"★ Please upload a {lang_name} SRT/VTT file.", type=['srt', 'vtt'], key=f'file_uploader_tab4_2_{st.session_state.uploader_tab4_2_key}')
                    error_holder_column2=st.empty()
                    if japanese_file:
                        timestamp_patch = datetime.now().strftime("%Y%m%d%H%M%S")
                        temp_dir = os.path.join(tempfile.gettempdir(), f"tempdir_{timestamp_patch}")
                        os.makedirs(temp_dir, exist_ok=True)
                        st.session_state.japanese_path_both = os.path.join(temp_dir, f"{japanese_file.name}")
                        with open(st.session_state.japanese_path_both, 'wb') as f:
                            f.write(japanese_file.getbuffer())

                        

                    if st.session_state.japanese_path_both:
                        st.warning(f"{os.path.basename(st.session_state.japanese_path_both)}がアップロードされました。")
    

            elif option == 'Only English':
                english_file = st.file_uploader("★ Please upload an English SRT/VTT file.", type=['srt', 'vtt'], key=f'file_uploader_tab4_3_{st.session_state.uploader_tab4_3_key}')
                error_holder_only_en=st.empty()
                if english_file:
                    timestamp_patch = datetime.now().strftime("%Y%m%d%H%M%S")
                    temp_dir = os.path.join(tempfile.gettempdir(), f"tempdir_{timestamp_patch}")
                    os.makedirs(temp_dir, exist_ok=True)
                    st.session_state.english_path_only = os.path.join(temp_dir, f"{english_file.name}")

                    with open(st.session_state.english_path_only, 'wb') as f:
                        f.write(english_file.getbuffer())
                
                if st.session_state.english_path_only:
                    st.warning(f"{os.path.basename(st.session_state.english_path_only)}がアップロードされました。")

            else:
                japanese_file = st.file_uploader(f"★ Please upload a {lang_name} SRT/VTT file.", type=['srt', 'vtt'], key=f'file_uploader_tab4_4_{st.session_state.uploader_tab4_4_key}')
                error_holder_only_ja=st.empty()
                if japanese_file:
                    timestamp_patch = datetime.now().strftime("%Y%m%d%H%M%S")
                    temp_dir = os.path.join(tempfile.gettempdir(), f"tempdir_{timestamp_patch}")
                    os.makedirs(temp_dir, exist_ok=True)

                    st.session_state.japanese_path_only = os.path.join(temp_dir, f"{japanese_file.name}")

                    with open(st.session_state.japanese_path_only, 'wb') as f:
                        f.write(japanese_file.getbuffer())

                if st.session_state.japanese_path_only:
                    st.warning(f"{os.path.basename(st.session_state.japanese_path_only)}がアップロードされました。")

            H1,H3,H4=st.columns([2,1,1])

            with H3:
                if st.button("クリア", key='clear_tab4_widget',use_container_width=True):
                    if option==f'{lang_name} and English':
                        moz.clear_session_state(tab='SRT/VTT→Excel(2言語)',option=f'{lang_name} and English')
                    if option=='Only English':
                        moz.clear_session_state(tab='SRT/VTT→Excel(2言語)',option='Only English')
                    if option==f'Only {lang_name}':
                        moz.clear_session_state(tab='SRT/VTT→Excel(2言語)',option=f'Only {lang_name}')
                        
            with H4:
                if st.button("終了", key="exit_tab4_widget",use_container_width=True):
                        os.kill(os.getpid(), signal.SIGTERM)              

            with H1:
                if option==f'{lang_name} and English':
                    do_exe_both=st.button("処理実行", key='process_button_tab4_both_widget',use_container_width=True)
                if option=='Only English':
                    do_exe_en=st.button("処理実行", key='process_button_tab4_en_widget',use_container_width=True)
                if option==f'Only {lang_name}':    
                    do_exe_ja=st.button("処理実行", key='process_button_tab4_ja_widget',use_container_width=True)
                    
            if option == f'{lang_name} and English':
                
                if do_exe_both:
                    if st.session_state.english_path_both and st.session_state.japanese_path_both:
                        st.session_state.both_excel_file_path, st.session_state.both_df = moz.create_excel_from_srt(english_path=st.session_state.english_path_both, japanese_path=st.session_state.japanese_path_both,replace_word=st.session_state.replace_word)
                        if st.session_state.both_excel_file_path==None :
                            st.error("ファイル処理中にエラーが発生しました")
                    elif st.session_state.english_path_both:
                        error_holder_column2.error(f"Please upload a {lang_name} file.")
                    elif st.session_state.japanese_path_both:
                        error_holder_column1.error("Please upload an English file.")
                    else:
                        error_holder_column2.error(f"Please upload a {lang_name} file.")
                        error_holder_column1.error("Please upload an English file.")

                        
                    
                if st.session_state.both_excel_file_path is not None:
                    st.session_state.both_download_filename_tab4 = os.path.basename(st.session_state.both_excel_file_path)

                if st.session_state.both_excel_file_path:
                    st.success("処理が完了しました。以下のリンクからファイルをダウンロードできます。")
                    with open(st.session_state.both_excel_file_path, 'rb') as f:
                        st.download_button(
                            label=f"{st.session_state.both_download_filename_tab4}をダウンロード",
                            data=f,
                            file_name=st.session_state.both_download_filename_tab4,
                            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                        )
                    #st.dataframe(st.session_state.both_df, width=2000, hide_index=True)
                    st.table(st.session_state.both_df)

            elif option == 'Only English':
                if do_exe_en:
                    if st.session_state.english_path_only:
                        st.session_state.en_excel_file_path, st.session_state.en_df = moz.create_excel_from_srt(english_path=st.session_state.english_path_only,replace_word=st.session_state.replace_word)
                        if st.session_state.en_excel_file_path==None :
                            st.error("ファイル処理中にエラーが発生しました")
                    else:
                        error_holder_only_en.error("Please upload an English file.")
                    if st.session_state.en_df is not None:                        
                        st.session_state.en_download_filename_tab4 = os.path.basename(st.session_state.en_excel_file_path)
                        
                        
                
                #else:
                    #st.error("ファイルをアップロードしてください")

                if st.session_state.en_excel_file_path:
                    st.success("処理が完了しました。以下のリンクからファイルをダウンロードできます。")
                    with open(st.session_state.en_excel_file_path, 'rb') as f:
                        st.download_button(
                            label=f"{st.session_state.en_download_filename_tab4}をダウンロード",
                            data=f,
                            file_name=st.session_state.en_download_filename_tab4,
                            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                        )
                    #st.dataframe(st.session_state.en_df, width=2000, hide_index=True)
                    st.table(st.session_state.en_df)

            elif option == f'Only {lang_name}':
                
                if do_exe_ja:
                    if st.session_state.japanese_path_only:
                        st.session_state.ja_excel_file_path, st.session_state.ja_df = moz.create_excel_from_srt(japanese_path=st.session_state.japanese_path_only)
                        if st.session_state.ja_excel_file_path==None :
                            st.error("ファイル処理中にエラーが発生しました")
                    else:
                        error_holder_only_ja.error(f"Please upload a {lang_name} file.")
                    if st.session_state.ja_df is not None:         
                        #st.success("処理が完了しました。以下のリンクからファイルをダウンロードできます。")                                   
                        st.session_state.ja_download_filename_tab4 = os.path.basename(st.session_state.ja_excel_file_path)
                        
                
                
                #else:
                    #st.error("ファイルをアップロードしてください")
                if st.session_state.ja_excel_file_path:
                    st.success("処理が完了しました。以下のリンクからファイルをダウンロードできます。")
                    with open(st.session_state.ja_excel_file_path, 'rb') as f:
                        st.download_button(
                            label=f"{st.session_state.ja_download_filename_tab4}をダウンロード",
                            data=f,
                            file_name=st.session_state.ja_download_filename_tab4,
                            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                        )
                    #st.dataframe(st.session_state.ja_df, width=2000, hide_index=True)
                    st.table(st.session_state.ja_df)

            # print(f"st.session_state.select_dot_result:{st.session_state.select_dot_result}")
            # print(f'st.session_state.dot_key:{st.session_state.dot_key}')   

            
                 

    elif st.session_state.current_tab == 'whisperファイルの復活①': #☆reversal1
        # print(f"st.session_state.ja_split:{st.session_state.ja_split}")
        # print(f"st.session_state.ja_split:{st.session_state.ja_split_key}")
        with st.container():
            #load_multi_without_model_option()
            
                 
            st.markdown("<div class='tab_title'>敗者復活 - Json & Srt -</div>", unsafe_allow_html=True)
            # モデル選択ラジオボタンの設定

            # ラジオボタンを表示
            
                
            st.session_state.selected_model = st.toggle(
                "largeモデルを使う",
                #index=('base', 'large').index(st.session_state.model_option_func),
                key='model_option_key',  
                on_change=save_model_option
                
            )
            
            #save_model_option()

            # 選択されたモデルを手動でセッションステートに保存
        
        
                

            # JSONファイルとSRTファイルの複数アップロードウィジェット
            L1,L2=st.columns([1,1])
            with L1:
                uploaded_json_files = st.file_uploader("★ JSONファイルをアップロードしてください", type=['json'], key=f'file_uploader_tab6_1_{st.session_state.uploader_tab6_1_key}', accept_multiple_files=True)
                t6_json_errorholoder=st.empty()
                if uploaded_json_files:

                    timestamp_patch = datetime.now().strftime("%Y%m%d%H%M%S")
                    temp_dir = os.path.join(tempfile.gettempdir(), f"tempdir_{timestamp_patch}")
                    os.makedirs(temp_dir, exist_ok=True)    
                    st.session_state.t6_jsons,st.session_state.t6_jsnamelist=upstock(st.session_state.t6_jsons,st.session_state.t6_jsnamelist,uploaded_json_files,temp_dir)
                    #print(st.session_state.t6_jsons)
                    #print(st.session_state.t6_jsnamelist)
                    

                if st.session_state.t6_jsons:
                    if len(st.session_state.t6_jsons) < 4:
                        for file in st.session_state.t6_jsons:
                            st.warning(f"{os.path.basename(file)}がアップロードされました。")
                    else:    
                        st.warning(f"{len(st.session_state.t6_jsons)}つのファイルがアップロードされました。")

            with L2:
                uploaded_srt_files = st.file_uploader("★ SRTファイルをアップロードしてください", type=['srt'], key=f'file_uploader_tab6_2_{st.session_state.uploader_tab6_2_key}', accept_multiple_files=True)
                t6_srt_errorholoder=st.empty()
                if uploaded_srt_files:

                    timestamp_patch = datetime.now().strftime("%Y%m%d%H%M%S")
                    temp_dir = os.path.join(tempfile.gettempdir(), f"tempdir_{timestamp_patch}")
                    os.makedirs(temp_dir, exist_ok=True)

                    st.session_state.t6_srts,st.session_state.t6_srtnamelist = upstock(st.session_state.t6_srts,st.session_state.t6_srtnamelist,uploaded_srt_files,temp_dir)
    
                
                if st.session_state.t6_srts:
                    if len(st.session_state.t6_srts) < 4:
                        for file in st.session_state.t6_srts:
                            st.warning(f"{os.path.basename(file)}がアップロードされました。")
                    else:
                        st.warning(f"{len(st.session_state.t6_srts)}つのファイルがアップロードされました。")

            K1,K3,K4=st.columns([2,1,1])
            with K1:
                do_exe_t6=st.button("処理実行", key="execute_tab9",use_container_width=True)

            with K3:
                if st.button("クリア", key="clear_tab6",use_container_width=True):
                    moz.clear_session_state('whisperファイルの復活①')        
            with K4:
                if st.button("終了", key="exit_tab6",use_container_width=True):
                    os.kill(os.getpid(), signal.SIGTERM)
            
            if do_exe_t6:
                if st.session_state.t6_jsons and st.session_state.t6_srts:
                                   
                    srt_output_files, txt_output_files = moz_t9.process_multiple_sets(
                        st.session_state.t6_jsons, 
                        st.session_state.t6_srts, 
                        st.session_state.selected_model,
                        st.session_state.replace_word
                    )

                    # SRTファイルとTXTファイルのパスを保存
                    st.session_state['tab9_output_srt_files'] = srt_output_files
                    st.session_state['tab9_output_txt_files'] = txt_output_files
                    st.session_state['tab9_files_ready'] = True
                
                elif st.session_state.t6_jsons:
                    t6_srt_errorholoder.error("srtファイルをアップロードしてください。")
                elif st.session_state.t6_srts:
                    t6_json_errorholoder.error("jsonファイルをアップロードしてください。")
                else:
                    t6_srt_errorholoder.error("srtファイルをアップロードしてください。")
                    t6_json_errorholoder.error("jsonファイルをアップロードしてください。")
            # ダウンロードボタンの表示
            if st.session_state.get('tab9_files_ready', False) and st.session_state['tab9_output_srt_files']:
                st.success("処理が完了しました。以下のリンクからファイルをダウンロードできます。")

                # SRTファイルの処理
                if 'tab9_output_srt_files' in st.session_state:
                    srt_output_file_paths = st.session_state['tab9_output_srt_files']

                    if isinstance(srt_output_file_paths, list):
                        # リストの場合（単一ファイル）
                        for srt_output_file_path in srt_output_file_paths:
                            if os.path.exists(srt_output_file_path):
                                with open(srt_output_file_path, "rb") as srt_file:
                                    st.download_button(
                                        label=f"{os.path.basename(srt_output_file_path)}をダウンロード",
                                        data=srt_file,
                                        file_name=os.path.basename(srt_output_file_path),
                                        key=f"tab9_output_srt_download_{os.path.basename(srt_output_file_path)}"
                                    )
                    else:
                        # ZIPファイルの場合
                        if os.path.exists(srt_output_file_paths):
                            with open(srt_output_file_paths, "rb") as srt_file:
                                st.download_button(
                                    label=f"{os.path.basename(srt_output_file_paths)}をダウンロード",
                                    data=srt_file,
                                    file_name=os.path.basename(srt_output_file_paths),
                                    key=f"tab9_output_srt_download"
                                )

                # TXTファイルの処理
                if 'tab9_output_txt_files' in st.session_state:
                    txt_output_file_paths = st.session_state['tab9_output_txt_files']

                    if isinstance(txt_output_file_paths, list):
                        # リストの場合（単一ファイル）
                        for txt_output_file_path in txt_output_file_paths:
                            if os.path.exists(txt_output_file_path):
                                with open(txt_output_file_path, "rb") as txt_file:
                                    st.download_button(
                                        label=f"{os.path.basename(txt_output_file_path)}をダウンロード",
                                        data=txt_file,
                                        file_name=os.path.basename(txt_output_file_path),
                                        key=f"tab9_output_txt_download_{os.path.basename(txt_output_file_path)}"
                                    )
                    else:
                        # ZIPファイルの場合
                        if os.path.exists(txt_output_file_paths):
                            with open(txt_output_file_paths, "rb") as txt_file:
                                st.download_button(
                                    label=f"{os.path.basename(txt_output_file_paths)}をダウンロード",
                                    data=txt_file,
                                    file_name=os.path.basename(txt_output_file_paths),
                                    key=f"tab9_output_txt_download"
                                    )

            # print(f"st.session_state.select_dot_result:{st.session_state.select_dot_result}")
            # print(f'st.session_state.dot_key:{st.session_state.dot_key}')

            
                         
    elif st.session_state.current_tab=="whisperファイルの復活②":#☆reversal2
        # print(f"st.session_state.ja_split:{st.session_state.ja_split}")
        # print(f"st.session_state.ja_split:{st.session_state.ja_split_key}")
        with st.container():
            #load_multi_without_model_option2()
            
                 


            st.markdown("<div class='tab_title'>敗者復活 - Only Json -</div>", unsafe_allow_html=True)
            st.session_state.selected_model2 = st.toggle(
                "largeモデルを使う",
                #index=('base', 'large').index(st.session_state.model_option_func),
                key='model_option_key2',  
                on_change=save_model_option2          
            )
            st.session_state.deepall = st.toggle(
                "ピリオドをすべて付けなおす",
                #index=('base', 'large').index(st.session_state.model_option_func),
                key='deepall_key',  
                on_change=save_deepall          
            )
            t11_uploaded_files = st.file_uploader("★ JSONファイルをアップロードしてください。", type="json",key=f'file_uploader_tab7_{st.session_state.uploader_tab7_key}', accept_multiple_files=True)
            t11_errorholoder=st.empty()
            if t11_uploaded_files:

                timestamp_patch = datetime.now().strftime("%Y%m%d%H%M%S")
                temp_dir = os.path.join(tempfile.gettempdir(), f"tempdir_{timestamp_patch}")
                os.makedirs(temp_dir, exist_ok=True)    
                st.session_state.t11_jsons,st.session_state.t11_namelist=upstock(st.session_state.t11_jsons,st.session_state.t11_namelist,t11_uploaded_files,temp_dir)
            

            if st.session_state.t11_jsons:
                if len(st.session_state.t11_jsons) < 4:
                    for file in st.session_state.t11_jsons:
                        st.warning(f"{os.path.basename(file)}がアップロードされました。")
                else:
                    st.warning(f"{len(st.session_state.t11_jsons)}つのファイルがアップロードされました。")


            M1,M3,M4=st.columns([2,1,1])
            with M1:
                do_exe_t11= st.button("処理実行",key="t11_exe",use_container_width=True)
             
                                

            with M3:
                if st.button("クリア", key="clear_tab11",use_container_width=True):
                    moz.clear_session_state('whisperファイルの復活②')
            with M4:
                if st.button("終了", key="exit_tab11",use_container_width=True):
                    os.kill(os.getpid(), signal.SIGTERM)
            
            
            if do_exe_t11:
                if st.session_state.t11_jsons:
                    st.session_state.t11_srt_files,st.session_state.skipped_files=js.multi_json_operator(st.session_state.t11_jsons,st.session_state.replace_word,st.session_state.selected_model2)
                    
                else:
                    t11_errorholoder.error("ファイルをアップロードしてください。")        

            if st.session_state.t11_srt_files:
                if st.session_state.skipped_files:
                    st.success(f"残り{len(st.session_state.t11_jsons)-len(st.session_state.skipped_files)}つのファイル処理が完了しました。以下のリンクからダウンロードできます。")
                    t11_srts=st.session_state.t11_srt_files
                    for idx,t11_srt_path in enumerate(t11_srts):
                        t11_srt_name=os.path.basename(t11_srt_path)
                        with open(t11_srt_path, "rb") as f:
                            st.download_button(label=f"{t11_srt_name}をダウンロード", data=f, file_name=t11_srt_name, key=f"t11_downloader_{idx}")
                    
                    st.info("以下のファイルがスキップされました。srtファイルとjsonファイルからの再編をお試しください。")
                    for skipped_file in st.session_state.skipped_files:
                        st.write(f"・{skipped_file}")
                        
                else:
                    st.success("処理が完了しました。以下のリンクからファイルをダウンロードできます。")
                
                    t11_srts=st.session_state.t11_srt_files
                    for idx,t11_srt_path in enumerate(t11_srts):
                        t11_srt_name=os.path.basename(t11_srt_path)
                        with open(t11_srt_path, "rb") as f:
                            st.download_button(label=f"{t11_srt_name}をダウンロード", data=f, file_name=t11_srt_name, key=f"t11_downloader_{idx}")
        
            elif st.session_state.skipped_files:
                st.info("以下のファイルの処理がスキップされました。jsonファイルとsrtファイルからの再編をお試しください。")
                for skipped_file in st.session_state.skipped_files:
                    st.write(f"・{skipped_file}")


            # print(f"st.session_state.select_dot_result:{st.session_state.select_dot_result}")
            # print(f'st.session_state.dot_key:{st.session_state.dot_key}')

            
                 

    elif st.session_state.current_tab == "YT付属字幕の再編":#☆yt
        # print(f"st.session_state.ja_split:{st.session_state.ja_split}")
        # print(f"st.session_state.ja_split:{st.session_state.ja_split_key}")
        with st.container():
            #load_multi_without_model_option3()
            
                 
            #print(f'yt_srts:{st.session_state.yt_srts}')
                
            st.markdown("<div class='tab_title'>ピリオドがないSRT字幕の再編</div>", unsafe_allow_html=True)
            st.session_state.selected_model3 = st.toggle(
                "largeモデルを使う",
                #index=('base', 'large').index(st.session_state.model_option_func),
                key='model_option_key3',  
                on_change=save_model_option3)
            
            uploaded_yt_srt_files = st.file_uploader("★ SRTファイルをアップロードしてください", type="srt", key=f'file_uploader_tab8_{st.session_state.uploader_tab8_key}', accept_multiple_files=True)
            yt_errorholoder=st.empty()
            # 実行ボタンを追加
            if uploaded_yt_srt_files:

                timestamp_patch = datetime.now().strftime("%Y%m%d%H%M%S")
                temp_dir = os.path.join(tempfile.gettempdir(), f"tempdir_{timestamp_patch}")
                os.makedirs(temp_dir, exist_ok=True)    
                st.session_state.yt_srts,st.session_state.yt_namelist=upstock(st.session_state.yt_srts,st.session_state.yt_namelist,uploaded_yt_srt_files,temp_dir)


            if st.session_state.yt_srts:
                if len(st.session_state.yt_srts) < 4:
                    for file in st.session_state.yt_srts:
                        st.warning(f"{os.path.basename(file)}がアップロードされました。")
                else:
                    st.warning(f"{len(st.session_state.yt_srts)}つのファイルをアップロードしました。")

            N1,N3,N4=st.columns([2,1,1])
            with N1:
                execute_button = st.button("処理実行", key="yt_execute_button",use_container_width=True)
            with N3:
                if st.button("クリア", key="clear_tab7",use_container_width=True):
                    moz.clear_session_state("YT付属字幕の再編")

            with N4:
                if st.button("終了", key="exit_tab7",use_container_width=True):
                    os.kill(os.getpid(), signal.SIGTERM)

            if execute_button:
                if st.session_state.yt_srts:
                    srt_output_files, txt_output_files = moz_t10.process_multi_files(st.session_state.yt_srts,st.session_state.selected_model3,replace_word=st.session_state.replace_word,)
                    st.session_state['yt_output_srt'] = srt_output_files
                    st.session_state['yt_output_txt'] = txt_output_files
                    st.session_state['download_ready'] = True
                else:
                    yt_errorholoder.error("ファイルをアップロードしてください。")        

            # ダウンロードボタンを表示
            if st.session_state.get('download_ready', False):
                st.success("処理が完了しました。以下のリンクからファイルをダウンロードできます。")

                with open(st.session_state['yt_output_srt'], "rb") as file:
                    st.download_button(
                        label=f"{os.path.basename(st.session_state['yt_output_srt'])}をダウンロード",
                        data=file,
                        file_name=os.path.basename(st.session_state['yt_output_srt']),
                        key="yt_srt_download"
                    )

                with open(st.session_state['yt_output_txt'], "rb") as file:
                    st.download_button(
                        label=f"{os.path.basename(st.session_state['yt_output_txt'])}をダウンロード",
                        data=file,
                        file_name=os.path.basename(st.session_state['yt_output_txt']),
                        key="yt_txt_download")
            # print(f"st.session_state.select_dot_result:{st.session_state.select_dot_result}")
            # print(f'st.session_state.dot_key:{st.session_state.dot_key}')

            
                 
    elif st.session_state.current_tab == '日本語srt,vttの句読点分割': #☆ja_split
        # print(f"st.session_state.ja_split:{st.session_state.ja_split}")
        # print(f"st.session_state.ja_split:{st.session_state.ja_split_key}")
        with st.container():
            
                 
            #load_multi()
            #print(f'kuten_files:{st.session_state.t5_kuten_files}')
            st.markdown("<div class='tab_title'>日本語SRT/VTTの句点・読点分割</div>", unsafe_allow_html=True)
            
            t5_uploaded_files = st.file_uploader("★ 日本語のsrt,vttファイルをアップロードしてください", type=['srt', 'vtt'], accept_multiple_files=True, key=f'file_uploader_tab5_{st.session_state.uploader_tab5_key}')
            t5_errorholoder=st.empty()
            if t5_uploaded_files:
                timestamp_patch = datetime.now().strftime("%Y%m%d%H%M%S")
                temp_dir = os.path.join(tempfile.gettempdir(), f"tempdir_{timestamp_patch}")
                os.makedirs(temp_dir, exist_ok=True)

                st.session_state.t5_kuten_files,st.session_state.t5_filenames=upstock(st.session_state.t5_kuten_files,st.session_state.t5_filenames,t5_uploaded_files,temp_dir)

                

            if st.session_state.t5_kuten_files:
                if len(st.session_state.t5_kuten_files) < 4:
                    for file in st.session_state.t5_kuten_files:
                        st.warning(f"{os.path.basename(file)}がアップロードされました。")
                else:
                    st.warning(f"{len(st.session_state.t5_filenames)}つのファイルがアップロードされました。")
            J1,J3,J4 = st.columns([2,1,1])
            with J1:
                do_exe_t5=st.button("処理実行", key="t5_exe",use_container_width=True)    

            with J3:
                if st.button("クリア", key="clear_tab5",use_container_width=True):
                    moz.clear_session_state(tab='日本語srt,vttの句読点分割')        

            with J4:
                if st.button("終了", key="exit_tab5",use_container_width=True):
                    os.kill(os.getpid(), signal.SIGTERM)

            
            if do_exe_t5:
                if st.session_state.t5_kuten_files:
                    lang_tail=extract_short_name(st.session_state.language_result)
                    if lang_tail=='ja' or lang_tail=='zh':
                        results = moz_t8.process_files(st.session_state.t5_kuten_files,False)
                    else:
                        results = period.process_files(st.session_state.t5_kuten_files,False)
                    st.session_state['results'] = results
                else:
                    t5_errorholoder.error("ファイルをアップロードしてください。")       

            if 'results' in st.session_state and st.session_state['results']:
                st.success("処理が完了しました。以下のリンクからファイルをダウンロードできます。")
                for idx,result in enumerate(st.session_state['results']):
                    with open(result, "rb") as file:
                        st.download_button(
                            label=f"{os.path.basename(result)} をダウンロード",
                            data=file,
                            file_name=f'{os.path.basename(result)}',
                            key=f"t5_dl_{idx}"
                        )
            
                 

           # print(f"st.session_state.select_dot_result:{st.session_state.select_dot_result}")
            # print(f'st.session_state.dot_key:{st.session_state.dot_key}')



    elif st.session_state.current_tab=="その他":
        # print(f"st.session_state.ja_split:{st.session_state.ja_split}")
        # print(f"st.session_state.ja_split:{st.session_state.ja_split_key}")
        
             
        st.markdown("<div class='tab_title'>その他</div>", unsafe_allow_html=True)
        with st.container():
            if 'alc_namelist' not in st.session_state:
                st.session_state.alc_namelist=[]

            if 'alc_inputs' not in st.session_state:
                st.session_state.alc_inputs = []

            if 'alc_processed_file_paths' not in st.session_state:
                st.session_state.alc_processed_file_paths=[]

            if 'alc_uploader_key' not in st.session_state:
                st.session_state.alc_uploader_key=0




            if 'srtvtt_namelist' not in st.session_state:
                st.session_state.srtvtt_namelist=[]

            if 'srtvtt_inputs' not in st.session_state:
                st.session_state.srtvtt_inputs = []

            if 'srtvtt_processed_file_paths' not in st.session_state:
                st.session_state.srtvtt_processed_file_paths=[]

            if 'srtvtt_uploader_key' not in st.session_state:
                st.session_state.srtvtt_uploader_key=0


            if 'rp_only_uploader_key' not in st.session_state:
                st.session_state.rp_only_uploader_key=0
            
            if 'rp_only_uploaded_files' not in st.session_state:
                st.session_state.rp_only_uploaded_files=[]
            
            if 'rp_only_filenames' not in st.session_state:
                st.session_state.rp_only_filenames=[]
            
            if 'rp_only_otfiles' not in st.session_state:
                st.session_state.rp_only_otfiles = []


  

            # タイトル
            with st.expander("☆ テキストに改行を入れる(テキストエリアでの作業です)"):
                with st.container():
                    st.markdown("<div class='second_tab_title'>テキストの改行挿入</div>", unsafe_allow_html=True)
                    st.markdown("改行の無い文章をピリオドや句点で区切ります。srt,vttは別のタブをお使いください。")

                    # テキスト入力
                    input_text = st.text_area("テキストを入力してください",key="alc1")

                    # 句点、クエスチョンマーク、ビックリマークで改行を入れる処理
                    left,right=st.columns([1,1])
                    with left:
                        alc_do_exe=st.button("句点改行",use_container_width=True,key="alc_do_exe1")
                    with right:
                        alc_clear1=st.button("クリア",use_container_width=True,key="alc_clear1")
                        if alc_clear1:
                            clear_c()

                    formatted_text=""
                    if input_text:
                        # 句点、クエスチョンマーク、ビックリマークの後に改行を追加
                        if alc_do_exe:
                            
                            if st.session_state.select_dot_result:
                                
                                data_folder = "/content/my_app"
                                with open(os.path.join(data_folder,st.session_state.select_dot_result), newline='',encoding='utf-8') as dot_csvfile:
                                    reader = csv.reader(dot_csvfile)
                                    next(reader)
                                    dot_replacements = [(row[0],row[1]) for row in reader]
                                
                                
                                for dot_original, dot_replacement in dot_replacements:
                                    r_dot_original=re.escape(dot_original)
                                    dot_new_original = rf"\b{r_dot_original}"
                                    input_text = re.sub(dot_new_original, dot_replacement, input_text)  
                            input_text=t9.protect_inner_dots(input_text)
                            input_text = input_text.replace("。」","」。").replace("?」","」?").replace("？」","」？")                          
                            formatted_text = input_text.replace("。", "。\n").replace("?", "?\n").replace("？","？\n").replace("!", "!\n").replace("\n\n","\n")
                            formatted_text =formatted_text.replace("」。","。」").replace("」?","?」").replace("」？","？」")    
                            formatted_text = formatted_text.replace(".",".\n").replace("\n\n","\n")
                            formatted_text = formatted_text.replace("[dot]",".")
                        
                        # 結果を表示
                    st.text_area("改行後のテキスト", formatted_text, height=300,key="alc1_out")

            with st.expander("☆ テキストの改行を取り除く(テキストエリアでの作業です)"):
                with st.container():
                    st.markdown("<div class='second_tab_title'>テキストの改行除去</div>", unsafe_allow_html=True)
                    st.markdown("改行を削除します。")
                    input_text2 = st.text_area("テキストを入力してください",key="alc2")
                    left,right=st.columns([1,1])
                    with left:
                        alc_do_exe2 =st.button("改行削除",use_container_width=True,key="alc_do_exe2")
                    with right:
                        alc_clear2=st.button("クリア",use_container_width=True,key="alc_clear2")
                        if alc_clear2:
                            clear_d()


                    formatted_text2=""
                
                    if input_text2:
                        if alc_do_exe2:
                            formatted_text2=input_text2.replace("\n"," ").replace("。 ","。")
                    st.text_area("結合後のテキスト", formatted_text2, height=300,key="alc2_out")

            with st.expander("☆ SRT,VTTからタイムスタンプを除去(テキストエリアでの作業です)"):
                
                with st.container():
                    st.markdown("<div class='second_tab_title'>SRT,VTTからNRテキストへ変換</div>", unsafe_allow_html=True)
                    st.markdown("IDとタイムスタンプを除去して、改行なしの文章にします。")
                    input_srt = st.text_area("SRT,VTTの内容を貼り付けてください。",key="alc_srt")
                    left,right=st.columns([1,1])
                    with left:
                        alc_srt_do_exe =st.button("タイムスタンプ除去",use_container_width=True,key="alc_srt_do_exe")
                    with right:
                        alc_clears2=st.button("クリア",use_container_width=True,key="alc_srt_clear")
                        if alc_clears2:
                            clear_e()


                    deleted_srt=""
                
                    if input_srt:
                        if alc_srt_do_exe:
                            delete_webvtt=moz_t7.webvtt_remover(input_srt)
                            deleted_srt = re.sub(r'\d{1,4}\n\d{1,2}:\d{2}:\d{2}[\.,]\d{1,3}\s-->\s\d{1,2}:\d{2}:\d{2}[\.,]\d{1,3}\n', '', delete_webvtt)
                            deleted_srt = deleted_srt.replace("\n"," ").replace("  "," ")
                    st.text_area("結合後のテキスト", deleted_srt, height=300,key="alc_srt_out")

  



            # Streamlit部分
            with st.expander("☆ IDのないSRT,VTTにIDを付ける"):
                st.markdown("<div class='second_tab_title'>IDのないSRT,VTTにIDを付ける</div>", unsafe_allow_html=True)
                st.markdown("このアプリはIDのないSRT,VTTに対応していないので、IDのないSRT,VTTにIDを付けます。")
                # アップロードされたファイルを一時保存し、そのパスをセッションに保存（重複保存を避ける）
                alc_uploaded_files = st.file_uploader("SRTまたはVTTファイルをアップロード", type=["srt", "vtt"], accept_multiple_files=True,key=f"alc_uploader_{st.session_state.alc_uploader_key}")
                alc_msg=st.empty()
                if alc_uploaded_files:
                    
                    timestamp_patch = datetime.now().strftime("%Y%m%d%H%M%S")
                    temp_dir = os.path.join(tempfile.gettempdir(), f"tempdir_{timestamp_patch}")
                    os.makedirs(temp_dir, exist_ok=True)

                    st.session_state.alc_inputs,st.session_state.alc_namelist=upstock(st.session_state.alc_inputs,st.session_state.alc_namelist,alc_uploaded_files,temp_dir)
                    

                    if st.session_state.alc_inputs:
                        if len(st.session_state.alc_inputs) < 4:
                            for file in st.session_state.alc_inputs:
                                st.warning(f"{os.path.basename(file)}がアップロードされました。")
                        else:
                            st.warning(f"{len(st.session_state.alc_inputs)}つのファイルがアップロードされました。")

                # 処理実行ボタン
                O1,O2=st.columns([1,1])
                with O1:
                    alc3_exe=st.button("処理を実行",use_container_width=True,key="alc3_exe")
                with O2:
                    if st.button("クリア",use_container_width=True,key="alc3_clearanse"):
                        clear_f()
                
                        st.rerun()
                if alc3_exe:
                    if st.session_state.alc_inputs:
               
                            st.session_state.alc_processed_file_paths = process_subtitle(st.session_state.alc_inputs)
                    else:
                        alc_msg.error("ファイルをアップロードしてください。")

                if st.session_state.alc_processed_file_paths:
                            
                    # 処理済みファイルのダウンロードボタンを表示
                    for idx,fp in enumerate(st.session_state.alc_processed_file_paths):
                        with open(fp, 'rb') as processed_file:
                            st.download_button(
                                label=f"{os.path.basename(fp)} をダウンロード",
                                data=processed_file,
                                file_name=f"{os.path.basename(fp)}",  # 処理されたファイル名を指定
                                mime='text/plain',
                                key=f"sample_{idx}"
                                )

            with st.expander("☆ SRT↔VTT変換"):
                st.markdown("<div class='second_tab_title'>SRT,VTT変換</div>", unsafe_allow_html=True)
                st.markdown("ファイル形式をSRTはVTTへ、VTTはSRTへ変換します。")
                # アップロードされたファイルを一時保存し、そのパスをセッションに保存（重複保存を避ける）
                srtvtt_uploaded_files = st.file_uploader("SRTまたはVTTファイルをアップロード", type=["srt", "vtt"], accept_multiple_files=True,key=f"srtvtt_uploader_{st.session_state.srtvtt_uploader_key}")
                srtvtt_msg=st.empty()
                if srtvtt_uploaded_files:
                    
                    timestamp_patch = datetime.now().strftime("%Y%m%d%H%M%S")
                    temp_dir = os.path.join(tempfile.gettempdir(), f"tempdir_{timestamp_patch}")
                    os.makedirs(temp_dir, exist_ok=True)

                    st.session_state.srtvtt_inputs,st.session_state.srtvtt_namelist=upstock(st.session_state.srtvtt_inputs,st.session_state.srtvtt_namelist,srtvtt_uploaded_files,temp_dir)
                    

                    if st.session_state.srtvtt_inputs:
                        if len(st.session_state.srtvtt_inputs) < 4:
                            for file in st.session_state.srtvtt_inputs:
                                st.warning(f"{os.path.basename(file)}がアップロードされました。")
                        else:
                            st.warning(f"{len(st.session_state.srtvtt_inputs)}つのファイルがアップロードされました。")

                # 処理実行ボタン
                O1,O2=st.columns([1,1])
                with O1:
                    srtvtt_exe=st.button("処理を実行",use_container_width=True,key="srtvtt_exe")
                with O2:
                    if st.button("クリア",use_container_width=True,key="srtvtt_clearanse"):
                        clear_g()
                
                        st.rerun()
                if srtvtt_exe:
                    if st.session_state.srtvtt_inputs:
               
                            st.session_state.srtvtt_processed_file_paths = convert_files(st.session_state.srtvtt_inputs)
                    else:
                        srtvtt_msg.error("ファイルをアップロードしてください。")

                if st.session_state.srtvtt_processed_file_paths:
                            
                    # 処理済みファイルのダウンロードボタンを表示
                    for idx,fp in enumerate(st.session_state.srtvtt_processed_file_paths):
                        with open(fp, 'rb') as processed_file:
                            st.download_button(
                                label=f"{os.path.basename(fp)} をダウンロード",
                                data=processed_file,
                                file_name=f"{os.path.basename(fp)}",  # 処理されたファイル名を指定
                                mime='text/plain',
                                key=f"sample_{fp}_{idx}")

            with st.expander("☆ SRT,VTT,TXTの単語置き換え"):
                st.markdown("<div class='second_tab_title'>SRT,VTT,TXTの単語置き換え</div>", unsafe_allow_html=True)
                st.markdown("選択されている単語帳に基づいて単語の置き換えのみを行います。toggleボタンが無効でも置き換えます。")
                rp_only_uploader=st.file_uploader("★ SRT,VTT,TXTファイルをアップロードしてください。", type=["srt", "vtt","txt"], accept_multiple_files=True,key=f"rp_only_uploader_{st.session_state.rp_only_uploader_key}")
                rp_only_errorholoder=st.empty()
                if rp_only_uploader:
                    timestamp_patch = datetime.now().strftime("%Y%m%d%H%M%S")
                    temp_dir = os.path.join(tempfile.gettempdir(), f"tempdir_{timestamp_patch}")
                    os.makedirs(temp_dir, exist_ok=True)

                    st.session_state.rp_only_uploaded_files,st.session_state.rp_only_filenames=upstock(st.session_state.rp_only_uploaded_files,st.session_state.rp_only_filenames,rp_only_uploader,temp_dir)

                if st.session_state.rp_only_uploaded_files:
                    if len(st.session_state.rp_only_uploaded_files) < 4:
                        for file in st.session_state.rp_only_uploaded_files:
                            st.warning(f"{os.path.basename(file)}がアップロードされました。")
                    else:
                        st.warning(f"{len(st.session_state.rp_only_filenames)}つのファイルがアップロードされました。")
                
                s1,s3,s4 = st.columns([2,1,1])
                with s1 :
                    rp_exe=st.button("置き換え実行",key="rp_only_execute",use_container_width=True)
                
                with s3:
                    if st.button("クリア",key="rp_only_clear_buttton",use_container_width=True):
                        clear_h()

                with s4 :
                    if st.button("終了", key="rp_only_exit",use_container_width=True):
                        os.kill(os.getpid(), signal.SIGTERM)
                
                if rp_exe:
                    if st.session_state.rp_only_uploaded_files:
                        
                        data_folder = "/content/my_app"
                        st.session_state.rp_only_otfiles=only_replace_function(st.session_state.rp_only_uploaded_files,os.path.join(data_folder,st.session_state.select_rp_result))
                    else:
                        rp_only_errorholoder.error("ファイルをアップロードしてください。")
                
                #print(st.session_state.rp_only_otfiles)
                if 'rp_only_otfiles' in st.session_state and st.session_state.rp_only_otfiles:
                    st.success("処理が完了しました。以下のリンクからファイルをダウンロードできます。")

                    for idx,only_otfile in enumerate(st.session_state.rp_only_otfiles):
                        with open(only_otfile,"rb") as file:
                            st.download_button(
                            label=f"{os.path.basename(only_otfile)}をダウンロード",
                            data=file,
                            file_name=f'{os.path.basename(only_otfile)}',
                            key=f'rp_only_dl_{idx}'
                            )
            
            with st.expander("☆ 配布字幕の再編：一括処理版"):



                                
                t1_new_keys=["new_t1_input_filenames","new_t1_input_paths","new_t1_ot_excels","new_t1_ot_words","new_t1_ot_srts",]
                for key in t1_new_keys:
                    if key not in st.session_state:
                        st.session_state[key]=[]    
                
                if 'uploader_new_key' not in st.session_state:
                    st.session_state.uploader_new_key = 0


                st.markdown("<div class='second_tab_title'>配布字幕の再編　-　一括処理版　-</div>", unsafe_allow_html=True)
                new_t1_uploaded_files = st.file_uploader("★ ファイルをアップロードしてください", type=['srt', 'vtt'], key=f"new_file_uploader_tab1_{st.session_state.uploader_new_key}",accept_multiple_files=True)
                editor_erroholder=st.empty()
                if new_t1_uploaded_files:
                    timestamp_patch = datetime.now().strftime("%Y%m%d%H%M%S")
                    temp_dir = os.path.join(tempfile.gettempdir(), f"tempdir_{timestamp_patch}")
                    os.makedirs(temp_dir, exist_ok=True)
                    st.session_state.new_t1_input_paths,st.session_state.new_t1_input_filenames=upstock(st.session_state.new_t1_input_paths,st.session_state.new_t1_input_filenames,new_t1_uploaded_files,temp_dir)
                    
                if st.session_state.new_t1_input_paths:
                    if len(st.session_state.new_t1_input_paths) < 4:
                        for file in st.session_state.new_t1_input_paths:
                            st.warning(f"{os.path.basename(file)}がアップロードされました。")
                    else:
                        st.warning(f"{len(st.session_state.new_t1_input_filenames)}つのファイルがアップロードされました。")



                A1,A3,A4=st.columns([2,1,1])
                with A1:
                    new_do_periods =st.button('ピリオドによる補正',use_container_width=True,key="new_periods_widget")
                        
                with A3:
                    if st.button("クリア",use_container_width=True,key="new_clear_tab1_widget"):
                        clear_i()
                        

                with A4:     
                    if st.button("終了",use_container_width=True,key="new_exit_tab1_widget"):
                        os.kill(os.getpid(), signal.SIGTERM)

                if new_do_periods:
                    if st.session_state.new_t1_input_paths:
                        #st.session_state.output_html_tab1, st.session_state.output_files_tab1, st.session_state.output_file_tab1, st.session_state.t7_df = moz.process_file(st.session_state.t1_input_paths,st.session_state.replace_word)
                        st.session_state.new_t1_ot_excels,st.session_state.new_t1_ot_words,st.session_state.new_t1_ot_srts = moz.new_process_file(st.session_state.new_t1_input_paths,st.session_state.replace_word)
                    
                    else:st.error("ファイルをアップロードしてください。")

            
                            
                if st.session_state.new_t1_ot_excels:
                    st.success("処理が完了しました。以下のリンクからファイルをダウンロードできます。")
                    for idx,file in enumerate(st.session_state.new_t1_ot_excels+st.session_state.new_t1_ot_words+st.session_state.new_t1_ot_srts):
                        original_filename = os.path.basename(file)
                        with open(file, "rb") as f:
                            st.download_button(label=f"{original_filename}をダウンロード", data=f, file_name=original_filename, key=f"new_download_ja_button_{idx}")
            
                 
    elif st.session_state.current_tab=="翻訳先言語":
        # print(f"st.session_state.ja_split:{st.session_state.ja_split}")
        # print(f"st.session_state.ja_split:{st.session_state.ja_split_key}")
        
             
        st.markdown("<div class='tab_title'>変換先言語</div>", unsafe_allow_html=True)
        with st.container():

            # "。","、","?"("？"),"!"("！"),区切り,半角スペースなし。
            language_groupA = [
                "Japanese (ja)",
                "Chinese (zh)",
                "Korean (ko)",
                "Thai (th)",
                "Burmese (my)",
                "Khmer (km)"
            ]

            # 特殊な区切り、半角スペースなし。
            language_groupB = [
                "Lao (lo)"
            ]

            # "。","、"区切り,半角スペースあり。
            language_groupC = [
                "Vietnamese (vi)"
            ]

            # ".",",","?","!"区切り,半角スペースあり。
            language_groupD = [
                "English (en)",
                "Spanish (es)",
                "French (fr)", 
                "Portuguese (pt)",
                "Russian (ru)",
                "German (de)",
                "Italian (it)", 
                "Dutch (nl)", 
                "Swedish (sv)",
                "Polish (pl)",
                "Ukrainian (uk)",
                "Greek (el)",
                "Romanian (ro)", 
                "Hungarian (hu)", 
                "Czech (cs)",
                "Hebrew (he)",
                "Finnish (fi)",
                "Serbian (sr)", 
                "Slovak (sk)", 
                "Georgian (ka)",
                "Norwegian (no)",
                "Danish (da)",
                "Icelandic (is)", 
                "Latvian (lv)",
                "Lithuanian (lt)",
                "Estonian (et)", 
                "Afrikaans (af)", 
                "Zulu (zu)", 
                "Galician (gl)", 
                "Basque (eu)", 
                "Armenian (hy)", 
                "Somali (so)", 
                "Malagasy (mg)"
            ]

            # 特殊な区切り、半角スペースあり。
            language_groupE = [
                "Arabic (ar)",
                "Bengali (bn)",
                "Tamil (ta)",
                "Urdu (ur)",
                "Persian (fa)",
                "Pashto (ps)",
                "Kurdish (ku)",
                "Tigrinya (ti)",
                "Amharic (am)",
                "Sinhala (si)"
            ]

            languages=language_groupA+language_groupD

            st.session_state.language_result=st.radio("Choose Your Mother Tongue",languages,horizontal=True,key="language_key",on_change=save_language_key)
            
            if st.button("保存", key="cash_control"):
                st.cache_data.clear()
                st.cache_resource.clear()
                st.rerun()


            

    


            # print(f"st.session_state.select_dot_result:{st.session_state.select_dot_result}")
            # print(f'st.session_state.dot_key:{st.session_state.dot_key}')


            
                 
    elif st.session_state.current_tab=="LICENSE":#☆license
        # print(f"st.session_state.ja_split:{st.session_state.ja_split}")
        # print(f"st.session_state.ja_split:{st.session_state.ja_split_key}")
        
             
        with st.container():
            # ライセンスファイルの読み込み
            with open("LICENSES.md", "r", encoding="utf-8") as f:
                markdown_content = f.read()

            # markdown2で表を含むMarkdownをHTMLに変換
            markdowner = markdown2.Markdown(extras=["tables"])  # "tables"オプションを有効化
            html_content = markdowner.convert(markdown_content)

            # CSSでスクロール領域と表のスタイルを調整する
            st.markdown(
                """
                <style>
  
                table {
                    width: 100%;
                    border-collapse: collapse;
                }
                th, td {
                    border: 1px solid black;
                    padding: 8px;
                    text-align: left;
                }
                th {
                    background-color: #f2f2f2;
                }
                </style>
                """, 
                unsafe_allow_html=True
            )

            # タイトルとライセンス内容を表示
            st.markdown("<div class='tab_title'>LICENSEについて</div>", unsafe_allow_html=True)

            # HTMLとしてライセンス内容を表示 (表を含む)
            st.markdown(f"<div class='license-container'>{html_content}</div>", unsafe_allow_html=True)
            
                 
            # print(f"st.session_state.select_dot_result:{st.session_state.select_dot_result}")
            # print(f'st.session_state.dot_key:{st.session_state.dot_key}')