from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder


def remove_duplicates(df):

    df = df.drop_duplicates()

    return df


def encode_features(df):

    encoder = LabelEncoder()

    categorical_cols = [
        'sex',
        'smoker',
        'region'
    ]

    for col in categorical_cols:

        if col in df.columns:

            df[col] = encoder.fit_transform(
                df[col]
            )

    return df


def scale_features(X):

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    return X_scaled
