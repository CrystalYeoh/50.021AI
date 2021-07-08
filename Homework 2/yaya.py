#Reading the file
df = pd.read_json("drive/MyDrive/datasets/"+file)
df = df.drop_duplicates(subset='image_id', keep="first")

# If video is inverted
# df.keypoints =df.keypoints.apply(lambda x: flip(x))

# Setting labels
#            1        2           3          4           5               6             7              8            9          10          11           12       13         14         15           16          17      
labels = ["Nose", "LeftEye", "RightEye", "LeftEar",  "RightEar",  "LeftShoulder","RightShoulder","LeftElbow","RightElbow","LeftWrist","RightWrist","LeftHip","RightHip","LeftKnee","RightKnee","LeftAnkle","RightAnkle"]

sensor_data = pd.read_json("drive/MyDrive/datasets/dataset.json")
sensor_data = sensor_data.drop(index=range(8))
sensor_data = sensor_data.reset_index()
sensor_data["label"]= df.keypoints.apply(lambda x: categorise(x))
sensor_data["img_no"]= df.image_id

X = np.array(sensor_data[[1,2,3,4,5,6,7,8,9]])
y = np.array(sensor_data.label)

X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.33, random_state=42)

clf = RandomForestClassifier()
clf.fit(X_train,y_train)
prediction = clf.predict(X_test)
print(accuracy_score(y_test, prediction))

# does accuracy increase with more data:
   # if it does
      # this model is only applicable for this set of sensors (cannot generalise to other sensors), and this configuration
   # if it does not
      # sensor values are not congruent across different times, we probably need to change sensors to ensure congruency (better sensor), and then check whether it increases
