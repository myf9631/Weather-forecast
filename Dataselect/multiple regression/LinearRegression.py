# coding=gbk
#�������ͼ������ݼ�
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame
from sklearn.model_selection import train_test_split

# ��ȡ�ļ�
data = pd.read_csv('dropzero_20181107-20190228.csv')
examDf = DataFrame(data)

# ������ϴ,�����һ���п��������ڣ������Ļ����Ǿ�ֻ��Ҫ�ӵڶ��п�ʼ�����ݣ�
# �������£��������������е�0��Ϊ1�ͺã�Ҫ��Щ��ȡ��Щ��
new_examDf = examDf.iloc[:, 0:]

# ��������
print(new_examDf.describe())  # ��������������ʾ��ֵ��ƽ��������Ϣ�����Լ��ж��������Ƿ����쳣ֵ
print(new_examDf[new_examDf.isnull() == True].count())  # ����ȱʧֵ�������Ϊ0��˵������û��ȱʧֵ

# ������ϵ�����ж��Ƿ�ֵ�������Իع�ģ��
print(new_examDf.corr())  # 0-0.3����أ�0.3-0.6����أ�0.6-1ǿ��أ�

# ͨ��seaborn���һ��������ֱ�ߺ�95%�����Ŵ���ֱ���ж���ع�ϵ
sns.pairplot(data, x_vars=['2','5','8'], y_vars= ['34'], size=7, aspect=0.8, kind='reg')
plt.show()


# ���ѵ�����Ͳ��Լ� 0.75��0.25
#0-33 һ��34������ ��Ϊ�Ա���x    34��ΪĿ��ֵ��
X_train, X_test, Y_train, Y_test = train_test_split(new_examDf.iloc[:, :34], new_examDf.iloc[:,34],
                                                    train_size=0.75,random_state=0)

print("�Ա���---Դ����:", new_examDf.iloc[:, :34].shape, "��  ѵ����:", X_train.shape, "��  ���Լ�:", X_test.shape)
print("�����---Դ����:", new_examDf.iloc[:,34].shape, "��    ѵ����:", Y_train.shape, "��  ���Լ�:", Y_test.shape)
# �������Թ滮��
model = LinearRegression()
model.fit(X_train, Y_train)  # ���Իع�ѵ��

a = model.intercept_  # �ؾ�
b = model.coef_  # �ع�ϵ��

print("��ϲ���:�ؾ�", a, ",�ع�ϵ����", b)

# ��ʾ���Է��̣������Ʋ�����С��λΪ��λ
print("��������: Y = ", round(a, 4), "+", round(b[0], 4), "* X1 + ", round(b[1], 4), "* X2 +",
      round(b[2],4),"* X3 + ",round(b[3], 4), "* X4 + ", round(b[4], 4), "* X5","+",round(b[5],4),"* X6 +",
round(b[6],4),"* X7 + ",round(b[7], 4), "* X8 + ", round(b[8], 4), "* X9","+",round(b[9],4), "* X10 +",
round(b[10],4),"* X11 + ",round(b[11], 4), "* X12 + ", round(b[12], 4), "* X13","+",round(b[13],4),"* X14 +",
round(b[14],4),"* X15 + ",round(b[15], 4), "* X16 + ", round(b[16], 4), "* X17","+",round(b[17],4), "* X18 +",
 round(b[18],4),"* X19 + ",round(b[19], 4), "* X20 + ", round(b[10], 4), "* X21","+",round(b[21],4), "* X22 +",
round(b[22],4),"* X23 + ",round(b[23], 4), "* X24 + ", round(b[24], 4), "* X25","+",round(b[25],4), "* X26 +",
round(b[26],4),"* X27 + ",round(b[27], 4), "* X28 + ", round(b[28], 4), "* X29","+",round(b[29],4), "* X30 +",
round(b[30],4),"* X31 + ",round(b[31], 4), "* X32 ",round(b[32],4),"* X33 + ",round(b[33], 4), "* X34 ")

# �Բ��Լ����ݣ���predict����Ԥ��
Y_pred = model.predict(X_test)

#��ӱ�ǩ��ͼ
plt.figure()
plt.plot(range(len(Y_pred)), Y_pred, 'red', linewidth=2.5, label="predict data")
plt.plot(range(len(Y_test)), Y_test, 'green', label="test data")
plt.show()

plt.figure()
y = Y_pred - Y_test
plt.plot(y)
#ͼ��λ�����Ͻǣ�����2���ޣ����Ƶģ�1Ϊ���Ͻǣ�3Ϊ���½ǣ�4Ϊ���½�
plt.legend(loc=2)
plt.show()  # ��ʾԤ��ֵ�����ֵ����


#׼ȷ��
score = model.score(X_test,Y_test)
print('׼ȷ��:',score)