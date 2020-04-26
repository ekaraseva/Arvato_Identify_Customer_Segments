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
          
        X_cat=pd.get_dummies(X.astype('category'))
        print (X_cat['GABAEUDETYP_5.0'])
        #X_cat[np.isnan(X_cat)]=0
        X_cat=X_cat.fillna(0)
        print (X_cat['GABAEUDETYP_5.0'])
                        
        return pd.DataFrame(data=X_cat, columns=self._feature_names)

    
    def fit(self, X, y=None, **fitparams):
        # Assumes X is a DataFrame
        self._columns = X.columns.values
        self._feature_names = list(pd.get_dummies(X.astype('category')).columns)
        self._total_cat_cols=len(pd.get_dummies(X.astype('category')).columns)

        return self
    
    def get_feature_names(self):
        return self._feature_names
