import cv2
import mediapipe as mp
import numpy as np

def calcular_ear(puntos_ojo):
    # Convertimos los puntos de landmarks a arreglos numéricos de NumPy
    p1, p2, p3, p4, p5, p6 = [np.array([p.x, p.y]) for p in puntos_ojo]
    
    # Calculamos las distancias verticales entre los párpados
    dist_vertical_1 = np.linalg.norm(p2 - p6)
    dist_vertical_2 = np.linalg.norm(p3 - p5)
    
    # Calculamos la distancia horizontal entre las esquinas del ojo
    dist_horizontal = np.linalg.norm(p1 - p4)
    
    # Fórmula matemática oficial del Eye Aspect Ratio (EAR)
    ear = (dist_vertical_1 + dist_vertical_2) / (2.0 * dist_horizontal)
    return ear

def lanzar_laboratorio_ia_ear():
    print("🤖 [IA Ocular Advanced] Inicializando modelos biométricos de Google MediaPipe...")
    
    # 1. Inicializamos las soluciones de malla facial de MediaPipe
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(
        max_num_faces=1,
        refine_landmarks=True, # 🟢 OBLIGATORIO: Habilita los puntos ultra detallados de las pupilas y párpados
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )
    
    # Índices específicos de los 6 landmarks para el Ojo Izquierdo en la malla de MediaPipe
    LOGICA_OJO_IZQ = [362, 385, 387, 263, 373, 380]
    
    # Límites lógicos del negocio bancario preventivo
    UMBRAL_EAR = 0.22  # Si el EAR baja de este número, el ojo se considera cerrado
    CONSECUTIVE_FRAMES = 15  # Cantidad de cuadros (aprox 1.5 segs) para considerar fatiga crítica
    
    contador_cuadros_fatiga = 0
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("❌ Error: No se detecta flujo de hardware de video.")
        return

    print("🟢 Algoritmo EAR en línea. Analizando parpadeo y fatiga. Presione 'q' para salir.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        # Invertimos el frame horizontalmente para un efecto espejo natural en UX
        frame = cv2.flip(frame, 1)
        alto, ancho, _ = frame.shape
        
        # MediaPipe exige procesar en el espacio de color RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        resultados = face_mesh.process(rgb_frame)
        
        estado_alerta = "NORMAL"
        color_interfaz = (0, 255, 0) # Verde inicial
        
        if resultados.multi_face_landmarks:
            for face_landmarks in resultados.multi_face_landmarks:
                # Extraemos los puntos geométricos del ojo izquierdo
                puntos_ojo = [face_landmarks.landmark[i] for i in LOGICA_OJO_IZQ]
                
                # Calculamos el ratio de apertura ocular en tiempo real
                ear_actual = calcular_ear(puntos_ojo)
                
                # Dibujamos círculos dorados de auditoría sobre los párpados detectados
                for p in puntos_ojo:
                    cx, cy = int(p.x * ancho), int(p.y * alto)
                    cv2.circle(frame, (cx, cy), 2, (0, 204, 255), -1)
                
                # 2. EVALUACIÓN LOGICA AUTOMATIZADA
                if ear_actual < UMBRAL_EAR:
                    contador_cuadros_fatiga += 1
                else:
                    contador_cuadros_fatiga = 0
                
                # Si los ojos permanecen cerrados por más del límite de cuadros tolerado
                if contador_cuadros_fatiga >= CONSECUTIVE_FRAMES:
                    estado_alerta = "ALERTA: FATIGA DETECTADA CRITICA"
                    color_interfaz = (0, 0, 255) # Cambio instantáneo a Rojo de peligro
                    # 💡 AQUÍ SE INYECTARÁ EL LLAMADO DE API PARA MODIFICAR LA PANTALLA
                
                # Pintamos las métricas en la pantalla del laboratorio para control del usuario
                cv2.putText(frame, f"EAR: {ear_actual:.2f}", (30, 50), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, color_interfaz, 2)
                cv2.putText(frame, f"ESTADO: {estado_alerta}", (30, 90), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, color_interfaz, 2)

        cv2.imshow('Commonwealth Bank Simulation - Advanced AI Ocular Lab', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    face_mesh.close()
    print("🤖 Laboratorio de IA cerrado de forma segura.")

if __name__ == "__main__":
    lanzar_laboratorio_ia_ear()
