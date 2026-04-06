import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib # We need this to save the scaler!

print("🧠 Loading Massive Dataset...")
# 1. Load the new 750-row dataset
df = pd.read_csv('massive_complexity_data.csv')

# 2. Encode Text to Numbers (0 to 4)
encoder = LabelEncoder()
df['Complexity_Encoded'] = encoder.fit_transform(df['Complexity'])

# Print the mapping so we know which number the AI assigned to which algorithm
print("\n🔑 Encoding Map:")
for i, item in enumerate(encoder.classes_):
    print(f"  {item} = {i}")

X = df[['Complexity_Encoded', 'N_Value']].values
y = df['Time_Seconds'].values

# 3. Scale the Data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

print("\n🏗️ Building the Upgraded Architecture...")
# We increased the neurons to 32 to handle the 5 different algorithmic curves
model = tf.keras.Sequential([
    tf.keras.layers.Dense(32, activation='relu', input_shape=(2,)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1, activation='linear')
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

print("🔥 Training the AI on 750 rows... (This will be quick!)")
# Training for 300 epochs because the math is harder now
history = model.fit(X_train, y_train, epochs=300, validation_data=(X_test, y_test), verbose=0)
print("✅ Training Complete!")

# --- 4. THE MOST IMPORTANT STEP: SAVE THE MODEL ---
model.save('tle_predictor.h5')
# We also MUST save the scaler and encoder, or our web app won't know how to format user input!
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(encoder, 'encoder.pkl')
print("💾 Model officially saved as 'tle_predictor.h5'!")
print("💾 Scaler and Encoder saved as .pkl files!")

# --- 5. Final Real-World Test ---
print("\n🔮 Live AI Predictions for a massive input: N = 20,000:")

# Ask the encoder what the secret numbers for O(N log N) and O(N^2) are
nlogn_code = encoder.transform(['O(N log N)'])[0]
n2_code = encoder.transform(['O(N^2)'])[0]

# Setup the test cases
test_cases = np.array([
    [nlogn_code, 20000],
    [n2_code, 20000]
])

# Scale the test cases and predict
test_scaled = scaler.transform(test_cases)
predictions = model.predict(test_scaled)

print(f"-> O(N log N) loop: ~{predictions[0][0]:.4f} seconds.")
print(f"-> O(N^2) loop: ~{predictions[1][0]:.4f} seconds.")