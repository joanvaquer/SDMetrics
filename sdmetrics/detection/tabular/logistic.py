from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import RobustScaler

from sdmetrics.detection.tabular.base import TabularDetector


class LogisticDetector(TabularDetector):

    name = "logistic"

    def fit(self, X, y):
        """This function trains a sklearn pipeline with a robust scalar
        and a logistic regression classifier.

        Arguments:
            X (np.ndarray): The numerical features (i.e. transformed rows).
            y (np.ndarray): The binary classification target.
        """
        self.model = Pipeline([
            ('scalar', RobustScaler()),
            ('classifier', LogisticRegression(solver="lbfgs")),
        ])
        self.model.fit(X, y)

    def predict_proba(self, X):
        return self.model.predict_proba(X)[:, 1]
