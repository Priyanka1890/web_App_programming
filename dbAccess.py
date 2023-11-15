import pandas as pd


def insert_new_registration_data(table_name: str, names: str, passwords: str, phones: str, emails: str,
                                 addresss: str) -> int:
    old_df = pd.read_csv(table_name, index_col=False)  # existing table data
    idx = len(old_df)
    new_data_point = pd.DataFrame([{
        "idx": idx,
        "name": names,
        "password": passwords,
        "address": addresss,
        "phone": phones,
        "email": emails,
    }])
    new_df = pd.concat([old_df, new_data_point], axis=0)
    new_df.to_csv(table_name, index=False)
    if len(old_df) < len(new_df):
        return 1
    else:
        return 0


def check_login_data(table_name, emails, passwords) -> int:
    df = pd.read_csv(table_name)  # existing table data
    selected_df = df[(df.email == emails) & (df.password.values.astype('str') == passwords)]
    print(selected_df)
    if len(selected_df) > 0:
        return 1
        else:
        return 0
