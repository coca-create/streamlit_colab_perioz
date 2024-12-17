import pandas as pd
from datetime import datetime
import tempfile
import os
import re
from streamlit_module import moz_tab7 as t7
from streamlit_module import common as co
from streamlit_module import moz_split as cm
import streamlit as st
import csv
import zipfile


def convert_time_to_seconds(time_str):
    try:
        time_parts = time_str.split(':')
        if len(time_parts) == 3:
            h, m, s = time_parts
        elif len(time_parts) == 2:
            h = 0
            m, s = time_parts
        else:
            raise ValueError(f"Unexpected time format: {time_str}")
        
        h = float(h)
        m = float(m)
        s = float(s.replace(',', '.'))
        return h * 3600 + m * 60 + s
    except ValueError as e:
        raise ValueError(f"Error converting time: {time_str}, {e}")

def convert_seconds_to_time(seconds, format_type='vtt'):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = seconds % 60
    if format_type == 'vtt':
        return f"{h:01}:{m:02}:{s:06.3f}".replace(',', '.')
    else:
        return f"{h:02}:{m:02}:{s:06.3f}".replace('.', ',')
    
def restore_special_periods(text):
    text = text.replace('[dot]', '.')
    return text

def merge_segments(segments):
    merged_segments = []
    buffer_segment = ""
    buffer_start = None
    buffer_end = None

    for segment, start, end in segments:
        if buffer_segment:
            buffer_segment += " " + segment
            buffer_end = end
            if segment.endswith('.') or segment.endswith('?') or segment.endswith('!') or segment.endswith('？') or segment.endswith('！'):
                merged_segments.append((buffer_segment, buffer_start, buffer_end))
                buffer_segment = ""
                buffer_start = None
                buffer_end = None
        else:
            if segment.endswith('.') or segment.endswith('?') or segment.endswith('!') or segment.endswith('？') or segment.endswith('！'):
                merged_segments.append((segment, start, end))
            else:
                buffer_segment = segment
                buffer_start = start
                buffer_end = end

    if buffer_segment:
        merged_segments.append((buffer_segment, buffer_start, buffer_end))

    #print(f"Merged Segments: {merged_segments}")  # デバッグ出力

    return merged_segments
def split_segment(segment, start_time, end_time): # 文字数基準の分割。
    if start_time is None or end_time is None:
        return [(segment, start_time, end_time)]

    #print(f"Segment before split: {segment}")  # デバッグ出力

    # 空白で区切って単語単位で処理
    words = segment.split()

    # 分割用リスト
    sentences = []
    current_sentence = []

    for word in words:
        current_sentence.append(word)
        # 単語がピリオド, 感嘆符, 質問符で終わる場合
        if word.endswith(('.', '!', '?','？','！')):
            # 現在の文を文字列として結合し、リストに追加
            sentences.append(' '.join(current_sentence))
            current_sentence = []

    # 最後の文があれば追加
    if current_sentence:
        sentences.append(' '.join(current_sentence))

    # 文の長さ（文字数）を考慮して、時間を配分
    total_length = sum(len(sentence) for sentence in sentences)
    if total_length == 0:
        return [(segment, start_time, end_time)]  # 文がない場合、元のセグメントをそのまま返す
    
    

    # タイムスタンプを文の長さに応じて割り振る
    times = [start_time]
    for sentence in sentences:
        sentence_length = len(sentence)
        duration = (end_time - start_time) * (sentence_length / total_length)
        times.append(times[-1] + duration)

    return [(sentences[i], times[i], times[i+1]) for i in range(len(sentences))]

def process_vtt(lines):
    segments = []
    start_time = None
    end_time = None
    text = ""
    header = lines[0]

    for line in lines[1:]:
        if re.match(r'^\d+$', line.strip()):
            if text:               
                common_app_data = os.getenv('APPDATA')  # WindowsのCommon AppDataフォルダ
                data_folder = os.path.join(common_app_data, 'PeriOz2')
                if st.session_state.select_dot_result:
                    with open(os.path.join(data_folder,st.session_state.select_dot_result), newline='',encoding='utf-8') as dot_csvfile:
                        reader = csv.reader(dot_csvfile)
                        next(reader)
                        dot_replacements = [(row[0],row[1]) for row in reader]
                         
                    for dot_original, dot_replacement in dot_replacements:
                        r_dot_original=re.escape(dot_original)
                        dot_new_original = rf"\b{r_dot_original}"
                        text = re.sub(dot_new_original, dot_replacement, text)

                if start_time is not None and end_time is not None:
                    segments.extend(split_segment(text.strip(), start_time, end_time))
            text = ""
            
        elif '-->' in line:
            times = line.strip().split(' --> ')
            start_time = convert_time_to_seconds(times[0])
            end_time = convert_time_to_seconds(times[1])
        else:
            text += line.strip() + " "

    if text:
        #print(st.session_state.select_dot_result)
        if st.session_state.select_dot_result:
            common_app_data = os.getenv('APPDATA')  # WindowsのCommon AppDataフォルダ
            data_folder = os.path.join(common_app_data, 'PeriOz2')
            
            with open(os.path.join(data_folder,st.session_state.select_dot_result), newline='',encoding='utf-8') as dot_csvfile:
                reader = csv.reader(dot_csvfile)
                next(reader)
                dot_replacements = [(row[0],row[1]) for row in reader]
            
            
            for dot_original, dot_replacement in dot_replacements:
                r_dot_original=re.escape(dot_original)
                dot_new_original = rf"\b{r_dot_original}"
                text = re.sub(dot_new_original, dot_replacement, text)

        #text = replace_special_periods(text)
        if start_time is not None and end_time is not None:
            segments.extend(split_segment(text.strip(), start_time, end_time))

    merged_segments = merge_segments(segments)


    '''if replace_words==True and st.session_state.select_rp_result: 
        common_app_data = os.getenv('APPDATA')  # WindowsのCommon AppDataフォルダ
        data_folder = os.path.join(common_app_data, 'PeriOz2')
        with open(os.path.join(data_folder,st.session_state.select_rp_result), newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # ヘッダーをスキップ
            replacements = [(row[0], row[1]) for row in reader]'''


    output = [header]
    segment_number = 0
    for text, start, end in merged_segments:        
        text = restore_special_periods(text)
        '''if replace_words==True and st.session_state.select_rp_result:
            for original, replacement in replacements:
                original=re.escape(original)
                new_original = rf"\b{original}\b"
                text = re.sub(new_original, replacement, text)'''
        output.append(f"{segment_number + 1}")
        output.append(f"{convert_seconds_to_time(start, 'vtt')} --> {convert_seconds_to_time(end, 'vtt')}")
        output.append(text)
        segment_number += 1
        output.append("")  # セグメント間の改行を保持

    return '\n'.join(output)

def process_srt(lines):
    segments = []
    start_time = None
    end_time = None
    text = ""
    segment_index = 0

    for line in lines:
        if re.match(r'^\d+$', line.strip()):
            if text:
                # text = replace_special_periods(text)
                if st.session_state.select_dot_result:
                    common_app_data = os.getenv('APPDATA')  # WindowsのCommon AppDataフォルダ
                    data_folder = os.path.join(common_app_data, 'PeriOz2')
                    with open(os.path.join(data_folder,st.session_state.select_dot_result), newline='',encoding='utf-8') as dot_csvfile:
                        reader = csv.reader(dot_csvfile)
                        next(reader)
                        dot_replacements = [(row[0],row[1]) for row in reader]
                    
                    
                    for dot_original, dot_replacement in dot_replacements:
                        r_dot_original=re.escape(dot_original)
                        dot_new_original = rf"\b{r_dot_original}"
                        text = re.sub(dot_new_original, dot_replacement, text)

                segments.extend(split_segment(text.strip(), start_time, end_time))
            segment_index = int(line.strip())
            text = ""
        elif '-->' in line:
            times = line.strip().split(' --> ')
            start_time = convert_time_to_seconds(times[0].replace(',', '.'))
            end_time = convert_time_to_seconds(times[1].replace(',', '.'))
        else:
            text += line.strip() + " "

    if text:
        #text = replace_special_periods(text)
        if st.session_state.select_dot_result:
            common_app_data = os.getenv('APPDATA')  # WindowsのCommon AppDataフォルダ
            data_folder = os.path.join(common_app_data, 'PeriOz2')
            with open(os.path.join(data_folder,st.session_state.select_dot_result), newline='',encoding='utf-8') as dot_csvfile:
                reader = csv.reader(dot_csvfile)
                next(reader)
                dot_replacements = [(row[0],row[1]) for row in reader]
            
            
            for dot_original, dot_replacement in dot_replacements:
                r_dot_original=re.escape(dot_original)
                dot_new_original = rf"\b{r_dot_original}"
                text = re.sub(dot_new_original, dot_replacement, text)

        segments.extend(split_segment(text.strip(), start_time, end_time))

    merged_segments = merge_segments(segments)

    # replacements.csv を読み込む
    

    output = []
    segment_number = 0
    for text, start, end in merged_segments:
        text = restore_special_periods(text)
        output.append(f"{segment_number + 1}\n{convert_seconds_to_time(start,'srt').replace('.', ',')} --> {convert_seconds_to_time(end,'srt').replace('.', ',')}\n{text}\n")
        segment_number += 1

    return '\n'.join(output)

def process_sp_periods(input_file):#日本語と中国語以外の句点（ピリオド分割)
    if input_file is None:
        return None

    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    lang_tail=co.extract_short_name(st.session_state.language_result)
    basename = os.path.splitext(os.path.basename(input_file))[0].replace(f"_{lang_tail}","")
    
    timestamp_patch = datetime.now().strftime("%Y%m%d%H%M%S")
    temp_dir = os.path.join(tempfile.gettempdir(), f"tempdir_{timestamp_patch}")
    os.makedirs(temp_dir, exist_ok=True) 
    if input_file.lower().endswith('.vtt'):
        output = process_vtt(lines)
        output_file = os.path.join(temp_dir, f"{basename}_sp_{lang_tail}.vtt")
    elif input_file.lower().endswith('.srt'):
        output = process_srt(lines)
        output_file = os.path.join(temp_dir, f"{basename}_sp_{lang_tail}.srt")
    else:
        raise ValueError('Unsupported file format')

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(output)

    return output_file

def process_files(file_paths,onlyfile=False):
    # 1つの一時ディレクトリを生成する
    #print("nowko")
    timestamp_patch = datetime.now().strftime("%Y%m%d%H%M%S")
    temp_dir = os.path.join(tempfile.gettempdir(), f"tempdir_{timestamp_patch}")
    os.makedirs(temp_dir, exist_ok=True)
    
    results = []
    for uploaded_file in file_paths:
        outputfilepath=process_sp_periods(uploaded_file)
        results.append(outputfilepath)
    
        if onlyfile==False and st.session_state.comma_split:
            
            cm_file=cm.true_comma_split(outputfilepath,st.session_state.max_split,st.session_state.min_split)           
            results.append(cm_file)
            
    if onlyfile==True:
        return results[0]

    # 4つ以上のファイルの場合、ZIPファイルにまとめる
    if len(results) > 3:
        zip_file = 'splitted_files.zip'
        zip_file_path = os.path.join(temp_dir, zip_file)
        
        with zipfile.ZipFile(zip_file_path, 'w') as zipf:
            for file_path in results:
                # ファイルをZIPファイルに追加
                zipf.write(file_path, os.path.basename(file_path))
            #print(zip_file_path)
        return [zip_file_path]  # ZIPファイルのパスを返す

    return results  # 3つ以下ならファイルパスのリストを返す
