def main(x):
    conditions = {
        x[2] == 1987:
            {
                x[0] == 'DART':
                    {
                        x[1] == 'SLIM': 0,
                        x[1] == 'BISON': 1,
                        x[1] == 'JULIA': 2
                    },
                x[0] == 'NU':
                    {
                        x[3] == 1993: 3,
                        x[3] == 1976: 4,
                        x[3] == 2012: 5
                    }
            },
        x[2] == 1973:
            {
            x[0] == 'DART':
                {
                    x[1] == 'SLIM': 6,
                    x[1] == 'BISON': 7,
                    x[1] == 'JULIA': 8
                },
            x[0] == 'NU': 9
            },
        x[2] == 1978: 10
    }

    while isinstance(conditions, dict):
        conditions = conditions[True]
    return conditions

print(main(['NU', 'JULIA', 1973, 2012]))
print(main(['NU', 'SLIM', 1978, 1976]))
