import pandas as pd

###读取*SearchStream.tsv文件

df1 = pd.read_csv(r'D:\dstn\test\Location.tsv',sep='\t',encoding='utf-8')###读取第一个文件

df2 = pd.read_csv(r'D:\dstn\test\UserInfo.tsv',sep='\t',encoding='utf-8') ###读取第二个文件

outfile = pd.merge(df1, df2,  left_on='Level', right_on=['UserID'])

##输出/生成文件
outfile.to_csv(r'D:\dstn\test\test3.csv',index=False,encoding='utf-8')


###可以将两张表粘在一起，但是不是表中的一列