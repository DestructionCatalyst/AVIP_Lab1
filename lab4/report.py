import pandas as pd


if __name__ == '__main__':
    features = pd.read_csv('features.csv')
    for index, row in features.iterrows():
        asd = \
        """
## Символ {letter}

![Letter](./generated/letter_{znum}.png), ![Letter](./profiles/x/{znum}.png) ![Letter](./profiles/y/{znum}.png)\\

Признаки:
- Вес чёрного = {weight}
- Нормированный вес чёрного = {nweight}
- Центр масс = ({centerx}, {centery})
- Нормированный центр масс = ({ncenterx}, {ncentery})
- Моменты инерции = ({inertiax}, {inertiay})
- Нормированные моменты инерции = ({ninertiax}, {ninertiay})
        """.format(
            letter=row.letter,
            znum=str(index + 1).zfill(2),
            weight=row.weight,
            nweight=row.relative_weight,
            centerx=row.center_x,
            centery=row.center_y,
            ncenterx=row.relative_center_x,
            ncentery=row.relative_center_y,
            inertiax=row.inertia_x,
            inertiay=row.inertia_y,
            ninertiax=row.relative_inertia_x,
            ninertiay=row.relative_inertia_y,
        )
        print(asd)
