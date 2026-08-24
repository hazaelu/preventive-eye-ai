import cv2
import numpy as np

def lanzar_laboratorio_ia():
    print("🤖 [IA Ocular] Inicializando modelos lógicos de visión artificial...")
    
    # 1. Cargamos las redes de clasificadores pre-entrenados Haar Cascades desde el núcleo de OpenCV
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    
    # 2. Inicializamos el flujo de captura de video (0 = cámara local por defecto)
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("❌ Error: La infraestructura no detecta un flujo de video o cámara web activa.")
        return

    print("🟢 Algoritmo en línea. Escaneando patrones faciales. Presione 'q' para apagar de forma segura.")

    while True:
        # Capturamos el fotograma cuadro por cuadro
        ret, frame = cap.read()
        if not ret:
            break
            
        # Optimización Matemática: La visión artificial procesa matrices en escala de grises para máxima velocidad
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # 3. El modelo matemático escanea la matriz en busca de coordenadas faciales
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
        
        for (x, y, w, h) in faces:
            # Dibujamos un contenedor verde en el rostro (Grosor: 2px)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            # Segmentamos la Región de Interés (ROI) para economizar ciclos de procesamiento de CPU
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            
            # 4. Buscamos los patrones oculares exclusivamente dentro del rostro detectado
            eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=10, minSize=(15, 15))
            
            for (ex, ey, ew, eh) in eyes:
                # Dibujamos un contenedor dorado corporativo sobre las pupilas/mirada detectada
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 204, 255), 2)
                
                # 💡 LÓGICA PREVENTIVA FUTURA: Aquí evaluaremos el ratio de parpadeo (EAR) para modular el monitor
                
        # Proyectamos la ventana gráfica interactiva del laboratorio en tiempo real
        cv2.imshow('AI Eye Tracking Laboratory - Preventative Health Project', frame)
        
        # Escuchamos el teclado de forma asíncrona; si se presiona 'q', rompemos el bucle
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberamos el hardware y cerramos los hilos gráficos de forma limpia
    cap.release()
    cv2.destroyAllWindows()
    print("🤖 Laboratorio de Inteligencia Artificial cerrado correctamente.")

if __name__ == "__main__":
    lanzar_laboratorio_ia()
