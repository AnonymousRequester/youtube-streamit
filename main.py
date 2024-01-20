import streamlit as st
import time


st.title('Test')

st.write('プレグロスバーの表示')
'Start!!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}%')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!'

# left_column, right_column = st.columns(2)
# button = left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('ここは右カラム')

# expa = st.expander('問い合わせ')
# expa.write('問い合わせ内容を書く')
# expa.write('問い合わせ内容を書く')
# expa.write('問い合わせ内容を書く')
# expa.write('問い合わせ内容を書く')


# text = st.text_input('あなたの趣味を教えてください。')
# condition = st.slider('あなたの今のコンディションは？', 0, 10, 5)

# 'あなたの趣味：', text
# 'あなたの趣味：', condition


# if st.checkbox('Show Image'):
#     img = Image.open('20231028.jpeg')
#     st.image(img, caption='LC500', use_column_width=True)



# st.video('https://www.youtube.com/watch?v=LAK8ylcvHrg', start_time=60)

# st.write('DataFrame')

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

# st.map(df)

# st.line_chart(df)

# st.write(df)
# st.dataframe(df.style.highlight_max(axis=0), width=1000, height=500)
# st.table(df.style.highlight_max(axis=0))



# """
# Python 初級編
# """
# # Pythonコードを表示
# python_code = """
# def hello_world():
#     print("Hello, World!")

# hello_world()
# """

# # st.code()メソッドを使用してコードを表示
# st.code(python_code, language='python')
