import pandas as pd;
import glob;

Path = "tfidResults";

filespath = glob.glob(Path + "/*.txt");

for compPath in filespath:
    filename = compPath.split('tfidResults/')[1];
    print(filename.split('.')[0]+' Owner User ID\n');
    df = pd.read_csv(compPath, sep="\t",header=None,names=["word","tfidf_score"]);
    df["word"] = df["word"].str.split(" ",n=1,expand=True);
    res = df.sort_values(by = ["tfidf_score"], ascending=False).head(10);
    print(res);
    print('\n\n\n');
