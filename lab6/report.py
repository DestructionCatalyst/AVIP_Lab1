import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv('result.csv')
    for hypothesis in df[['0']].iterrows():
        sym = hypothesis[1][0]
        sym = sym.replace("(", "").replace(")", "")
        sym, feat, prof = sym.split(",")
        print(f"{hypothesis[0]}: {sym} -{feat} по признакам,{prof} по профилям;\\")
