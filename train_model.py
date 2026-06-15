import pandas as pd
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

data = pd.read_csv("diet_health_dataset.csv")

le_gender = LabelEncoder()
le_disease = LabelEncoder()
le_food = LabelEncoder()
le_diet = LabelEncoder()

data['Disease'] = data['Disease'].fillna('None')
data['Gender'] = le_gender.fit_transform(data['Gender'])
data['Disease'] = le_disease.fit_transform(data['Disease'])
data['Food_Preference'] = le_food.fit_transform(data['Food_Preference'])
data['Recommended_Diet'] = le_diet.fit_transform(data['Recommended_Diet'])

X = data[['Age','Gender','Height_cm','Weight_kg','BMI','Disease','Food_Preference','Calories_Intake']]
y = data['Recommended_Diet']

X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.2,random_state=42,stratify=y
)

param_grid = {
    'n_estimators':[200,300],
    'max_depth':[10,15],
    'min_samples_split':[2,5],
    'min_samples_leaf':[1,2]
}

grid = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5, n_jobs=-1)
grid.fit(X_train,y_train)

model = grid.best_estimator_

joblib.dump(model,"diet_model.pkl")
joblib.dump(le_gender,"le_gender.pkl")
joblib.dump(le_disease,"le_disease.pkl")
joblib.dump(le_food,"le_food.pkl")
joblib.dump(le_diet,"le_diet.pkl")

print("Model saved successfully")
