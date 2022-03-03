import cv2
import numpy as np

class_names = ["bad","good"]

model = cv2.dnn.readNet(model='../../input/DenseNet_121.caffemodel', config='../../input/DenseNet_121.prototxt', framework='Caffe')

image = cv2.imread('../../input/image_1.jpg')
blob = cv2.dnn.blobFromImage(image=image, scalefactor=1, size=(256, 256), mean=(104, 117, 123))
model.setInput(blob)
outputs = model.forward()
final_outputs = outputs[0]
final_outputs = final_outputs.reshape(1000, 1)
label_id = np.argmax(final_outputs)
probs = np.exp(final_outputs) / np.sum(np.exp(final_outputs))
final_prob = np.max(probs) * 100
out_name = class_names[label_id]
out_text = f"{out_name}, {final_prob:.3f}"
print(out_text)