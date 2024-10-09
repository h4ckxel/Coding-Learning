import cv2
import mediapipe as mp
import tensorflow as tf
import numpy as np

# inicializa mediapipe hands para detectar las manos en la imagen/video
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)  # detecta una mano a la vez con confianza mínima de 0.5
mp_drawing = mp.solutions.drawing_utils  # utilidad para dibujar puntos y conexiones de la mano

# carga el modelo de red neuronal entrenado previamente
model = tf.keras.models.load_model('LSM_model.h5')

# inicia la captura de video desde la cámara
cap = cv2.VideoCapture(0)

def preprocess_frame(frame):
    # convierte el fotograma de BGR a RGB, ya que mediapipe usa RGB como entrada
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # procesa la imagen para detectar la mano y obtener puntos de referencia
    result = hands.process(rgb_frame)
    
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # dibuja las marcas de la mano y las conexiones en el fotograma original (opcional)
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # obtiene el tamaño del fotograma actual
            h, w, c = frame.shape
            
            # encuentra los límites de la región de la mano (bounding box) usando las coordenadas normalizadas de los puntos detectados
            x_min = int(min([landmark.x for landmark in hand_landmarks.landmark]) * w)
            x_max = int(max([landmark.x for landmark in hand_landmarks.landmark]) * w)
            y_min = int(min([landmark.y for landmark in hand_landmarks.landmark]) * h)
            y_max = int(max([landmark.y for landmark in hand_landmarks.landmark]) * h)
            
            # ajusta los límites del bounding box para asegurarse de que no se salga de la imagen
            x_min = max(0, x_min)
            y_min = max(0, y_min)
            x_max = min(w, x_max)
            y_max = min(h, y_max)
            
            # recorta la región de la mano usando el bounding box calculado
            hand_frame = frame[y_min:y_max, x_min:x_max]
            
            # verifica que el recorte de la mano no esté vacío
            if hand_frame.size == 0:
                return None
            
            return hand_frame
    
    return None

# ciclo principal para capturar fotogramas y procesarlos
while True:
    ret, frame = cap.read()  # lee el fotograma de la cámara
    if not ret:
        break
    
    # preprocesa el fotograma actual para detectar la mano y recortar la región relevante
    hand_frame = preprocess_frame(frame)
    
    if hand_frame is not None:
        # redimensiona la imagen de la mano a (64, 64) píxeles para adaptarse a la entrada de la red neuronal
        input_image = cv2.resize(hand_frame, (64, 64))
        input_image = input_image / 255.0  # normaliza los valores de píxeles a un rango [0, 1]
        input_image = np.expand_dims(input_image, axis=0)  # agrega una dimensión para que tenga formato (1, 64, 64, 3)
        
        # realiza la predicción con el modelo cargado
        predictions = model.predict(input_image)
        predicted_class = np.argmax(predictions, axis=1)  # obtiene el índice de la clase con mayor probabilidad
        
        # define las etiquetas correspondientes a cada clase (por ejemplo: "hola", "gracias", etc.)
        class_labels = ["hola", "gracias", "por favor", "adios"]  # etiquetas de las clases de salida
        predicted_label = class_labels[predicted_class[0]]  # asigna la etiqueta correspondiente a la predicción
        
        # muestra la clase predicha en el fotograma en la parte superior izquierda
        cv2.putText(frame, f"Pred: {predicted_label}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    
    # muestra el fotograma procesado en la ventana de visualización
    cv2.imshow('Sign Language Detection', frame)
    
    # permite cerrar la ventana al presionar la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# libera la cámara y cierra todas las ventanas de OpenCV
cap.release()
cv2.destroyAllWindows()
'''
El proyecto aun sigue en proceso, faltan implementaciones al algoritmo.
'''
