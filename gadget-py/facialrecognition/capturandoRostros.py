import cv2
import os
import imutils


def processPerson(dataPath, fileName):
    person = fileName.split(".", 1)[0]
    absolutePersonalPath = os.path.join(dataPath, person)
    absoluteFilePath = os.path.join(dataPath, fileName)
    count = 0

    if not os.path.exists(absolutePersonalPath):
        print('Carpeta creada: ', absolutePersonalPath)
        os.makedirs(absolutePersonalPath)
    else:
        count = len(os.listdir(absolutePersonalPath))

    print("Processing file ", absoluteFilePath, " count ", count)

    cap = cv2.VideoCapture(absoluteFilePath)

    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:

        ret, frame = cap.read()
        if ret == False: break
        frame = imutils.resize(frame, width=640)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = frame.copy()

        faces = faceClassif.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            face = auxFrame[y:y + h, x:x + w]
            face = cv2.resize(face, (150, 150), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(absolutePersonalPath + '/face_{}.jpg'.format(count), face)
            count = count + 1
        cv2.imshow('frame', frame)

        k = cv2.waitKey(1)
        if k == 27 or count >= 1300:
            break

    cap.release()
    cv2.destroyAllWindows()




# getting data directory
dataPath = os.path.join(os.path.abspath(os.getcwd()), 'data')
print('Reading data from directory: ', dataPath)

# getting video files
filenames = next(os.walk(dataPath), (None, None, []))[2]
print('files: ', filenames)

# read files and create folders if it does not exist and create files
for name in filenames:
    if not name.startswith("."):
        processPerson(dataPath, name)

# directories = next(os.walk(dataPath))[1]
# print('directories: ', directories)

# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
