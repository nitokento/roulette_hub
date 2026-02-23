import streamlit as st
import pandas as pd
from datetime import datetime
import random
import os
import time  

#tryは失敗したときの保険なり#
st.set_page_config(page_title="ダイスログ・システム", layout="centered")
st.title("信頼してるけどｗ")
try:
    st.image("野球.jpg"with=150,caption="担当:澤村拓一")
except:
    st.error("画像ファイル'野球.jpg'が見つかりません。github確認して")



LOG_FILE = "ルーレッツ.csv"


if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

if not st.session_state.user_name:
    st.info("最初に班名を登録してください")
    name_input = st.text_input("名前（例：萩生田光一）")
    if st.button("登録"):
        if name_input:
            st.session_state.user_name = name_input
            st.rerun()
        else:
            st.warning("名前を入力してください")
else:
   
    try:
        st.sidebar.image("大学生中指無修正.JPG", width=50) 
    except:
        st.sidebar.write("👤") 

    st.sidebar.write(f"ログイン中: **{st.session_state.user_name}**")
    
    if st.sidebar.button("ログアウト（名前変更）"):
        st.session_state.user_name = ""
        st.rerun()

    
    st.subheader(f"{st.session_state.user_name} さんの操作")
    
    if st.button("🎲 サイコロをぶん投げる"):
        
        cut_in_container = st.empty() 
        try:
            
            gif_path = r"C:\Users\azuru\Desktop\ルーレット\澤村大暴投.gif"
            
           
            cut_in_container.image(gif_path, use_container_width=True)
            
            
            time.sleep(1.2) 
            
           
            cut_in_container.empty()
        except Exception as e:
            st.error(f"カットインの再生に失敗しました: {e}")

        
        result = random.randint(1, 6)
        
        now = datetime.now()
        time_stamp = now.strftime("%Y/%m/%d %H:%M:%S") 

       
        new_log = {
            "発生時刻": time_stamp,
            "操作者": st.session_state.user_name,
            "出目": f"🎲 {result}"
        }

        
        df_new = pd.DataFrame([new_log])
        df_new.to_csv(LOG_FILE, index=False, header=not os.path.exists(LOG_FILE), mode='a', encoding='utf_8_sig')
        
        
        st.balloons()
        st.header(f"結果：{result} ") 
        st.success(f"【{time_stamp}】に記録しました！")

   
    st.divider()
    st.subheader("履歴一覧（最新順）")
    
    if os.path.exists(LOG_FILE):
        df_log = pd.read_csv(LOG_FILE)
        df_display = df_log.iloc[::-1] 
        
        st.dataframe(df_display, use_container_width=True)
        
        csv = df_log.to_csv(index=False).encode('utf_8_sig')
        st.download_button(
            label="履歴ファイルを保存",
            data=csv,
            file_name=f"dice_history_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
            mime="text/csv",
        )
    else:
        st.write("まだ履歴はありません。")