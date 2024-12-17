import re
from datetime import timedelta
import tempfile
import os
from datetime import datetime
import streamlit as st
from streamlit_module import moz_tab7 as t7
from streamlit_module import common as co 

# タイムスタンプを秒単位のfloatに変換する関数
def timestamp_to_seconds(timestamp):
    time_parts = re.split(r'[:,.]', timestamp)
    hours, minutes, seconds, millis = map(int, time_parts[:3] + [time_parts[-1]])
    return hours * 3600 + minutes * 60 + seconds + millis / 1000.0

# 秒単位のfloatをタイムスタンプ形式に変換する関数
def seconds_to_timestamp(seconds, is_srt=True):
    td = timedelta(seconds=seconds)
    total_seconds = int(td.total_seconds())
    millis = int(td.microseconds / 1000)
    timestamp = f"{total_seconds // 3600}:{(total_seconds % 3600) // 60:02}:{total_seconds % 60:02},{millis:03}"
    if not is_srt:
        timestamp = timestamp.replace(',', '.')
    return timestamp

# 読点で分割し、min_length以下の場合はマージし、max_lengthに基づいてセグメントを分割
'''def split_and_merge_short_segments(text, start_time, end_time, min_length=10, max_length=70):
    sub_segments = re.split(r'(?<=、)', text)
    total_length = sum(len(seg) for seg in sub_segments)
    duration = end_time - start_time

    result_segments = []
    result_timestamps = []
    current_seg = ""
    current_start_time = start_time
    elapsed_time = start_time

    for i, sub_seg in enumerate(sub_segments):
        segment_length = len(sub_seg)
        proportion = segment_length / total_length
        segment_duration = proportion * duration
        new_end_time = elapsed_time + segment_duration
        
        # min_length以下のセグメントは次のセグメントとマージ
        if len(current_seg) + len(sub_seg) <= min_length:
            current_seg += sub_seg
        elif len(current_seg) + len(sub_seg) <= max_length:
            current_seg += sub_seg
        else:
            # max_lengthを超えたらセグメント確定
            result_segments.append(current_seg)
            result_timestamps.append((current_start_time, elapsed_time))  # 終了時刻を更新
            current_seg = sub_seg
            current_start_time = elapsed_time  # 次のセグメントの開始時刻を更新

        elapsed_time = new_end_time

    # 最後のセグメントも処理
    if current_seg:
        result_segments.append(current_seg)
        result_timestamps.append((current_start_time, elapsed_time))  # 最終セグメントの終了時刻を更新

    return result_segments, result_timestamps'''

'''def split_and_merge_short_segments(text, start_time, end_time, min_length=10, max_length=70):
    # 読点で分割
    sub_segments = re.split(r'(?<=、)', text)
    total_length = sum(len(seg) for seg in sub_segments)
    duration = end_time - start_time

    if total_length == 0 or duration <= 0:
        return [], []  # テキストや時間が不正な場合は空リストを返す

    result_segments = []
    result_timestamps = []
    current_seg = ""
    current_start_time = start_time
    elapsed_time = start_time

    for sub_seg in sub_segments:
        segment_length = len(sub_seg)
        proportion = segment_length / total_length
        segment_duration = proportion * duration
        new_end_time = elapsed_time + segment_duration

        # min_length以下のセグメントは次のセグメントとマージ
        if len(current_seg) + len(sub_seg) <= min_length:
            current_seg += sub_seg
        elif len(current_seg) + len(sub_seg) <= max_length:
            current_seg += sub_seg
        else:
            # max_lengthを超えたらセグメント確定
            if current_seg.strip():  # 空でなければ追加
                result_segments.append(current_seg)
                result_timestamps.append((current_start_time, elapsed_time))
            current_seg = sub_seg
            current_start_time = elapsed_time

        elapsed_time = max(new_end_time, elapsed_time + 0.01)  # 微小な進行を強制

    # 最後のセグメントも処理
    if current_seg.strip():
        result_segments.append(current_seg)
        result_timestamps.append((current_start_time, elapsed_time))

    # 幅がゼロのタイムスタンプを除外
    filtered_segments = []
    filtered_timestamps = []
    for seg, (start, end) in zip(result_segments, result_timestamps):
        if end - start > 0:
            filtered_segments.append(seg)
            filtered_timestamps.append((start, end))

    return filtered_segments, filtered_timestamps'''

'''def split_and_merge_short_segments(text, start_time, end_time, min_length=10, max_length=30):
    # 読点で分割
    sub_segments = re.split(r'(?<=、)', text)
    total_length = sum(len(seg) for seg in sub_segments)
    duration = end_time - start_time

    if total_length == 0 or duration <= 0:
        return [], []  # テキストや時間が不正な場合は空リストを返す

    result_segments = []
    result_timestamps = []
    current_seg = ""
    current_start_time = start_time
    elapsed_time = start_time

    for sub_seg in sub_segments:
        segment_length = len(sub_seg)
        proportion = segment_length / total_length
        segment_duration = proportion * duration
        new_end_time = elapsed_time + segment_duration

        # 最小文字数以下の場合は次のセグメントとマージ
        if len(current_seg) + len(sub_seg) <= max_length:
            current_seg += sub_seg
        else:
            # max_lengthを超えたらセグメント確定
            if len(current_seg) < min_length:
                # 最小文字数ルール優先: 次のセグメントをマージ
                current_seg += sub_seg
                elapsed_time = new_end_time  # タイムスタンプを進める
            else:
                # 通常の分割処理
                result_segments.append(current_seg)
                result_timestamps.append((current_start_time, elapsed_time))
                current_seg = sub_seg
                current_start_time = elapsed_time

        elapsed_time = max(new_end_time, elapsed_time + 0.01)  # 微小な進行を強制

    # 最後のセグメントも処理
    if current_seg.strip():
        result_segments.append(current_seg)
        result_timestamps.append((current_start_time, elapsed_time))

    return result_segments, result_timestamps'''
def split_and_merge_short_segments(text, start_time, end_time, min_length=10, max_length=30):
    # 読点で分割
    lang_tail=co.extract_short_name(st.session_state.language_result)
    if lang_tail=='ja':
        sub_segments = re.split(r'(?<=、)', text)
    else:
        sub_segments = re.split(r'(?<=,)', text)
    total_length = sum(len(seg) for seg in sub_segments)
    duration = end_time - start_time

    if total_length == 0 or duration <= 0:
        return [], []  # テキストや時間が不正な場合は空リストを返す

    result_segments = []
    result_timestamps = []
    current_seg = ""
    current_start_time = start_time
    elapsed_time = start_time

    for sub_seg in sub_segments:
        segment_length = len(sub_seg)
        proportion = segment_length / total_length
        segment_duration = proportion * duration
        new_end_time = elapsed_time + segment_duration

        # 最小文字数以下の場合は次のセグメントとマージ
        if len(current_seg) + len(sub_seg) <= max_length:
            current_seg += sub_seg
        else:
            # max_lengthを超えたらセグメント確定
            if len(current_seg) < min_length:
                # 最小文字数ルール優先: 次のセグメントをマージ
                current_seg += sub_seg
                elapsed_time = new_end_time  # タイムスタンプを進める
            else:
                # 通常の分割処理
                result_segments.append(current_seg)
                result_timestamps.append((current_start_time, elapsed_time))
                current_seg = sub_seg
                current_start_time = elapsed_time

        elapsed_time = max(new_end_time, elapsed_time + 0.01)  # 微小な進行を強制

    # 最後のセグメントも処理
    if current_seg.strip():
        result_segments.append(current_seg)
        result_timestamps.append((current_start_time, elapsed_time))

    # 最後の要素が最小文字数以下の場合、1つ前のセグメントに結合
    if len(result_segments) > 1 and len(result_segments[-1]) < min_length:
        # 結合する
        result_segments[-2] += result_segments[-1]
        result_timestamps[-2] = (result_timestamps[-2][0], result_timestamps[-1][1])  # 終了時刻を更新
        # 最後のセグメントを削除
        result_segments.pop()
        result_timestamps.pop()

    return result_segments, result_timestamps
# SRT/VTTファイルを読み込み、タイムスタンプとテキストを同時に分割・マージする
def split_srt_vtt_by_comma_and_merge(file_path, max_length=70, min_length=10):
    is_srt = file_path.endswith('.srt')

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    if not is_srt:
        lines = t7.webvtt_rm(lines)

    new_segments = []
    segment_id = 1
    buffer = []
    
    for line in lines:
        if line.strip() == "" and buffer:
            # タイムスタンプの解析
            timestamp_str = buffer[1].strip()
            match = re.match(r'(\d{1,2}:\d{2}:\d{2}[,.]\d{3}) --> (\d{1,2}:\d{2}:\d{2}[,.]\d{3})', timestamp_str)
            if not match:
                raise ValueError("Invalid timestamp format")
            
            start_time_str, end_time_str = match.groups()
            start_time = timestamp_to_seconds(start_time_str)
            end_time = timestamp_to_seconds(end_time_str)
            
            text = ''.join(buffer[2:]).strip()
            
            # タイムスタンプとテキストを同時に分割・マージ
            segments, timestamps = split_and_merge_short_segments(text, start_time, end_time, min_length, max_length)
            
            # 各セグメントにタイムスタンプを割り当てて出力
            for segment, (seg_start_time, seg_end_time) in zip(segments, timestamps):
                new_segments.append(f"{segment_id}\n")
                new_segments.append(f"{seconds_to_timestamp(seg_start_time,is_srt)} --> {seconds_to_timestamp(seg_end_time,is_srt)}\n")
                new_segments.append(f"{segment.strip()}\n\n")
                
                segment_id += 1
            
            buffer = []
        else:
            buffer.append(line)
    
    # 新しいファイルのパスを生成
    timestamp_patch = datetime.now().strftime("%Y%m%d%H%M%S")
    temp_dir = os.path.join(tempfile.gettempdir(), f"tempdir_{timestamp_patch}")
    os.makedirs(temp_dir, exist_ok=True)

    new_filename = f"{os.path.basename(file_path).replace('_sp','_spc')}"
    new_filepath = os.path.join(temp_dir, new_filename)

    with open(new_filepath, 'w', encoding='utf-8') as file:
        if is_srt:
            file.writelines(new_segments)
        else:
            # WebVTT形式に戻す
            file.write("WEBVTT\n\n")  # WebVTTのヘッダー
            file.writelines(new_segments)

    return new_filepath

def true_comma_split(file_path, max_length=70, min_length=10):
    is_srt = file_path.endswith('.srt')

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    if not is_srt:
        lines = t7.webvtt_rm(lines)

    new_segments = []
    segment_id = 1
    buffer = []
    
    for line in lines:
        if line.strip() == "" and buffer:
            # タイムスタンプの解析
            timestamp_str = buffer[1].strip()
            match = re.match(r'(\d{1,2}:\d{2}:\d{2}[,.]\d{3}) --> (\d{1,2}:\d{2}:\d{2}[,.]\d{3})', timestamp_str)
            if not match:
                raise ValueError("Invalid timestamp format")
            
            start_time_str, end_time_str = match.groups()
            start_time = timestamp_to_seconds(start_time_str)
            end_time = timestamp_to_seconds(end_time_str)
            
            text = ''.join(buffer[2:]).strip()
            
            # タイムスタンプとテキストを同時に分割・マージ
            segments, timestamps = split_and_merge_short_segments(text, start_time, end_time, min_length, max_length)
            
            # 各セグメントにタイムスタンプを割り当てて出力
            for segment, (seg_start_time, seg_end_time) in zip(segments, timestamps):
                new_segments.append(f"{segment_id}\n")
                new_segments.append(f"{seconds_to_timestamp(seg_start_time)} --> {seconds_to_timestamp(seg_end_time)}\n")
                new_segments.append(f"{segment.strip()}\n\n")
                
                segment_id += 1
            
            buffer = []
        else:
            buffer.append(line)
    
    # 新しいファイルのパスを生成
    timestamp_patch = datetime.now().strftime("%Y%m%d%H%M%S")
    temp_dir = os.path.join(tempfile.gettempdir(), f"tempdir_{timestamp_patch}")
    os.makedirs(temp_dir, exist_ok=True)

    new_filename = f"{os.path.basename(file_path).replace('_sp','_spc')}"
    new_filepath = os.path.join(temp_dir, new_filename)

    with open(new_filepath, 'w', encoding='utf-8') as file:
        file.writelines(new_segments)

    return new_filepath