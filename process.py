import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin


class GetDummies(BaseEstimator, TransformerMixin):
    '''
    A Dataframe transformer that provide dummy variable encoding
    
    '''    
    def transform(self, X, **transformparams):
        '''
        Returns a dummy variable encoded version of a DataFrame
        
        Inputs:
            X :pandas DataFrame
        
        Returns:
            X_transformed: pandas DataFrame with new encoding    
        '''
        # check that we have a DataFrame with same column names as the one we fit
        if set(self._columns) != set(X.columns):
            raise ValueError('Passed DataFrame has different columns than fit DataFrame')
        elif len(self._columns) != len(X.columns):
            raise ValueError('Passed DataFrame has different number of columns than fit DataFrame')
          
        # create separate array for new encoded categoricals
        X_cat = np.empty((len(X), self._total_cat_cols), dtype='int')
        i = 0
        for col in self._columns:
            vals = self._cat_cols[col]
            for val in vals:
                X_cat[:, i] = X[col] == val
                i += 1
                
        return pd.DataFrame(data=X_cat, columns=self._feature_names)

    
    def fit(self, X, y=None, **fitparams):
        # Assumes X is a DataFrame
        self._columns = X.columns.values
        self._feature_names = []
        self._total_cat_cols = 0
        # Create a dictionary mapping categorical column to unique values
        self._cat_cols = {}
        for col in self._columns: 
            vals = X[col].value_counts().index.values
            vals = np.sort(vals)
            col_names = [col + '_' + str(int(val)) for val in vals]
            self._feature_names = np.append(self._feature_names, col_names)
            self._cat_cols[col] = vals
            self._total_cat_cols += len(vals)
        return self
    
    def get_feature_names(self):
        return self._feature_names

