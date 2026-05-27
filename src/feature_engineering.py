def create_features(df):

    # BMI Risk Category

    if 'bmi' in df.columns:

        df['bmi_category'] = df['bmi'].apply(

            lambda x:

            'Underweight'
            if x < 18.5

            else 'Normal'
            if x < 25

            else 'Overweight'
            if x < 30

            else 'Obese'

        )

    return df
