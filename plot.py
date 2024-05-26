import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    dfNew = pd.read_csv('new_data.csv')
    dfcat = dfNew['Category'] == 5
    df1 = dfNew[dfcat]
    print(df1)
    fig=plt.figure(figsize=(10,8))
    ax=fig.gca()
    df1.hist(column='year', bins=100, ax=ax)

    plt.show()

if __name__ == '__main__':
    main()
