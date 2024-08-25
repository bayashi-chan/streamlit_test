import pandas as pd 
import streamlit as st 

st.title('Streamlitやってみる これはst.titleの大きさ')

#titleは大きな文字、:blue[]の[]は中の文字を青くする、:sunglasses: は サングラスをかけた顔の絵文字
st.title("Hello, :blue[Bayashi's HP]:sunglasses:")
st.write('writeの大きさで記載')

st.write(
    pd.DataFrame(
        {
            "first column":[1,2,3,4],
            "second column":[10,20,30,40],
        }
    )
)

st.link_button("yahooファイナンス","https://finance.yahoo.co.jp/")

st.header("Stramlitでは何ができるのか、下記にいろいろ行ってみる", divider="rainbow")

#”””は、複数行にまたがる文字列を記載できる？
code = """print("まず、文を表示してみる。")"""
#printはそのまま表示、st.codeはStreamlit上でコードそのものを表示したいときに用いる。あ
st.code(code,language="python")

agree = st.checkbox("I agree?")
if agree:
    st.write("Okay!")

options = st.multiselect(
    "好きな色はなんですか？",
    ["赤","緑","青","黄"]
)

st.write("あなたが選んだ色は：",options)


options = st.radio(
    "好きな色はなんですか？",
    ["赤","緑","青","黄"]
)

st.write("あなたが選んだ色は：",options)

#修正できるデータフレーム
df = pd.DataFrame(
    [
        {"colors":"赤" , "rating": 4,"mark":True},
        {"colors":"緑" , "rating": 5,"mark":True},
        {"colors":"青" , "rating": 6,"mark":True},
    ]
)
edited_df = st.data_editor(df)
st.write(edited_df["rating"])
st.write(edited_df["rating"].idxmax())
st.write(edited_df.loc[edited_df["rating"].idxmax()])


edited_df = edited_df[edited_df["mark"] == True]
st.write(edited_df.loc[edited_df["rating"].idxmax()]["colors"])

csv = edited_df.to_csv().encode("utf-8")  #まずcsvにデータ変換をしてあげて

st.download_button(
    label="CSVをダウンロード",
    data=csv,
    file_name="sample_df.csv",
    mime="text/csv"
)

#　プログレスバー表示
df = pd.DataFrame(
    {
        "sales":[20,55,100,80],
        "progress_sales":[20,55,100,80],
    }
)


st.data_editor(
    df,
    column_config={
        "progress_sales":st.column_config.ProgressColumn(
            min_value=0,
            max_value=100,
        ),
    }
)

#時系列バー表示
df = pd.DataFrame(
    {
        "sales": [
            [0,4,26,30,60,80,100],
            [3,50,0,80,40,30,100]
        ]
    }
)
st.data_editor(df)


st.data_editor(
    df,
    column_config={
        "sales":st.column_config.BarChartColumn(
            y_min=0,
            y_max=100,
        ),
    }
)


st.data_editor(
    df,
    column_config={
        "sales":st.column_config.LineChartColumn(
            y_min=0,
            y_max=100,
        ),
    }
)

#スライダー（ユーザーインプット）
age = st.slider("あなたは何歳ですか？",0,130,40)
st.write("私は",age,"歳です")

#日付選択（ユーザーインプット）
import datetime
date = st.date_input("あなたが生まれたのはいつですか？",datetime.date(2000,1,1))
st.write("私は",date,"に生まれました")

#ユーザーの自由記述（ユーザーインプット）
text = st.text_input("入力してください","ここに入力をお願いします")
st.write(text)

#　カラムを分ける
col1,col2 = st.columns(2)
with col1:
    st.title("column1")
    st.write("これはカラムの１です")
with col2:
    st.title("column2")
    st.write("これはカラムの２です")

#　タブを分ける
tab1,tab2 = st.tabs(["tab1","tab2"])
with tab1:
    st.title("Tab1")
    st.write("これはタブの１です")
with tab2:
    st.title("Tab2")
    st.write("これはタブの２です")

# アコーディオン表示
with st.expander("もっと詳しく見る"):
    st.write("XXXXXXX")

#ポップアップ表示
with st.popover("もっと詳しく見る"):
    st.write("XXXXXX")

#サイドバー
with st.sidebar:
    st.title("ばやと申します")
    st.write("詳細１")

#notification
agree = st.checkbox("同意しますか？")
if agree:
    st.toast("Thank you", icon ="👌")
    st.toast("Thank you", icon ="👌")
    st.toast("Thank you", icon ="👌")

birthday = st.checkbox("今日はあなたの誕生日ですか？")
if birthday:
    st.toast("誕生日おめでとう！",icon="👍")
    st.balloons()

# 複数ページ実装
st.page_link("app.py",label="Home",icon="🏠")
st.page_link("pages/page1.py",label="page1")
st.page_link("pages/page2.py",label="page2")
st.page_link("https://docs.streamlit.io/develop/api-reference",label="StreamlitのAPIドキュ")

print("0825に編集追加した")