from math import sqrt
import random
import streamlit as st

st.title("ピアソン類似度を用いたアーティストレコメンデーション 'Artist Recommendation'")

dataset = {}

#アンケート結果をdatasetに入力
with open("アーティスト１（回答） - フォームの回答 1.csv", "r", encoding='utf-8') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '').split(",")

    for i in range(1,len(lines)):
        l = {}
        for n in range(1,11):
            if lines[i][n] == "":
                continue
            l[lines[0][n]] = int(lines[i][n])

        dataset[lines[i][0]] = l

with open("アーティスト２（回答） - フォームの回答 1 (1).csv", "r", encoding='utf-8') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '').split(",")

    for i in range(1,len(lines)):
        l = {}
        for n in range(1,11):
            if lines[i][n] == "":
                continue
            l[lines[0][n]] = int(lines[i][n])

        dataset[lines[i][0]] = l

with open("アーティスト３（回答） - フォームの回答 1.csv", "r", encoding='utf-8') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '').split(",")

    for i in range(1,len(lines)):
        l = {}
        for n in range(1,11):
            if lines[i][n] == "":
                continue
            l[lines[0][n]] = int(lines[i][n])

        dataset[lines[i][0]] = l

with open("アーティスト４（回答） - フォームの回答 1.csv", "r", encoding='utf-8') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '').split(",")

    for i in range(1,len(lines)):
        l = {}
        for n in range(1,11):
            if lines[i][n] == "":
                continue
            l[lines[0][n]] = int(lines[i][n])

        dataset[lines[i][0]] = l

with open("アーティスト5（回答） - フォームの回答 1.csv", "r", encoding='utf-8') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '').split(",")

    for i in range(1,len(lines)):
        l = {}
        for n in range(1,11):
            if lines[i][n] == "":
                continue
            l[lines[0][n]] = int(lines[i][n])

        dataset[lines[i][0]] = l

with open("アーティスト6（回答） - フォームの回答 1.csv", "r", encoding='utf-8') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '').split(",")

    for i in range(1,len(lines)):
        l = {}
        for n in range(1,11):
            if lines[i][n] == "":
                continue
            l[lines[0][n]] = int(lines[i][n])

        dataset[lines[i][0]] = l

with open("アーティスト7（回答） - フォームの回答 1.csv", "r", encoding='utf-8') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '').split(",")

    for i in range(1,len(lines)):
        l = {}
        for n in range(1,11):
            if lines[i][n] == "":
                continue
            l[lines[0][n]] = int(lines[i][n])

        dataset[lines[i][0]] = l

with open("アーティスト8（回答） - フォームの回答 1.csv", "r", encoding='utf-8') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '').split(",")

    for i in range(1,len(lines)):
        l = {}
        for n in range(1,11):
            if lines[i][n] == "":
                continue
            l[lines[0][n]] = int(lines[i][n])

        dataset[lines[i][0]] = l

with open("アーティスト9（回答） - フォームの回答 1.csv", "r", encoding='utf-8') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '').split(",")

    for i in range(1,len(lines)):
        l = {}
        for n in range(1,11):
            if lines[i][n] == "":
                continue
            l[lines[0][n]] = int(lines[i][n])

        dataset[lines[i][0]] = l

with open("アーティスト10（回答） - フォームの回答 1.csv", "r", encoding='utf-8') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '').split(",")

    for i in range(1,len(lines)):
        l = {}
        for n in range(1,11):
            if lines[i][n] == "":
                continue
            l[lines[0][n]] = int(lines[i][n])

        dataset[lines[i][0]] = l



with open("artist.txt","r")as f:
    artists = f.readlines()
    for i in range(len(artists)):
        artists[i] = artists[i].replace('\n', '')


# 50人のアーティストから10組をランダムに選ぶ
random.shuffle(artists)
l = artists[:10]

name = st.text_input("ニックネームを入力 ’Enter your nick name’")
st.write("以下に書かれた10組のアーティストの中から、曲を聴いたことのあるアーティストのみに、1〜5までの評価をつけてください 'Please rate only the 10 artists listed below on a scale of 1 to 5. Leave blank, If you have never heard the artist's song.'")


artists = {}

artists['SEVENTEEN'] = st.slider('SEVENTEEN', 1, 5, 3)
artists['乃木坂46'] = st.slider('乃木坂46', 1, 5, 3)
artists['ずっと真夜中でいいのに。'] = st.slider('ずっと真夜中でいいのに。', 1, 5, 3)
artists['藤井風'] = st.slider('藤井風', 1, 5, 3)
artists['ONE OK ROCK'] = st.slider('ONE OK ROCK', 1, 5, 3)
artists['エド・シーラン'] = st.slider('エド・シーラン', 1, 5, 3)
artists['YOASOBI'] = st.slider('YOASOBI', 1, 5, 3)
artists['TWICE'] = st.slider('TWICE', 1, 5, 3)
artists['NiziU'] = st.slider('NiziU', 1, 5, 3)
artists['Official髭男dism'] = st.slider('Official髭男dism', 1, 5, 3)

dataset[name] = artists

# ピアソン類似度の算出
def pearson_correlation(person1, person2):

    # 両方のアイテムを取得
    both_rated = {}
    for item in dataset[person1]:
        if item in dataset[person2]:
            both_rated[item] = 1

    number_of_ratings = len(both_rated)

    # 共通のアイテムがあるかチェック、無ければ 0 を返す
    if number_of_ratings == 0:
        return 0

    # 各ユーザーごとのすべての好みを追加
    person1_preferences_sum = sum(
        [dataset[person1][item] for item in both_rated])
    person2_preferences_sum = sum(
        [dataset[person2][item] for item in both_rated])

    # 各ユーザーの好みの値の二乗を計算
    person1_square_preferences_sum = sum(
        [pow(dataset[person1][item], 2) for item in both_rated])
    person2_square_preferences_sum = sum(
        [pow(dataset[person2][item], 2) for item in both_rated])

    # アイテムごとのユーザー同士のレーティングを算出して合計
    product_sum_of_both_users = sum(
        [dataset[person1][item] * dataset[person2][item] for item in both_rated])

    # ピアソンスコアの計算
    numerator_value = product_sum_of_both_users - \
        (person1_preferences_sum * person2_preferences_sum / number_of_ratings)
    denominator_value = sqrt((person1_square_preferences_sum - pow(person1_preferences_sum, 2) / number_of_ratings) * (
        person2_square_preferences_sum - pow(person2_preferences_sum, 2) / number_of_ratings))
    if denominator_value == 0:
        return 0
    else:
        r = numerator_value / denominator_value
        return r

# ある人に対して、推薦度の高い順にアーティストをレコメンドする
def get_recommend(person, top_N):

    totals = {} ; simSums = {} #推薦度スコアを入れるための箱を作っておく

    # 自分以外のユーザのリストを取得してFor文を回す
    # -> 各人との類似度、及び各人からの（まだ本人が知らない）アーティストの推薦スコアを計算するため
    list_others = list(dataset.keys()) ; list_others.remove(person)

    for other in list_others:
        # 本人がまだ知らないアーティストの集合を取得
        set_other = set(dataset[other]); set_person = set(dataset[person])
        set_new_movie = set_other.difference(set_person)

        # あるユーザと本人の類似度を計算(simは0~1の数字)
        sim = pearson_correlation(person, other)

        # (本人がまだしらない)アーティストのリストでFor分を回す
        for item in set_new_movie:

            # "類似度 x レビュー点数" を推薦度のスコアとして、全ユーザで積算する
            totals.setdefault(item,0)
            totals[item] += dataset[other][item]*sim 

            # またユーザの類似度の積算値をとっておき、これで上記のスコアを除する
            simSums.setdefault(item,0)
            simSums[item] += sim



    rankings = [(total/simSums[item],item) for item,total in totals.items() if simSums[item] != 0]
    rankings.sort()
    rankings.reverse()


    return [i[1] for i in rankings][:top_N]

# レコメンド結果の出力
if st.button("お勧めされたアーティスト上位3組を見る 'See the Top 3 recommended artists'"):
    a = get_recommend(name, 3)
    st.write('1', a[0])
    st.write('2', a[1])
    st.write('3', a[2])

if st.button("考慮に入れられたアーティスト全50組を見る 'See all 50 artists taken into consideration'"):
    st.write("'BTS', 'YOASOBI', 'back number', 'Official髭男dism', '日向坂46', '優里', 'Ado', 'LiSA', 'あいみょん', 'SEVENTEEN', '平井大', 'TWICE', 'King Gnu', '藤井風', 'エド・シーラン', '米津玄師', 'Novelbright', 'Mrs.GREEN APPLE', 'DISH//', 'ONE OK ROCK', '星野源', 'ジャスティン・ビーバー', '菅田将暉', 'Snow Man', 'yama', 'マカロニえんぴつ', 'ずっと真夜中でいいのに。', 'King & Prince', '嵐', 'Ayase', '[Alexandros]', 'スピッツ', '緑黄色社会', '乃木坂46', 'GReeeeN', 'BUMP OF CHICKEN', 'NiziU', 'きゃりーぱみゅぱみゅ', '青山テルマ', 'Mr.Children', '宇多田ヒカル', 'Creepy Nuts', 'SEKAI NO OWARI', 'SixTONES', 'millennium parade', 'スキマスイッチ', '福山雅治', 'aiko', 'サザンオールスターズ', '椎名林檎'")

if st.button("使われたアルゴリズムを見る'See the algorithm'"):
    """
    ```python
    # ピアソン類似度を算出する関数'Function to calculate Pearson similarity'
    def pearson_correlation(person1, person2):

        both_rated = {}
        for item in dataset[person1]:
            if item in dataset[person2]:
                both_rated[item] = 1

        number_of_ratings = len(both_rated)

        if number_of_ratings == 0:
            return 0

        # 各ユーザーごとのすべての好みを追加'Add all preferences for each user'
        person1_preferences_sum = sum(
            [dataset[person1][item] for item in both_rated])
        person2_preferences_sum = sum(
            [dataset[person2][item] for item in both_rated])

        # 各ユーザーの好みの値の二乗を計算'Calculate the square of each user's preference value'
        person1_square_preferences_sum = sum(
            [pow(dataset[person1][item], 2) for item in both_rated])
        person2_square_preferences_sum = sum(
            [pow(dataset[person2][item], 2) for item in both_rated])

        # アイテムごとのユーザー同士のレーティングを算出して合計'Calculate and total user-to-user ratings for each item'
        product_sum_of_both_users = sum(
            [dataset[person1][item] * dataset[person2][item] for item in both_rated])

        # ピアソンスコアの計算'Calculate Pearson Score'
        numerator_value = product_sum_of_both_users - \
            (person1_preferences_sum * person2_preferences_sum / number_of_ratings)
        denominator_value = sqrt((person1_square_preferences_sum - pow(person1_preferences_sum, 2) / number_of_ratings) * (
            person2_square_preferences_sum - pow(person2_preferences_sum, 2) / number_of_ratings))
        if denominator_value == 0:
            return 0
        else:
            r = numerator_value / denominator_value
            return r
    ```
    ```python
    # ある人に対して、推薦度の高い順にアーティストをレコメンドする 'Recommend artists to the user in order of recommendation'
    def get_recommend(person, top_N):

        totals = {} ; simSums = {} 
        list_others = list(dataset.keys()) ; list_others.remove(person)

        for other in list_others:
            set_other = set(dataset[other]); set_person = set(dataset[person])
            set_new_movie = set_other.difference(set_person)

            # あるユーザと本人の類似度を計算(simは0~1の数字)'Calculate the similarity between the user and other'
            sim = pearson_correlation(person, other)

            # (本人がまだしらない)アーティストのリストでFor文'For loop in the list of artists'
            for item in set_new_movie:

                # "類似度 x レビュー点数" を推薦度のスコアとして、全ユーザで積算する'Similarity x Review Score" is used as the recommendation score and summed for all users.'
                totals.setdefault(item,0)
                totals[item] += dataset[other][item]*sim 

                # またユーザの類似度の積算値をとっておき、これで上記のスコアを除する'Also, keep the total of the user's similarity and divide the above score by it.'
                simSums.setdefault(item,0)
                simSums[item] += sim

        rankings = [(total/simSums[item],item) for item,total in totals.items() if simSums[item] != 0]
        rankings.sort()
        rankings.reverse()

        return [i[1] for i in rankings][:top_N]
    ```
    """
