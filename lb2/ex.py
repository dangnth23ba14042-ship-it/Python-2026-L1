import gzip
import pickle
import pandas as pd

df_students = pd.read_csv('students.csv')
df_scores = pd.read_csv('scores.csv')

df_main = pd.merge(df_students, df_scores, on='student_id', how='inner')

df_students.to_csv('students_export.csv', index=False)
df_scores.to_csv('scores_export.csv', index=False)
df_main.to_csv('merged_data.csv', index=False)

with open('students.txt', 'w', encoding='utf-8') as f:
  for row in df_students.itertuples():
    f.write(f'{row.student_id},{row.name},{row.major}\n')

data_to_pickle = {
    'students': df_students.to_dict(orient='records'),
    'scores': df_scores.to_dict(orient='records'),
}

with gzip.open('students.dat', 'wb') as f:
  pickle.dump(data_to_pickle, f)


def query_data(df):
  print("\n--- DataFrame Hiện Tại ---")
  print(df.head(10))
  print("\n--------------------------")
  condition = input(
      "Nhập điều kiện truy vấn Pandas (VD: name == 'Alice' hoặc python >="
      " 80): "
  )
  try:
    result = df.query(condition)
    print("\n--- Kết Quả Truy Vấn ---")
    print(result)
  except Exception as e:
    print(f"Lỗi cú pháp truy vấn: {e}")


query_data(df_main)