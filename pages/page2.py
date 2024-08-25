import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

st.title("Irisデータを用いた予測アプリ")

iris = load_iris() 
#アイリスには色々なデータが入っている。アイリスデータには説明変数に該当する部分のデータが

x = pd.DataFrame(iris.data,columns=iris.feature_names)
#アイリスfeature_nameのところに説明変数に該当するカラムの名称がある
#xは説明変数で、yが目的変数

y = pd.Series(iris.target,name="species")

#　学習データとテストデータに分割
train_test_split(x,y,test_sizr=0.3)

print("0825henkou")

