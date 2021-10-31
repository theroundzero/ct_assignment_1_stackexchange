import pandas as pd;
import re;

df = pd.read_csv('/home/rijo_thomas23/ownerposts.csv', sep=',', header=None)

df[1] = df[1].apply(lambda x: re.sub(r"[^a-zA-Z]+",' ', x))
df[2] = df[2].apply(lambda x: re.sub(r"[^a-zA-Z]+",' ', x))
df[3] = df[3].apply(lambda x: re.sub(r"[^a-zA-Z]+",' ', x))
df = df.groupby(0)

df.apply(lambda x: x.to_csv(r'{}.txt'.format(x.name),header=False,index=False, sep=','));
