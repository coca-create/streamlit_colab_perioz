

import json
import streamlit as st
from deepmultilingualpunctuation import PunctuationModel
import re
import os
from datetime import datetime
import tempfile
from streamlit_module import moz_tab9 as t9
from streamlit_module import moz_sp as sp
import zipfile
import csv


def json_data_combine(data):
    combined_data = []
    i = 0

    while i < len(data):
        current_item = data[i]
        word = current_item['word']
        
        while (i + 1 < len(data)) and (not data[i + 1]['word'].startswith(" ")):
            next_item = data[i + 1]
            word += next_item['word']
            current_item['end'] = next_item['end']
            i += 1
        
        current_item['word'] = word
        combined_data.append(current_item)
        i += 1

    return combined_data

def apply_punctuated_words_to_data(data, punctuated_words):
    for i in range(len(data)):
        # deepmultiで作った単語を元のデータに置き換える
        # 単語の前にスペースを追加
        data[i]['word'] = f" {punctuated_words[i]}"

    return data



def json_rev(t11_uploaded_file,replace_word,select_model,dp2_bar=None,spl2_bar=None):
    if t11_uploaded_file is not None:
        if replace_word==True:
            common_app_data = os.getenv('APPDATA')  # WindowsのCommon AppDataフォルダ
            data_folder = os.path.join(common_app_data, 'PeriOz2')
            with open(os.path.join(data_folder,st.session_state.select_rp_result), newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # ヘッダーをスキップ
                replacements = [(row[0], row[1]) for row in reader]        
        with open(t11_uploaded_file,'r',encoding='utf-8') as file:
            data=json.load(file)
        
       
        data = json_data_combine(data)
        
        
        for item in data:
            item['word']=t9.protect_special_cases_srt(item['word'])
            
        
        original_words = [item['word'].strip() for item in data]
 
        sentences = "".join([item['word'] for item in data])
        #print(f"Sentences: {sentences}")  # 長い場合は最初の部分のみ出力


        '''with open("before_output.txt", "w", encoding="utf-8") as f:
            f.write(sentences)'''
        if select_model == False:
           model_name = "oliverguhr/fullstop-punctuation-multilingual-base"
        else:
           model_name = "oliverguhr/fullstop-punctuation-multilang-large"        
        model = PunctuationModel(model_name)

        # 実験
        
        if st.session_state.deepall:
            with st.spinner("すべてのピリオドを付け直し中です。"):
                sentences=sentences.replace(".","").replace("?","").replace("!","")
                sentences=model.restore_punctuation(sentences)
            '''with open ("sentence.txt","w",encoding='utf-8') as f:
                f.write(sentences)'''
        
        sentence_list=re.split(r'([.!?])', sentences)
                
        if len(sentence_list) % 2 != 0:
          sentence_list.append('')

        sentence_list=[''.join(sentence_list[i:i+2]) for i in range(0, len(sentence_list)-1, 2)]
        #print(sentence_list)
        if st.session_state.deepall:
            punctuated_list=sentence_list

        else :
            total_sentences=len(sentence_list)
            '''with open('sentence_list.txt', 'w', encoding='utf-8') as f:
                for sentence in sentence_list:
                    f.write(sentence + '\n')'''
            #空白のlistが入っているから、num+1ではなくnum。
            #print(f'model:{model_name}')
  
            punctuated_list=[]
            for num,sentence in enumerate(sentence_list):
                #print(len(sentence))

                if len(sentence)>0:
                    try:
                        punctuated_sentence = model.restore_punctuation(sentence)
                    except Exception as e:
                        print(f"Error restoring punctuation for sentence {num}: {e}")
                else:
                    punctuated_sentence = sentence    
                #punctuated_sentence = punctuated_sentence.replace(" - "," ").replace("- "," ").replace(" -"," ")
                punctuated_list.append(punctuated_sentence)
                dp2_bar.progress((num+1)/total_sentences)


        #print(f"Punctuated sentence: {punctuated_sentence}") 
        
       
        punctuated_sentences=' '.join(punctuated_list)
        '''with open("after_output.txt", "w", encoding="utf-8") as f:
            f.write(punctuated_sentences)'''

        words_in_sentences = punctuated_sentences.split()
    
        punctuated_words = [word.strip() for word in words_in_sentences]
        #print(f"Punctuated words: {punctuated_words}") 
    
        
        #print(f"処理後単語数:{len(words_in_sentences)}")
        #print(f"original:{len(original_words)}")
        
       
        #new_sentences = " ".join([item['word'] for item in data])


        # リストの長さを比較
        if len(original_words) != len(punctuated_words):

           
            #st.info(f"{os.path.basename(t11_uploaded_file)}からの再編は難しいようです。jsonファイルとsrtファイルの組み合わせによる再編をお使いください")
            return None,None,os.path.basename(t11_uploaded_file)
        else:           
      
            # 置換処理を実行
            
            new_data = apply_punctuated_words_to_data(data, punctuated_words)
            

            srt_entries = []
            entry_number = 1
            segment_text = ""
            segment_start = None
            segment_end = None
            
            #spl2_bar.progress(0)
            total_segments=len(new_data)
            for num,word_info in enumerate(new_data):

                if segment_start is None:
                    segment_start = word_info["start"]
                segment_text += word_info["word"]
                segment_end = word_info["end"]

                if word_info["word"].endswith('.') or word_info["word"].endswith('?'):
                    srt_entries.append({
                        "number": entry_number,
                        "start": segment_start,
                        "end": segment_end,
                        "text": segment_text.replace("[dot]",".").strip()
                    })
                    entry_number += 1
                    segment_text = ""
                    segment_start = None

            if segment_text.strip():
                srt_entries.append({
                    "number": entry_number,
                    "start": segment_start,
                    "end": segment_end,
                    "text": segment_text.replace("[dot]",".").strip()
                })
            if not st.session_state.deepall:
                spl2_bar.progress((num+1)/total_segments)

            t11_basename = os.path.splitext(t11_uploaded_file)[0]
            
            timestamp_patch = datetime.now().strftime("%Y%m%d%H%M%S")
            temp_dir = os.path.join(tempfile.gettempdir(), f"tempdir_{timestamp_patch}")
            os.makedirs(temp_dir, exist_ok=True) 

            t11_srt_path = os.path.join(temp_dir,f"{t11_basename}_rvj.srt")
            t11_txt_path = os.path.join(temp_dir,f"{t11_basename}_rvj_NR.txt")
            
            texts=[]
            if st.session_state.deepall:
                with st.spinner("キャピタライズを行っています。"):
                    with open(t11_srt_path, 'w', encoding='utf-8') as f:
                        for entry in srt_entries:
                            start_time = t9.format_time(entry["start"])
                            end_time = t9.format_time(entry["end"])
                            text = sp.process_text(entry['text'])
                            if replace_word==True:
                                for original, replacement in replacements:
                                    original=re.escape(original)
                                    new_original=rf"\b{original}\b"
                                    text = re.sub(new_original, replacement, text)
                            f.write(f"{entry['number']}\n{start_time} --> {end_time}\n{text}\n\n")
                            texts.append(text)

                    with open(t11_txt_path,"w",encoding="utf-8") as f:
                        for text in texts:
                            '''
                            if replace_word==True:
                                for original, replacement in replacements:
                                    original=re.escape(original)
                                    new_original = rf"\b{original}\b"
                                    text = re.sub(new_original, replacement, text)     '''               
                            f.write(text+" ")
            else:
                with open(t11_srt_path, 'w', encoding='utf-8') as f:
                    for entry in srt_entries:
                        start_time = t9.format_time(entry["start"])
                        end_time = t9.format_time(entry["end"])
                        text = sp.process_text(entry['text'])
                        if replace_word==True:
                            for original, replacement in replacements:
                                original=re.escape(original)
                                new_original=rf"\b{original}\b"
                                text = re.sub(new_original, replacement, text)
                        f.write(f"{entry['number']}\n{start_time} --> {end_time}\n{text}\n\n")
                        texts.append(text)

                with open(t11_txt_path,"w",encoding="utf-8") as f:
                    for text in texts:
                        '''
                        if replace_word==True:
                            for original, replacement in replacements:
                                original=re.escape(original)
                                new_original = rf"\b{original}\b"
                                text = re.sub(new_original, replacement, text)     '''               
                        f.write(text+" ")

        return t11_srt_path, t11_txt_path,None

    else:
        st.write("Jsonファイルをアップロードしてください。")


    
def multi_json_operator(uploaded_files,replace_word,select_model):
    warning_placeholder = st.sidebar.empty()
    warning_placeholder.warning("処理中にタブを切り替えると処理が中止されます。ご注意ください。")

    srt_files=[]
    txt_files=[]
    skipped_files=[]
    skipped_file_messages=[]
    for idx,json_file in enumerate(uploaded_files):


        if not st.session_state.deepall:
            dp2_message = st.empty()  
            dp2_bar = st.progress(0)
            spl2_message = st.empty()  
            spl2_bar = st.progress(0)

            dp2_message.write("ピリオドを追加しています。")
            spl2_message.write("ピリオドを基準に分割し、capitalize処理を行っています。")


        file_number=st.empty()
        sk_files=[]
        if skipped_files:
            for sk_file in skipped_files:
                # プレースホルダーを作成して、その中にメッセージを表示
                placeholder = st.empty()
                placeholder.write(f'＊　"{sk_file}"　の処理はスキップされました。')
        
                # プレースホルダーをリストに保存
                sk_files.append(placeholder)



        file_number.write(f'処理中のファイル:　{idx+1}/{len(uploaded_files)}　・・・　"{os.path.basename(json_file)}"')
        
        if not st.session_state.deepall:
            srt_file,txt_file,skipped_file=json_rev(json_file,replace_word,select_model,dp2_bar,spl2_bar)
        else:
            srt_file,txt_file,skipped_file=json_rev(json_file,replace_word,select_model)
        if srt_file==None:
            
            
            skipped_files.append(skipped_file)
            file_number.empty()
            if not st.session_state.deepall:
            
                dp2_message.empty()  
                dp2_bar.empty()
                spl2_message.empty()  
                spl2_bar.empty()

            if sk_files:
          
                for file in sk_files:
                    file.empty()           
            
            continue
        else:

            srt_files.append(srt_file)
            txt_files.append(txt_file)
            file_number.empty()
            if not st.session_state.deepall:
                dp2_message.empty()  
                dp2_bar.empty()
                spl2_message.empty() 
                if spl2_bar:
                    spl2_bar.empty()
            if sk_files:
                for file in sk_files:
                    file.empty() 
    
    if len(srt_files) > 1 :
        # ZIPファイルを生成
        timestamp_patch = datetime.now().strftime("%Y%m%d%H%M%S")
        temp_dir = os.path.join(tempfile.gettempdir(), f"tempdir_{timestamp_patch}")
        os.makedirs(temp_dir, exist_ok=True)

        reversal_srt_zip = os.path.join(temp_dir, "reversal_srts_from_json.zip")
        reversal_txt_zip = os.path.join(temp_dir, "reversal_txts_from_json.zip")
        with zipfile.ZipFile(reversal_srt_zip, 'w') as srt_zip:
            for file in srt_files:
                srt_zip.write(file, os.path.basename(file))
     
        with zipfile.ZipFile(reversal_txt_zip, 'w') as txt_zip:
            for file in txt_files:
                txt_zip.write(file, os.path.basename(file))
        zip_files=[reversal_srt_zip,reversal_txt_zip]
        file_number.empty()

        warning_placeholder.empty()

        return zip_files,skipped_files
    elif srt_files==[]:
        warning_placeholder.empty()

        return [],skipped_files
    else:
        srt_and_txt_file=[srt_files[0],txt_files[0]]
        file_number.empty()
        for sikipped_mssg_holder in skipped_file_messages:
            sikipped_mssg_holder.empty()
        warning_placeholder.empty()
        return srt_and_txt_file,skipped_files
    
