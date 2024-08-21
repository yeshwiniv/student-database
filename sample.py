import pandas as pd
import pymysql
connection=pymysql.connect(host='localhost',
                           user='root',
                           password='y@9443057412',
                           db='college_svvcas')
cursor=connection.cursor()
cursor.execute("select*from student_bca");
student_bca=cursor.fetchall();
cursor.close()
df=pd.DataFrame(student_bca,columns=['Gender','Ethnicity','parental_level_of_education','lunch','Test_preparation_score','maths_score','reading-score','writing_score'])
print(df)
df.to_csv('stud_details.csv',index=False)
connection.close()
