import sys
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path: str = os.path.join('artifacts', 'preprocessor.pkl')
    numerical_features = ['reading score', 'writing score']
    categorical_features =['gender','race/ethnicity','parental level of education','lunch','test preparation course']


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.preprocessor = self._create_preprocessor()

    def _create_preprocessor(self):
        try:
            num_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler(with_mean=False))
                ])

            cat_pipeline = Pipeline(
                steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('onehot', OneHotEncoder(handle_unknown='ignore')),
                ('scaler', StandardScaler(with_mean=False))
            ])

            logging.info("numerical features standard scaling completed")
            logging.info("categorical features encoding completed")

            # Create the preprocessor using ColumnTransformer
            preprocessor = ColumnTransformer([
                ('num', num_pipeline, self.config.numerical_features),
                ('cat', cat_pipeline, self.config.categorical_features)
            ])
            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)

            logging.info("Train and Test data read successfully")

            # Separate features and target
            X_train = train_data.drop(columns=['math score'],axis=1)
            y_train = train_data['math score']
            X_test = test_data.drop(columns=['math score'],axis=1)
            y_test = test_data['math score']

            logging.info("Applying preprocessing object on training and testing data")

            # Fit and transform the data
            X_train_transformed = self.preprocessor.fit_transform(X_train)
            X_test_transformed = self.preprocessor.transform(X_test)

            train_array = np.c_[X_train_transformed, np.array(y_train)]
            test_array = np.c_[X_test_transformed, np.array(y_test)]

            logging.info("Saved preprocessing object.")
            
            # Save the preprocessor object
            save_object(
                file_path=self.config.preprocessor_obj_file_path,
                obj=self.preprocessor
            )

            return train_array, test_array, self.config.preprocessor_obj_file_path

        except Exception as e:
            raise CustomException(e, sys)